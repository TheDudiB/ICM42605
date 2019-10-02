#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import QWidget, QFont, QApplication, QFileDialog, QMessageBox
from PyQt4.QtCore import pyqtSlot, QTimer
from serial.tools.list_ports import comports
from mainui import Ui_Dialog
from pyqtgraph import PlotWidget
from stream import getValue


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


class MainUi(QWidget):
    def __init__(self):
        super(MainUi, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.RawDataF, self.BiasF, self.SFF, self.recF = 0, 0, 0, 0
        self.RawSF = self.ui.qtSGyroSF.value()
        self.BiasX, self.BiasY, self.BiasZ = 0.0, 0.0, 0.0
        self.SFX, self.SFY, self.SFZ = 1.0, 1.0, 1.0
        self.mapFunc = [self.ui.qtSBiasX,
                        self.ui.qtSBiasY,
                        self.ui.qtSBiasZ,
                        self.ui.qtSSFX,
                        self.ui.qtSSFY,
                        self.ui.qtSSFZ,
                        self.ui.qtSGyroSF]
        self.ComSelect(0, True)
        self.iStream = 0
        self.data = [[] for i in range(8)]
        self.ui.qtComPorts.currentIndexChanged.connect(self.ComSelect)
        self.ui.qtBStream.clicked.connect(self.stremingData)
        self.ui.qtBBrowse.clicked.connect(self.file_select)
        self.ui.verticalLayout_2.removeWidget(self.ui.widget)
        self.ui.widget.close()
        self.ui.plot = PlotWidget(name='gyro data', title='Gyro data')
        self.ui.plotx = self.ui.plot.plot(pen=red, name='Gyro X')
        self.ui.ploty = self.ui.plot.plot(pen=green, name='Gyro Y')
        self.ui.plotz = self.ui.plot.plot(pen=blue, name='Gyro Z')
        self.ui.verticalLayout_2.addWidget(self.ui.plot)
        self.ui.qtCRawData.clicked.connect(self.changed)
        self.ui.qtCBias.clicked.connect(self.changed)
        self.ui.qtCSF.clicked.connect(self.changed)
        self.ui.qtCRecorde.clicked.connect(self.changed)
        [x.valueChanged.connect(self.valueChane) for x in self.mapFunc]

    @pyqtSlot(float)
    def valueChane(self, val):
        s = self.sender()
        if s == self.ui.qtSBiasX:
            self.BiasX = val
        elif s == self.ui.qtSBiasY:
            self.BiasY = val
        elif s == self.ui.qtSBiasZ:
            self.BiasZ = val
        elif s == self.ui.qtSSFX:
            self.SFX = val
        elif s == self.ui.qtSSFY:
            self.SFY = val
        elif s == self.ui.qtSSFZ:
            self.SFZ = val
        elif s == self.ui.qtSGyroSF:
            self.RawSF = val

    @pyqtSlot()
    def changed(self):
        if self.ui.qtCRawData == self.sender():
            self.RawDataF = not self.RawDataF
        elif self.ui.qtCBias == self.sender():
            self.BiasF = not self.BiasF
        elif self.ui.qtCSF == self.sender():
            self.SFF = not self.SFF
        elif self.ui.qtCRecorde == self.sender():
            self.recF = not self.recF

    @pyqtSlot(int)
    def ComSelect(self, i, first_time=False):
        """Sets the selected com in qtComPorts
        i -> index value of qtComPorts
        first_time -> first calling signal isn't establish"""
        if i == 0:
            if not first_time:
                self.ui.qtComPorts.currentIndexChanged.disconnect()
            self.ui.qtComPorts.clear()
            self.comport = None
            ports = ['/dev/' + x.name
                     for x in comports() if 'AMA' not in x.name]
            self.ui.qtComPorts.addItems(['refresh'] + ports)
            self.ui.qtComPorts.insertSeparator(1)
            self.ui.qtComPorts.setCurrentIndex(-1)
            self.ui.qtComPorts.currentIndexChanged.connect(self.ComSelect)
        elif i > 0:
            self.comport = str(self.ui.qtComPorts.itemText(i))

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
        if not self.comport:
            QMessageBox.warning(self, 'No com',
                                "No com selected I can't work like this")
        else:
            if self.ui.qtBStream.text() == 'Stream':
                self.ui.qtBStream.setText('Stop')
                self.ui.qtCRecorde.setEnabled(False)
                self.streamData = getValue(self.comport)
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
                    #self.fileName = open(self.ui.qtBrowse.text(), 'w')
                    #self.fileName.write('time, accx, accy, accz, temp, gyorx, gyroy, gyroz\n')
                self.timer.start(1)
            elif self.ui.qtBStream.text() == 'Stop':
                self.ui.qtBStream.setText('Stream')
                self.ui.qtCRecorde.setEnabled(True)
                self.timer.stop()
                self.streamData.stop()
                self.data = [[] for i in range(8)]

    @pyqtSlot()
    def graphupdate(self):
        data = next(self.streamData)
        print(data)
        if data:
            if self.RawDataF:
                data[5] /= self.RawSF
                data[6] /= self.RawSF
                data[7] /= self.RawSF
            if self.SFF:
                data[5] *= self.SFX
                data[6] *= self.SFY
                data[7] *= self.SFZ
            if self.BiasF:
                data[5] += self.BiasX
                data[6] += self.BiasY
                data[7] += self.BiasZ
            if len(self.data[0]) >= 500:
                _ = [self.data[i].pop(0) for i in range(len(self.data))]
                _ = self.__x.pop(0)
                self.__x.append(self.__x[-1] + 1)
            else:
                self.__x.append(len(self.__x))
            [self.data[i].append(data[i]) for i in range(8)]
            # sdata = [str(x) for x in data]
            # self.fileName.write(','.join(sdata))
            if self.i > 7:
                self.ui.plotx.setData(x=self.__x, y=self.data[5])
                self.ui.ploty.setData(x=self.__x, y=self.data[6])
                self.ui.plotz.setData(x=self.__x, y=self.data[7])
                self.i = 0
                avgX = avg(self.data[5])
                avgY = avg(self.data[6])
                avgZ = avg(self.data[7])
                title = '{:.2} {:.2} {:.2}'.format(avgX, avgY, avgZ)
                self.ui.plot.setTitle(title)
            else:
                self.i += 1

    def closeEvent(self, event):
        if self.ui.qtBStream.text() == 'Stop':
            self.timer.stop()
            self.streamData.stop()
        super(MainUi, self).closeEvent(event)


def avg(x):
    return sum(x)*1.0/len(x)


def main():
    app = QApplication(sys.argv)
    ex = MainUi()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
