# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindo.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(571, 550)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(174, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 2, 1, 1)
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout_4.addWidget(self.line_7, 0, 3, 8, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.qtComPortsLabel = QtGui.QLabel(self.centralwidget)
        self.qtComPortsLabel.setObjectName(_fromUtf8("qtComPortsLabel"))
        self.verticalLayout_5.addWidget(self.qtComPortsLabel)
        self.qtComPorts = QtGui.QComboBox(self.centralwidget)
        self.qtComPorts.setMinimumSize(QtCore.QSize(150, 0))
        self.qtComPorts.setObjectName(_fromUtf8("qtComPorts"))
        self.verticalLayout_5.addWidget(self.qtComPorts)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 4, 2, 1)
        self.qtCRawData = QtGui.QCheckBox(self.centralwidget)
        self.qtCRawData.setEnabled(True)
        self.qtCRawData.setText(_fromUtf8(""))
        self.qtCRawData.setObjectName(_fromUtf8("qtCRawData"))
        self.gridLayout_4.addWidget(self.qtCRawData, 1, 0, 1, 1)
        self.qtSGyroSF = QtGui.QDoubleSpinBox(self.centralwidget)
        self.qtSGyroSF.setEnabled(False)
        self.qtSGyroSF.setDecimals(4)
        self.qtSGyroSF.setMinimum(0.0001)
        self.qtSGyroSF.setSingleStep(0.1)
        self.qtSGyroSF.setProperty("value", 1.0)
        self.qtSGyroSF.setObjectName(_fromUtf8("qtSGyroSF"))
        self.gridLayout_4.addWidget(self.qtSGyroSF, 1, 1, 1, 1)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_4.addWidget(self.line_5, 2, 0, 1, 3)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_6.addWidget(self.label_13)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.qtRateX = QtGui.QLCDNumber(self.centralwidget)
        self.qtRateX.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
""))
        self.qtRateX.setSmallDecimalPoint(True)
        self.qtRateX.setProperty("value", 0.0)
        self.qtRateX.setObjectName(_fromUtf8("qtRateX"))
        self.horizontalLayout_6.addWidget(self.qtRateX)
        self.qtRateY = QtGui.QLCDNumber(self.centralwidget)
        self.qtRateY.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
""))
        self.qtRateY.setSmallDecimalPoint(True)
        self.qtRateY.setProperty("value", 0.0)
        self.qtRateY.setObjectName(_fromUtf8("qtRateY"))
        self.horizontalLayout_6.addWidget(self.qtRateY)
        self.qtRateZ = QtGui.QLCDNumber(self.centralwidget)
        self.qtRateZ.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
""))
        self.qtRateZ.setSmallDecimalPoint(True)
        self.qtRateZ.setProperty("value", 0.0)
        self.qtRateZ.setObjectName(_fromUtf8("qtRateZ"))
        self.horizontalLayout_6.addWidget(self.qtRateZ)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_6.addWidget(self.line_6)
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_6.addWidget(self.label_14)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.qtLOSX = QtGui.QLCDNumber(self.centralwidget)
        self.qtLOSX.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
""))
        self.qtLOSX.setSmallDecimalPoint(True)
        self.qtLOSX.setProperty("value", 0.0)
        self.qtLOSX.setObjectName(_fromUtf8("qtLOSX"))
        self.horizontalLayout_7.addWidget(self.qtLOSX)
        self.qtLOSY = QtGui.QLCDNumber(self.centralwidget)
        self.qtLOSY.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
""))
        self.qtLOSY.setSmallDecimalPoint(True)
        self.qtLOSY.setProperty("value", 0.0)
        self.qtLOSY.setObjectName(_fromUtf8("qtLOSY"))
        self.horizontalLayout_7.addWidget(self.qtLOSY)
        self.qtLOSZ = QtGui.QLCDNumber(self.centralwidget)
        self.qtLOSZ.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
