# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Phantom App.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QAction, QFileDialog, QWidget,
                             QHBoxLayout, QTableView, QPushButton)
from PyQt5.QtGui import QIcon, QPalette

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Qt5Agg')

import pandas as pd
import numpy as np

class MatplotlibFigure(QWidget):

    # constructor
    def __init__(self, parent=None):
        super().__init__()
        self.figure = matplotlib.figure.Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self)
        self.setMinimumHeight(300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy)
        self.setAutoFillBackground(True)
        p = self.palette()
        #p.setColor(self.backgroundRole(), QtGui.QColor('lightgreen'))
        self.setPalette(p)

    def setLables(self, xlable, ylable):
        self.xLable = xlable
        self.yLable = ylable
        
    def setTitle(self, title):
        self.title = title

    def plot(self, xValues, yValues):
        self.figure.clf()
        self.figure.subplots_adjust(top=0.8)
        ax = self.figure.add_subplot(111)
        ax.set_ylabel(self.yLable)
        ax.set_xlabel(self.xLable)
        ax.set_title(self.title)
        #ax.plot(xValues, yValues, color='blue', lw=3)
        ax.scatter(xValues, yValues)
        self.canvas.draw_idle()
        print('PLOTTED')



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(921, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        #self.tab = QtWidgets.QWidget()
        #self.tab.setObjectName("tab")
        #self.tabWidget.addTab(self.tab, "")
        #self.tab_2 = QtWidgets.QWidget()
        #self.tab_2.setObjectName("tab_2")
        #self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 446, 484))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphContainerLayout = QtWidgets.QVBoxLayout()
        self.graphContainerLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.graphContainerLayout.setObjectName("graphContainerLayout")
        self.gridLayout_2.addLayout(self.graphContainerLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 2, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(7, 114, 461, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.cmbConstant = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbConstant.setGeometry(QtCore.QRect(70, 80, 151, 22))
        self.cmbConstant.setObjectName("cmbConstant")
        self.cmbYAxis = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbYAxis.setGeometry(QtCore.QRect(70, 20, 151, 22))
        self.cmbYAxis.setObjectName("cmbYAxis")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 54, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 25, 47, 13))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 84, 47, 13))
        self.label_3.setObjectName("label_3")
        self.cmbXAxis = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbXAxis.setGeometry(QtCore.QRect(70, 50, 151, 22))
        self.cmbXAxis.setObjectName("cmbXAxis")
        self.btnGenerateGraph = QtWidgets.QPushButton(self.groupBox_2)
        self.btnGenerateGraph.setGeometry(QtCore.QRect(321, 109, 130, 23))
        self.btnGenerateGraph.setObjectName("btnGenerateGraph")
        self.edtRange = QtWidgets.QLineEdit(self.groupBox_2)
        self.edtRange.setGeometry(QtCore.QRect(106, 110, 115, 20))
        self.edtRange.setObjectName("edtRange")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(19, 112, 91, 16))
        self.label_6.setObjectName("label_6")
        self.lblYRange = QtWidgets.QLabel(self.groupBox_2)
        self.lblYRange.setGeometry(QtCore.QRect(230, 24, 120, 15))
        self.lblYRange.setText("")
        self.lblYRange.setObjectName("lblYRange")
        self.lblXRange = QtWidgets.QLabel(self.groupBox_2)
        self.lblXRange.setGeometry(QtCore.QRect(230, 54, 120, 15))
        self.lblXRange.setText("")
        self.lblXRange.setObjectName("lblXRange")
        self.lblCRange = QtWidgets.QLabel(self.groupBox_2)
        self.lblCRange.setGeometry(QtCore.QRect(230, 84, 120, 15))
        self.lblCRange.setText("")
        self.lblCRange.setObjectName("lblCRange")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(26, 20, 421, 81))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.btnRefresh = QtWidgets.QPushButton(self.groupBox_3)
        self.btnRefresh.setGeometry(QtCore.QRect(279, 33, 115, 23))
        self.btnRefresh.setObjectName("btnRefresh")
        self.edtSkipCol = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtSkipCol.setGeometry(QtCore.QRect(150, 35, 115, 20))
        self.edtSkipCol.setObjectName("edtSkipCol")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(21, 20, 47, 13))
        self.label_4.setObjectName("label_4")
        self.edtSkipRow = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtSkipRow.setGeometry(QtCore.QRect(20, 35, 115, 20))
        self.edtSkipRow.setObjectName("edtSkipRow")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(151, 20, 47, 13))
        self.label_5.setObjectName("label_5")
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 921, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/Microsoft Access-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/image/Microsoft Excel-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        #self.toolBar.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        #connect click events
        self.btnGenerateGraph.clicked.connect(self.onPlotGraphClicked)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.groupBox.setTitle(_translate("MainWindow", "Settings"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Graph Variables"))
        self.label_2.setText(_translate("MainWindow", "X Axis"))
        self.label.setText(_translate("MainWindow", "Y Axis"))
        self.label_3.setText(_translate("MainWindow", "Constant"))
        self.btnGenerateGraph.setText(_translate("MainWindow", "Generate Graph"))
        self.edtRange.setText(_translate("MainWindow", "5"))
        self.label_6.setText(_translate("MainWindow", "Constant Range"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Skip excel rows && columns"))
        self.btnRefresh.setText(_translate("MainWindow", "Refresh"))
        self.edtSkipCol.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Rows"))
        self.edtSkipRow.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Columns"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setIconText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open Xls file"))
        self.actionOpen.triggered.connect(self.showFileOpenDialog)
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.triggered.connect(QtWidgets.QApplication.quit)
        self.cmbConstant.currentTextChanged.connect(self.onComboBoxCChanged)
        self.cmbYAxis.currentTextChanged.connect(self.onComboBoxYChanged)
        self.cmbXAxis.currentTextChanged.connect(self.onComboBoxXChanged)

    def showFileOpenDialog(self):
        #_translate = QtCore.QCoreApplication.translate
        fname = QFileDialog.getOpenFileName(MainWindow, 'Open file', '')
        if fname[0]:
            print("Selected file name %s", fname[0])
            self.xlParser = XlsParser()
            self.xlParser.parseFile(fname[0])
            #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", self.xlParser.getSheetName()))
            tab = self.createTabSheet(self.xlParser.getSheetName(),
                                      self.xlParser.getRowsCount(),
                                      self.xlParser.getColsCount())
            self.tabWidget.addTab(tab, self.xlParser.getSheetName())
            columns = self.xlParser.getColumns()
            self.cmbXAxis.addItems(columns)
            self.cmbYAxis.addItems(columns)
            self.cmbConstant.addItems(columns)
 
    def createTabSheet(self, name, row, col):
        tab1 = QWidget()
        tableWidget = QTableView()
        model = PandasModel(self.xlParser.getDataFrame())
        tableWidget.setStyleSheet("QHeaderView::section { background-color:green }")
        tableWidget.setCornerButtonEnabled(True)
        tableWidget.setModel(model)
        #tab1.setTabText(name)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)
        return tab1
        #self.tabWidget.addTab(tab1, name)
               
    def onComboBoxXChanged(self, value):
        min_val, max_val = self.xlParser.getMinMaxColumnData(value)
        #print("Combo name:",self.getObjectName())
        print("Selected col min-max:",min_val, ":",max_val)
        self.lblXRange.setText(str(min_val)+" ~ "+str(max_val))
    def onComboBoxYChanged(self, value):
        min_val, max_val = self.xlParser.getMinMaxColumnData(value)
        #print("Combo name:",self.getObjectName())
        print("Selected col min-max:",min_val, ":",max_val)
        self.lblYRange.setText(str(min_val)+" ~ "+str(max_val))
    def onComboBoxCChanged(self, value):
        min_val, max_val = self.xlParser.getMinMaxColumnData(value)
        #print("Combo name:",self.getObjectName())
        print("Selected col min-max:",min_val, ":",max_val)
        self.lblCRange.setText(str(min_val)+" ~ "+str(max_val))
        
    def onPlotGraphClicked(self, checked):
        print ("PlotGraph clicked")
        self.plotGraph()
        
    def plotGraph(self):
        xaxis = self.cmbXAxis.currentText()
        yaxis = self.cmbYAxis.currentText()
        constant = self.cmbConstant.currentText()
        dataFrame = self.xlParser.getDataFrame()
        df = dataFrame[[xaxis,yaxis,constant]].copy()
        df.dropna(inplace=True)
        df_constant = df.round({constant:0})
        print(df_constant[constant])
        min_val = min(df[constant].values)
        max_val = max(df[constant].values)
        step_val = self.edtRange.text()
        dfgrp = df.groupby(pd.cut(df[constant],
                                  np.arange(int(min_val), int(max_val), int(step_val))))
        #print("********<<<>>>***********")
        #print("Type:",type(dfgrp))
        #print(dfgrp)
        #print(dfgrp.first())
        print("Group Count:", dfgrp.ngroups)
        print("Groups Type:", type(dfgrp.groups))
        for name, df_group in dfgrp:
            print ("Name: ",name, end = " ")
            print ("Type: ",type(df_group))
            sc = MatplotlibFigure(self.scrollAreaWidgetContents)
            sc.setTitle("Constant: "+constant+" Interval: "+str(name))
            sc.setLables(xaxis, yaxis)
            self.graphContainerLayout.addWidget(sc)
            sc.plot(df_group[xaxis].values,df_group[yaxis].values)
            sc.show()        


class XlsParser:
    def __init__(self):
        print("constructor called")
        
        
    def parseFile(self, path):
        self.path = path
        print("parsing file:",self.path)
        self.file = pd.ExcelFile(self.path)
        self.sheets = self.file.sheet_names
        print("Sheets:",self.sheets)
        self.dataFrame = self.file.parse(self.sheets[0])
        #print(self.dataFrame)
        row, col = self.dataFrame.shape
        print("Row:",row,"Column:",col)
        self.rows = row
        self.cols = col
        print(self.dataFrame.columns)
    
    def getSheetName(self):
        return self.sheets[0]
    
    def getDataFrame(self):
        return self.dataFrame
    def getRowsCount(self):
        return self.rows
    def getColsCount(self):
        return self.cols
    def getColumns(self):
        return self.dataFrame.columns
    def getColumbData(self, colName):
        return self.dataFrame[colName].values
    def getMinMaxColumnData(self, colName):
        min_val = min(self.dataFrame[colName].values)
        max_val = max(self.dataFrame[colName].values)
        return min_val, max_val

class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None
      

#import sample_resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

