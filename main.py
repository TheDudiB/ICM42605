#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from PyQt4.QtGui import QApplication, QFileDialog, QMessageBox, QMainWindow, QDoubleSpinBox, QAbstractSpinBox\
                        ,QDesktopWidget
from PyQt4.QtCore import pyqtSlot, QTimer, QSettings
from serial.tools.list_ports import comports
from numpy import matrix, array, sin, pi, arctan2, cos, NaN, sign, arcsin, sqrt, eye
from mainWin import Ui_MainWindow
from pyqtgraph import PlotWidget
from stream import GetValue, test_con

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
dt = 1/100.0


def com_select():
    """Sets the selected com in qtComPorts
    i -> index value of qtComPorts
    first_time -> first calling signal isn't establish"""
    if 'win' in sys.platform:
        ports = [x.device
                 for x in comports()]
    else:
        ports = ['/dev/' + x.device
                 for x in comports() if 'AMA' not in x.name and x.name]
    return ports


class MainUi(QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        monitor = QDesktopWidget().screenGeometry(0)
        #self.move(monitor.left(), monitor.top())
        #self.showFullScreen()
        self.settings = QSettings('Elbit', 'Minhal')
        self.AMatrix = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.SMatrix = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.external_select, self.IMU_select = 0, 0
        self.RawDataF, self.BiasF, self.align, self.recF, self.scale = 0, 0, 0, 0, 0
        self.rate, self.FLOS, self.cube = 0, 0, 0
        self.comport = None
        self.LOS = array([0, 0, 0])
        self.R = ang2u(self.LOS)
        self.RawSF = float(self.ui.qtSGyroSF.value())
        self.BiasX, self.BiasY, self.BiasZ = 0.0, 0.0, 0.0
        mapFunc = [self.ui.qtSBiasX,
                   self.ui.qtSBiasY,
                   self.ui.qtSBiasZ,
                   self.ui.qtSGyroSF]

        self.iStream = 0
        self.data = [[] for i in range(9)]
        self.data_LOS = [[] for i in range(3)]
        self.ui.qtBStream.clicked.connect(self.stremingData)
        self.ui.verticalLayoutW.removeWidget(self.ui.widget)
        self.ui.widget.close()
        self.ui.plot = PlotWidget(name='gyro data', title='Gyro data x-Red y-Green z-Blue')
        self.ui.plotx = self.ui.plot.plot(pen=red, name='Gyro X')
        self.ui.ploty = self.ui.plot.plot(pen=green, name='Gyro Y')
        self.ui.plotz = self.ui.plot.plot(pen=blue, name='Gyro Z')
        self.ui.plot.setLabel('bottom', 'smaple no')
        self.ui.plot.setLabel('left', 'rate (bit)')
        self.ui.verticalLayoutW.addWidget(self.ui.plot)  # need to improve
        self.ui.qtCRawData.clicked.connect(self.changed)
        self.ui.qtCBias.clicked.connect(self.changed)
        self.ui.qtCAlign.clicked.connect(self.changed)
        self.ui.qtCScale.clicked.connect(self.changed)
        self.ui.qtRERate.clicked.connect(self.external_disp)
        self.ui.qtRECube.clicked.connect(self.external_disp)
        self.ui.qtRELOS.clicked.connect(self.external_disp)
        self.ui.qtRILOS.clicked.connect(self.IMU_display)
        self.ui.qtRICube.clicked.connect(self.IMU_display)
        self.ui.qtRIBoth.clicked.connect(self.IMU_display)
        [x.valueChanged.connect(self.value_chane) for x in mapFunc]
        self.ui.actionAbout.triggered.connect(self.Help)
        self.ui.qtBResetLOS.clicked.connect(self.reset_los)
        for i in range(3):
            for j in range(3):
                cell = QDoubleSpinBox(self.ui.qtAlignMat)
                cell.setButtonSymbols(QAbstractSpinBox.NoButtons)
                cell.setMinimum(0.0001 if i == j else -99.9999)
                cell.setDecimals(4)
                cell.setMaximum(99.9999)
                cell.setValue(1 if i == j else 0)
                cell.cellLoc = (i, j)
                cell.who_ur_dady = 'qtAlignMat'
                cell.valueChanged.connect(self.cell_change)
                self.ui.qtAlignMat.setCellWidget(i, j, cell)
        for i in range(3):
            for j in range(3):
                cell = QDoubleSpinBox(self.ui.qtScaleMat)
                cell.setButtonSymbols(QAbstractSpinBox.NoButtons)
                cell.setMinimum(0.0001 if i == j else -99.9999)
                cell.setDecimals(4)
                cell.setMaximum(99.9999)
                cell.setValue(1 if i == j else 0)
                cell.cellLoc = (i, j)
                cell.who_ur_dady = 'qtScaleMat'
                cell.valueChanged.connect(self.cell_change)
                self.ui.qtScaleMat.setCellWidget(i, j, cell)
        self.update_data()


    def update_data(self):
        self.AMatrix = self.settings.value('AMatrix', array([[1.0, 0, 0], [0, 1.0, 0], [0, 0, 1.0]])).toPyObject()
        self.SMatrix = self.settings.value('SMatrix', array([[1.0, 0, 0], [0, 1.0, 0], [0, 0, 1.0]])).toPyObject()
        self.BiasX = float(self.settings.value('BiasX', 0).toPyObject())
        self.BiasY = float(self.settings.value('BiasY', 0).toPyObject())
        self.BiasZ = float(self.settings.value('BiasZ', 0).toPyObject())
        self.RawSF = float(self.settings.value('RawSF', 1.0).toPyObject())

        for i in range(3):
            for j in range(3):
                cell = self.ui.qtAlignMat.cellWidget(i, j)
                cell.setValue(self.AMatrix[i, j])
                cell = self.ui.qtScaleMat.cellWidget(i, j)
                cell.setValue(self.SMatrix[i, j])
        self.ui.qtSBiasX.setValue(self.BiasX)
        self.ui.qtSBiasY.setValue(self.BiasY)
        self.ui.qtSBiasZ.setValue(self.BiasZ)
        self.ui.qtSGyroSF.setValue(self.RawSF)

    @pyqtSlot()
    def reset_los(self):
        self.LOS = array([0, 0, 0])
        self.R = ang2u(self.LOS)

    @pyqtSlot(float)
    def value_chane(self, val):
        s = self.sender()
        if s == self.ui.qtSBiasX:
            self.BiasX = val
        elif s == self.ui.qtSBiasY:
            self.BiasY = val
        elif s == self.ui.qtSBiasZ:
            self.BiasZ = val
        elif s == self.ui.qtSGyroSF:
            self.RawSF = val
        else:
            print('Whos this?')


    @pyqtSlot(bool)
    def external_disp(self, f):
        self.external_select = [self.ui.qtRERate, self.ui.qtRECube, self.ui.qtRELOS].index(self.sender())
        if self.external_select == 2:
            self.ui.plot.setLabel('left', 'LOS [°]')
            self.ui.plot.setTitle('LOS AZ-Red EL-Green RO-Blue')
        if self.external_select == 0:
            self.ui.plot.setLabel('left', 'rate (°/sec)' if self.RawDataF else 'rate (bit)')
            self.ui.plot.setTitle('Gyro data x-Red y-Green z-Blue')

    @pyqtSlot(bool)
    def IMU_display(self, f):
        self.IMU_select = [self.ui.qtRILOS, self.ui.qtRICube, self.ui.qtRIBoth].index(self.sender())


    @pyqtSlot()
    def changed(self):
        if self.ui.qtCRawData == self.sender():
            self.RawDataF = not self.RawDataF
            self.ui.plot.setLabel('left', 'rate (°/sec)' if self.RawDataF else 'rate (bit)')
            if self.ui.qtCBias.isChecked():
                self.ui.qtSBiasX.setEnabled(self.RawDataF)
                self.ui.qtSBiasY.setEnabled(self.RawDataF)
                self.ui.qtSBiasZ.setEnabled(self.RawDataF)
                self.ui.qtCBias.setChecked(self.RawDataF)
                self.BiasF = not self.BiasF
            if self.ui.qtCAlign.isChecked():
                self.ui.qtAlignMat.setEnabled(self.RawDataF)
                self.ui.qtCAlign.setChecked(self.RawDataF)
                self.align = not self.align
            if self.ui.qtCScale.isChecked():
                self.ui.qtScaleMat.setEnabled(self.RawDataF)
                self.ui.qtCScale.setChecked(self.RawDataF)
                self.scale = not self.scale
        elif self.ui.qtCBias == self.sender():
            self.BiasF = not self.BiasF
        elif self.ui.qtCAlign == self.sender():
            self.align = not self.align
        elif self.ui.qtCScale == self.sender():
            self.scale = not self.scale
        elif self.ui.qtCLOS == self.sender():
            self.FLOS = not self.FLOS
        elif self.ui.qtCCube == self.sender():
            self.cube = not self.cube


    @pyqtSlot(float)
    def cell_change(self, val):
        s = self.sender()
        x, y = s.cellLoc
        if s.who_ur_dady == 'qtAlignMat':
            self.AMatrix[x, y] = val
        elif s.who_ur_dady == 'qtScaleMat':
            self.SMatrix[x, y] = val


    @pyqtSlot()
    def file_select(self):
        """Select a file to edit and place it at the qtBrowse
        replace prevous value"""
        fname = QFileDialog.getSaveFileName(self,
                                            'select file',
                                            '/home/pi/Documents/output.csv',
                                            "csv file (*.csv)")
        self.ui.qtBrowse.clear()
        self.ui.qtBrowse.setText(fname)

    @pyqtSlot()
    def stremingData(self):
        """Fuction streams to pyqtgraph the sensor data,
        if function is streaming the function stops the data"""
        ports = com_select()
        self.comport = None
        if not ports:
            QMessageBox.warning(self, 'No Connection',
                                "No unit found please verify that the IMU is connected")
        else:
            for port in ports:
                if test_con(port):
                    self.comport = port
                    break
            if self.comport:
                if self.ui.qtBStream.text() == 'Stream':
                    self.ui.qtBStream.setText('Stop')
                    self.streamData = GetValue(self.comport)
                    self.streamData.start()
                    iter(self.streamData)
                    self.timer = QTimer()
                    self.timer.timeout.connect(self.graphupdate)
                    self.i = 0
                    self.__x = []
                    if self.recF:
                        if self.ui.qtBrowse.text() == '':
                            self.file_select()
                            if self.ui.qtBrowse.text() == '':
                                QMessageBox.warning(self,
                                                    'No file',
                                                    'No file selected')
                                self.stremingData()
                                return 0
                    self.timer.start()
                elif self.ui.qtBStream.text() == 'Stop':
                    self.ui.qtBStream.setText('Stream')
                    self.timer.stop()
                    self.streamData.stop()
                    self.data = [[] for i in range(8)]
            else:
                QMessageBox.warning(self, 'No Connection com search',
                                    "No unit found please verify that the IMU is connected")

    @pyqtSlot()
    def graphupdate(self):
        data = next(self.streamData)
        if data:
            gyro = array([data[5], data[6], data[7]])
            if self.RawDataF:
                gyro = gyro / self.RawSF
            if self.BiasF:
                gyro = gyro - array([self.BiasX, self.BiasY, self.BiasZ])
            if self.align:
                gyro = gyro.dot(self.AMatrix)
            if self.scale:
                gyro = gyro.dot(self.SMatrix)

            gyro_rad_dt = deg2rad(gyro) * dt
            self.R = rotation_integration(gyro_rad_dt).dot(self.R)
            self.LOS = rad2deg(u2ang(self.R))
            if len(self.data_LOS[0]) >= 500:
                _ = [self.data_LOS[i].pop(0) for i in range(3)]
            [self.data_LOS[i].append(self.LOS[i]) for i in range(3)]
            [x.display(self.LOS[i]) for i, x in enumerate([self.ui.qtLOSX, self.ui.qtLOSY, self.ui.qtLOSZ])]

            if len(self.data[0]) >= 500:
                _ = [self.data[i].pop(0) for i in range(len(self.data))]
                _ = self.__x.pop(0)
                self.__x.append(self.__x[-1] + 1)
            else:
                self.__x.append(len(self.__x))
            data[5], data[6], data[7] = list(gyro)
            [self.data[i].append(d) for i, d in enumerate(data)]
            # sdata = [str(x) for x in data]
            # self.fileName.write(','.join(sdata))
            if self.i > 3:
                [x.display(gyro[i]) for i, x in enumerate([self.ui.qtRateX, self.ui.qtRateY, self.ui.qtRateZ])]
                if self.external_select == 2:
                    self.ui.plotx.setData(x=self.__x, y=self.data_LOS[0])
                    self.ui.ploty.setData(x=self.__x, y=self.data_LOS[1])
                    self.ui.plotz.setData(x=self.__x, y=self.data_LOS[2])
                else:
                    self.ui.plotx.setData(x=self.__x, y=self.data[5])
                    self.ui.ploty.setData(x=self.__x, y=self.data[6])
                    self.ui.plotz.setData(x=self.__x, y=self.data[7])
                self.i = 0
                #avgX = avg(self.data[5])
                #avgY = avg(self.data[6])
                #avgZ = avg(self.data[7])
                #title = '{:.2} {:.2} {:.2}'.format(avgX, avgY, avgZ)
                #self.ui.plot.setTitle(title)
            else:
                self.i += 1

    def closeEvent(self, event):
        if self.ui.qtBStream.text() == 'Stop':
            self.timer.stop()
            self.streamData.stop()
        self.settings.setValue('AMatrix', self.AMatrix)
        self.settings.setValue('SMatrix', self.SMatrix)
        self.settings.setValue('BiasX', self.BiasX)
        self.settings.setValue('BiasY', self.BiasY)
        self.settings.setValue('BiasZ', self.BiasZ)
        self.settings.setValue('RawSF', self.RawSF)
        super(MainUi, self).closeEvent(event)

    @pyqtSlot()
    def Help(self):
        QMessageBox.information(self, 'Who you gonna call', 'Call Dudi for help')


def avg(x):
    return sum(x) * 1.0 / len(x)


def cross_matrix(w):
    return array([[0, -w[2], w[1]],
                  [w[2], 0, -w[0]],
                  [-w[1], w[0], 0]])


def mysinc(x):
    if x > 1e-9:
        return sin(x*pi)/x/pi
    else:
        return 1


def u2ang(u):
    if abs(u[0, 2]) - 1 > 1e-9:
        # not a rotation matrix
        angle = array([NaN, NaN, NaN])
    elif abs(u[0, 2]) - 1 >= 0:
        # gimble lock
        angle = array([arctan2(u[0, 1], u[0, 0]), -pi / 2 * sign(u[0, 2]), 0])
    else:
        angle = array([arctan2(u[0, 1], u[0, 0]), -arcsin(u[0, 2]), arctan2(u[1, 2], u[2, 2])])
    return angle


def ang2u(ang):
    caz = cos(ang[0])
    saz = sin(ang[0])
    cel = cos(ang[1])
    sel = sin(ang[1])
    crl = cos(ang[2])
    srl = sin(ang[2])

    return array([[caz * cel, saz * cel, -sel],
                  [-crl * saz + caz * sel * srl, caz * crl + saz * sel * srl, cel * srl],
                  [caz * crl * sel + saz * srl, crl * saz * sel - caz * srl, cel * crl]])


def rotation_integration(theta):
    crsmt = cross_matrix(theta)
    theta_norm = sqrt(sum(theta**2))
    if theta_norm > 0:
        return eye(3) + crsmt.dot(crsmt) / theta_norm**2 * (1-cos(theta_norm)) - crsmt*mysinc(theta_norm/pi)
    else:
        return eye(3)


def deg2rad(x):
    return x * 0.017453292519943295


def rad2deg(x):
    return x * 57.29577951308232

def main():
    app = QApplication(sys.argv)
    ex = MainUi()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