""))
        self.qtLOSZ.setSmallDecimalPoint(True)
        self.qtLOSZ.setProperty("value", 0.0)
        self.qtLOSZ.setObjectName(_fromUtf8("qtLOSZ"))
        self.horizontalLayout_7.addWidget(self.qtLOSZ)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_6.addWidget(self.line_2)
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_6.addWidget(self.label_15)
        self.qtCRate = QtGui.QCheckBox(self.centralwidget)
        self.qtCRate.setObjectName(_fromUtf8("qtCRate"))
        self.verticalLayout_6.addWidget(self.qtCRate)
        self.qtCLOS = QtGui.QCheckBox(self.centralwidget)
        self.qtCLOS.setObjectName(_fromUtf8("qtCLOS"))
        self.verticalLayout_6.addWidget(self.qtCLOS)
        self.qtCCube = QtGui.QCheckBox(self.centralwidget)
        self.qtCCube.setObjectName(_fromUtf8("qtCCube"))
        self.verticalLayout_6.addWidget(self.qtCCube)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 2, 4, 6, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.qtSBiasY = QtGui.QDoubleSpinBox(self.centralwidget)
        self.qtSBiasY.setEnabled(False)
        self.qtSBiasY.setDecimals(4)
        self.qtSBiasY.setMinimum(-99.99)
        self.qtSBiasY.setSingleStep(0.001)
        self.qtSBiasY.setObjectName(_fromUtf8("qtSBiasY"))
        self.gridLayout.addWidget(self.qtSBiasY, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.qtCBias = QtGui.QCheckBox(self.centralwidget)
        self.qtCBias.setText(_fromUtf8(""))
        self.qtCBias.setObjectName(_fromUtf8("qtCBias"))
        self.gridLayout.addWidget(self.qtCBias, 1, 0, 1, 1)
        self.qtSBiasZ = QtGui.QDoubleSpinBox(self.centralwidget)
        self.qtSBiasZ.setEnabled(False)
        self.qtSBiasZ.setDecimals(4)
        self.qtSBiasZ.setMinimum(-99.99)
        self.qtSBiasZ.setSingleStep(0.001)
        self.qtSBiasZ.setObjectName(_fromUtf8("qtSBiasZ"))
        self.gridLayout.addWidget(self.qtSBiasZ, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.qtSBiasX = QtGui.QDoubleSpinBox(self.centralwidget)
        self.qtSBiasX.setEnabled(False)
        self.qtSBiasX.setDecimals(4)
        self.qtSBiasX.setMinimum(-99.99)
        self.qtSBiasX.setSingleStep(0.001)
        self.qtSBiasX.setObjectName(_fromUtf8("qtSBiasX"))
        self.gridLayout.addWidget(self.qtSBiasX, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 3, 0, 1, 3)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_4.addWidget(self.line_4, 4, 0, 1, 3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_3.addWidget(self.label_10)
        self.qtCAlign = QtGui.QCheckBox(self.centralwidget)
        self.qtCAlign.setText(_fromUtf8(""))
        self.qtCAlign.setObjectName(_fromUtf8("qtCAlign"))
        self.verticalLayout_3.addWidget(self.qtCAlign)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.qtAlignMat = QtGui.QTableWidget(self.centralwidget)
        self.qtAlignMat.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qtAlignMat.sizePolicy().hasHeightForWidth())
        self.qtAlignMat.setSizePolicy(sizePolicy)
        self.qtAlignMat.setMinimumSize(QtCore.QSize(302, 92))
        self.qtAlignMat.setMaximumSize(QtCore.QSize(302, 92))
        self.qtAlignMat.setAutoScroll(False)
        self.qtAlignMat.setWordWrap(False)
        self.qtAlignMat.setCornerButtonEnabled(False)
        self.qtAlignMat.setRowCount(3)
        self.qtAlignMat.setColumnCount(3)
        self.qtAlignMat.setObjectName(_fromUtf8("qtAlignMat"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtAlignMat.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtAlignMat.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtAlignMat.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtAlignMat.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtAlignMat.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtAlignMat.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtAlignMat.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtAlignMat.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtAlignMat.setItem(2, 2, item)
        self.qtAlignMat.horizontalHeader().setVisible(False)
        self.qtAlignMat.verticalHeader().setVisible(False)
        self.horizontalLayout_3.addWidget(self.qtAlignMat)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 5, 0, 1, 3)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_4.addWidget(self.line_3, 6, 0, 1, 3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_4.addWidget(self.label_11)
        self.qtCScale = QtGui.QCheckBox(self.centralwidget)
        self.qtCScale.setText(_fromUtf8(""))
        self.qtCScale.setObjectName(_fromUtf8("qtCScale"))
        self.verticalLayout_4.addWidget(self.qtCScale)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.qtScaleMat = QtGui.QTableWidget(self.centralwidget)
        self.qtScaleMat.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qtScaleMat.sizePolicy().hasHeightForWidth())
        self.qtScaleMat.setSizePolicy(sizePolicy)
        self.qtScaleMat.setMinimumSize(QtCore.QSize(302, 92))
        self.qtScaleMat.setMaximumSize(QtCore.QSize(302, 92))
        self.qtScaleMat.setAutoScroll(False)
        self.qtScaleMat.setWordWrap(False)
        self.qtScaleMat.setCornerButtonEnabled(False)
        self.qtScaleMat.setRowCount(3)
        self.qtScaleMat.setColumnCount(3)
        self.qtScaleMat.setObjectName(_fromUtf8("qtScaleMat"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtScaleMat.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtScaleMat.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtScaleMat.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtScaleMat.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtScaleMat.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtScaleMat.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtScaleMat.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtScaleMat.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.qtScaleMat.setItem(2, 2, item)
        self.qtScaleMat.horizontalHeader().setVisible(False)
        self.qtScaleMat.verticalHeader().setVisible(False)
        self.horizontalLayout_4.addWidget(self.qtScaleMat)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 7, 0, 1, 3)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_4.addWidget(self.line, 8, 0, 1, 5)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.qtBBrowse = QtGui.QPushButton(self.centralwidget)
        self.qtBBrowse.setObjectName(_fromUtf8("qtBBrowse"))
        self.gridLayout_3.addWidget(self.qtBBrowse, 1, 1, 1, 1)
        self.qtBrowse = QtGui.QLineEdit(self.centralwidget)
        self.qtBrowse.setObjectName(_fromUtf8("qtBrowse"))
        self.gridLayout_3.addWidget(self.qtBrowse, 1, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.qtCRecorde = QtGui.QCheckBox(self.centralwidget)
        self.qtCRecorde.setObjectName(_fromUtf8("qtCRecorde"))
        self.gridLayout_3.addWidget(self.qtCRecorde, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 9, 0, 1, 5)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.qtBExit = QtGui.QPushButton(self.centralwidget)
        self.qtBExit.setObjectName(_fromUtf8("qtBExit"))
        self.horizontalLayout_5.addWidget(self.qtBExit)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.qtBStream = QtGui.QPushButton(self.centralwidget)
        self.qtBStream.setObjectName(_fromUtf8("qtBStream"))
        self.horizontalLayout_5.addWidget(self.qtBStream)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 10, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.qMain = QtGui.QMenu(self.menubar)
        self.qMain.setObjectName(_fromUtf8("qMain"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.qMain.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.qMain.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.label.setBuddy(self.qtSGyroSF)
        self.qtComPortsLabel.setBuddy(self.qtComPorts)
        self.label_2.setBuddy(self.qtCBias)
        self.label_4.setBuddy(self.qtSBiasY)
        self.label_3.setBuddy(self.qtSBiasX)
        self.label_5.setBuddy(self.qtSBiasZ)
        self.label_10.setBuddy(self.qtCAlign)
        self.label_11.setBuddy(self.qtCScale)
        self.label_12.setBuddy(self.qtBrowse)

        self.retranslateUi(MainWindow)
        self.qtComPorts.setCurrentIndex(-1)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.qtCRawData, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.qtSGyroSF.setEnabled)
        QtCore.QObject.connect(self.qtCBias, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.qtSBiasX.setEnabled)
        QtCore.QObject.connect(self.qtCBias, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.qtSBiasY.setEnabled)
        QtCore.QObject.connect(self.qtCBias, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.qtSBiasZ.setEnabled)
        QtCore.QObject.connect(self.qtCAlign, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.qtAlignMat.setEnabled)
        QtCore.QObject.connect(self.qtCScale, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.qtScaleMat.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.qtCRawData, self.qtSGyroSF)
        MainWindow.setTabOrder(self.qtSGyroSF, self.qtCBias)
        MainWindow.setTabOrder(self.qtCBias, self.qtSBiasX)
        MainWindow.setTabOrder(self.qtSBiasX, self.qtSBiasY)
        MainWindow.setTabOrder(self.qtSBiasY, self.qtSBiasZ)
        MainWindow.setTabOrder(self.qtSBiasZ, MainWindow.qtCBias_2)
        MainWindow.setTabOrder(MainWindow.qtCBias_2, MainWindow.qtSBiasZ_2)
        MainWindow.setTabOrder(MainWindow.qtSBiasZ_2, MainWindow.qtSBiasY_2)
        MainWindow.setTabOrder(MainWindow.qtSBiasY_2, MainWindow.qtSBiasX_2)
        MainWindow.setTabOrder(MainWindow.qtSBiasX_2, self.qtSBiasY)
        MainWindow.setTabOrder(self.qtSBiasY, self.qtCBias)
        MainWindow.setTabOrder(self.qtCBias, self.qtSBiasZ)
        MainWindow.setTabOrder(self.qtSBiasZ, self.qtSBiasX)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Manufacturer calibration", None))
        self.qtComPortsLabel.setText(_translate("MainWindow", "Com", None))
        self.label_13.setText(_translate("MainWindow", "Rate Out", None))
        self.label_14.setText(_translate("MainWindow", "LOS Out", None))
        self.label_15.setText(_translate("MainWindow", "Display", None))
        self.qtCRate.setText(_translate("MainWindow", "Rate", None))
        self.qtCLOS.setText(_translate("MainWindow", "LOS", None))
        self.qtCCube.setText(_translate("MainWindow", "Cube", None))
        self.label_2.setText(_translate("MainWindow", "Bias", None))
        self.label_4.setText(_translate("MainWindow", "Y", None))
        self.label_3.setText(_translate("MainWindow", "X", None))
        self.label_5.setText(_translate("MainWindow", "Z", None))
        self.label_10.setText(_translate("MainWindow", "Align", None))
        __sortingEnabled = self.qtAlignMat.isSortingEnabled()
        self.qtAlignMat.setSortingEnabled(False)
        item = self.qtAlignMat.item(0, 0)
        item.setText(_translate("MainWindow", "1.0000", None))
        item = self.qtAlignMat.item(0, 1)
        item.setText(_translate("MainWindow", "0.0000", None))
        item = self.qtAlignMat.item(0, 2)
        item.setText(_translate("MainWindow", "0.0000", None))
        item = self.qtAlignMat.item(1, 0)
        item.setText(_translate("MainWindow", "0.0000", None))
        item = self.qtAlignMat.item(1, 1)
        item.setText(_translate("MainWindow", "1.0000", None))
        item = self.qtAlignMat.item(1, 2)
        item.setText(_translate("MainWindow", "0.0000", None))
        item = self.qtAlignMat.item(2, 0)
        item.setText(_translate("MainWindow", "0.0000", None))
        item = self.qtAlignMat.item(2, 1)
        item.setText(_translate("MainWindow", "0.0000", None))
        item = self.qtAlignMat.item(2, 2)
        item.setText(_translate("MainWindow", "1.0000", None))
        self.qtAlignMat.setSortingEnabled(__sortingEnabled)
        self.label_11.setText(_translate("MainWindow", "Scale", None))
        __sortingEnabled = self.qtScaleMat.isSortingEnabled()
        self.qtScaleMat.setSortingEnabled(False)
        item = self.qtScaleMat.item(0, 0)
        item.setText(_translate("MainWindow", "1.0000", None))
        item = self.qtScaleMat.item(0, 1)
        item.setText(_translate("MainWindow", "0.0000", None))
        item = self.qtScaleMat.item(0, 2)
        item.setText(_translate("MainWindow", "0.0000", None))
        item = self.qtScaleMat.item(1, 0)
        item.setText(_translate("MainWindow", "0.0000", None))
        item = self.qtScaleMat.item(1, 1)
        item.setText(_translate("MainWindow", "1.0000", None))
        item = self.qtScaleMat.item(1, 2)
        item.setText(_translate("MainWindow", "0.0000", None))
        item = self.qtScaleMat.item(2, 0)
        item.setText(_translate("MainWindow", "0.0000", None))
        item = self.qtScaleMat.item(2, 1)
        item.setText(_translate("MainWindow", "0.0000", None))
        item = self.qtScaleMat.item(2, 2)
        item.setText(_translate("MainWindow", "1.0000", None))
        self.qtScaleMat.setSortingEnabled(__sortingEnabled)
        self.qtBBrowse.setText(_translate("MainWindow", "...", None))
        self.label_12.setText(_translate("MainWindow", "File location", None))
        self.qtCRecorde.setText(_translate("MainWindow", "Recorde", None))
        self.qtBExit.setText(_translate("MainWindow", "Exit", None))
        self.qtBStream.setText(_translate("MainWindow", "Stream", None))
        self.qMain.setTitle(_translate("MainWindow", "Main", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
