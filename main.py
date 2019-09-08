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
        self.RawDataF, self.BiasF, self.SFF = 0, 0, 0
        self.RawSF, self.RawBias = 0, 0
        self.BiasX, self.BiasY, self.BiasZ = 0, 0, 0
        self.SFX, self.SFY, self.SFZ = 0, 0, 0
        self.mapFunc = {self.ui.qtSBiasX: self.BiasX,
                        self.ui.qtSBiasY: self.BiasY,
                        self.ui.qtSBiasZ: self.BiasZ,
                        self.ui.qtSSFX: self.SFX,
                        self.ui.qtSSFY: self.SFY,
                        self.ui.qtSSFZ: self.SFZ,
                        self.ui.qtSGyroBias: self.RawBias,
                        self.ui.qtSGyroSF: self.RawSF}
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
        [x.valueChanged.connect(self.valueChane) for x in self.mapFunc.keys()]

    @pyqtSlot(float)
    def valueChane(self, val):
        self.mapFunc[self.sender()] = val
        print([x for x in self.mapFunc.values()])

    @pyqtSlot()
    def changed(self):
        if self.ui.qtCRawData == self.sender():
            self.RawDataF = not self.RawDataF
            print(self.RawDataF)
        elif self.ui.qtCBias == self.sender():
            self.BiasF = not self.BiasF
            print(self.BiasF)
        elif self.ui.qtCSF == self.sender():
            self.SFF = not self.SFF
            print(self.SFF)

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
                self.timer.start()
                self.i = 0
                self.__x = []
            elif self.ui.qtBStream.text() == 'Stop':
                self.ui.qtBStream.setText('Stream')
                self.ui.qtCRecorde.setEnabled(True)
                self.timer.stop()
                self.streamData.stop()
                self.data = [[] for i in range(8)]

    @pyqtSlot()
    def graphupdate(self):
        data = next(self.streamData)
        if data:
            if len(self.data[0]) >= 2000:
                _ = [self.data[i].pop(0) for i in range(len(self.data))]
                _ = self.__x.pop(0)
                self.__x.append(self.__x[-1] + 1)
            else:
                self.__x.append(len(self.__x))
            if self.RawDataF:
                pass
            if self.BiasF:
                pass
            if self.SFF:
                pass
            [self.data[i].append(data[i]) for i in range(8)]
            if self.i > 15:
                self.ui.plotx.setData(x=self.__x, y=self.data[5])
                self.ui.ploty.setData(x=self.__x, y=self.data[6])
                self.ui.plotz.setData(x=self.__x, y=self.data[7])
                self.i = 0
            else:
                self.i += 1


def main():
    app = QApplication(sys.argv)
    ex = MainUi()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
