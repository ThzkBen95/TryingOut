# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GraphProcessing.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication, QSizePolicy, QTextBrowser

import pandas as pd

import matplotlib.pyplot as plt
import mplcursors

import ParetoWindow

from io import StringIO
import time

from tabulate import tabulate


fname = ""              # CSV Filepath to pass between functions
ldf = ""                # CSV to dataframe
header_track = False    # Used to track whether first row of loaded dataframe has headers


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 675)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Loadedfilename = QtWidgets.QLabel(self.centralwidget)
        self.Loadedfilename.setObjectName("Loadedfilename")
        self.horizontalLayout_2.addWidget(self.Loadedfilename)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.CSVDir = QtWidgets.QLineEdit(self.tab)
        self.CSVDir.setObjectName("CSVDir")
        self.horizontalLayout.addWidget(self.CSVDir)
        self.BrowseCSVBtn = QtWidgets.QPushButton(self.tab)
        self.BrowseCSVBtn.setObjectName("BrowseCSVBtn")
        self.horizontalLayout.addWidget(self.BrowseCSVBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 4, 1, 1, 1)
        self.HeaderCheckbox = QtWidgets.QCheckBox(self.tab)
        self.HeaderCheckbox.setAutoFillBackground(False)
        self.HeaderCheckbox.setChecked(True)
        self.HeaderCheckbox.setObjectName("HeaderCheckbox")
        self.gridLayout.addWidget(self.HeaderCheckbox, 7, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 1, 1, 1)
        self.LoadCSVBtn = QtWidgets.QPushButton(self.tab)
        self.LoadCSVBtn.setObjectName("LoadCSVBtn")
        self.gridLayout.addWidget(self.LoadCSVBtn, 6, 1, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_4.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.gridLayout.addWidget(self.textBrowser_4, 5, 1, 1, 1)
        self.CSVPreview = QtWidgets.QTextEdit(self.tab)
        self.CSVPreview.setReadOnly(True)
        self.CSVPreview.setObjectName("CSVPreview")
        self.CSVPreview.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.gridLayout.addWidget(self.CSVPreview, 1, 0, 7, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.XaxisCombo = QtWidgets.QComboBox(self.tab_2)
        self.XaxisCombo.setObjectName("XaxisCombo")
        self.horizontalLayout_3.addWidget(self.XaxisCombo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.YaxisCombo = QtWidgets.QComboBox(self.tab_2)
        self.YaxisCombo.setObjectName("YaxisCombo")
        self.horizontalLayout_4.addWidget(self.YaxisCombo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.ZaxisCombo = QtWidgets.QComboBox(self.tab_2)
        self.ZaxisCombo.setObjectName("ZaxisCombo")
        self.horizontalLayout_5.addWidget(self.ZaxisCombo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_16.addWidget(self.label_17)
        self.GraphCombo = QtWidgets.QComboBox(self.tab_2)
        self.GraphCombo.setObjectName("GraphCombo")
        self.horizontalLayout_16.addWidget(self.GraphCombo)
        self.verticalLayout_6.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.colormapin = QtWidgets.QLineEdit(self.tab_2)
        self.colormapin.setObjectName("colormapin")
        self.horizontalLayout_12.addWidget(self.colormapin)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_17.addWidget(self.label_18)
        self.coloraxisCombo = QtWidgets.QComboBox(self.tab_2)
        self.coloraxisCombo.setObjectName("coloraxisCombo")
        self.horizontalLayout_17.addWidget(self.coloraxisCombo)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 1, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lineEdit_xlim = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_xlim.setObjectName("lineEdit_xlim")
        self.horizontalLayout_7.addWidget(self.lineEdit_xlim)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.lineEdit_ylim = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_ylim.setObjectName("lineEdit_ylim")
        self.horizontalLayout_8.addWidget(self.lineEdit_ylim)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.lineEdit_zlim = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_zlim.setObjectName("lineEdit_zlim")
        self.horizontalLayout_6.addWidget(self.lineEdit_zlim)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_Graph = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Graph.setObjectName("pushButton_Graph")
        self.horizontalLayout_9.addWidget(self.pushButton_Graph)
        self.pushButton_Pareto = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Pareto.setObjectName("pushButton_Pareto")
        self.horizontalLayout_9.addWidget(self.pushButton_Pareto)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.layoutWidget = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget.setGeometry(QtCore.QRect(11, -1, 851, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_13.addWidget(self.label_3)
        self.lineEdit_CSVDir_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_CSVDir_2.setObjectName("lineEdit_CSVDir_2")
        self.horizontalLayout_13.addWidget(self.lineEdit_CSVDir_2)
        self.BrowseCSVBtn_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.BrowseCSVBtn_2.setObjectName("BrowseCSVBtn_2")
        self.horizontalLayout_13.addWidget(self.BrowseCSVBtn_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_18.addWidget(self.label_14)
        self.lineEdit_MarginDir = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_MarginDir.setObjectName("lineEdit_MarginDir")
        self.horizontalLayout_18.addWidget(self.lineEdit_MarginDir)
        self.BrowseCSVBtn_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.BrowseCSVBtn_3.setObjectName("BrowseCSVBtn_3")
        self.horizontalLayout_18.addWidget(self.BrowseCSVBtn_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_18)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_19.addWidget(self.label_25)
        self.XaxisCombo_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.XaxisCombo_2.setObjectName("XaxisCombo_2")
        self.horizontalLayout_19.addWidget(self.XaxisCombo_2)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_19.addWidget(self.label_21)
        self.lineEdit_xshift = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_xshift.setText("")
        self.lineEdit_xshift.setObjectName("lineEdit_xshift")
        self.horizontalLayout_19.addWidget(self.lineEdit_xshift)
        self.verticalLayout_7.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_20.addWidget(self.label_26)
        self.YaxisCombo_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.YaxisCombo_2.setObjectName("YaxisCombo_2")
        self.horizontalLayout_20.addWidget(self.YaxisCombo_2)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_20.addWidget(self.label_20)
        self.lineEdit_yshift = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_yshift.setObjectName("lineEdit_yshift")
        self.horizontalLayout_20.addWidget(self.lineEdit_yshift)
        self.verticalLayout_7.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_21.addWidget(self.label_27)
        self.ZaxisCombo_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.ZaxisCombo_2.setObjectName("ZaxisCombo_2")
        self.horizontalLayout_21.addWidget(self.ZaxisCombo_2)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_21.addWidget(self.label_19)
        self.lineEdit_zshift = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_zshift.setObjectName("lineEdit_zshift")
        self.horizontalLayout_21.addWidget(self.lineEdit_zshift)
        self.verticalLayout_7.addLayout(self.horizontalLayout_21)
        self.verticalLayout_10.addLayout(self.verticalLayout_7)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_9.addWidget(self.label_22)
        self.GraphMarginIn = QtWidgets.QTextBrowser(self.layoutWidget)
        self.GraphMarginIn.setObjectName("GraphMarginIn")
        self.verticalLayout_9.addWidget(self.GraphMarginIn)
        self.pushButton_loadmargin = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_loadmargin.setObjectName("pushButton_loadmargin")
        self.verticalLayout_9.addWidget(self.pushButton_loadmargin)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.gridLayout_6.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_refreshmargin = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_refreshmargin.setObjectName("pushButton_refreshmargin")
        self.gridLayout_5.addWidget(self.pushButton_refreshmargin, 2, 0, 1, 1)
        self.pushButton_savemargin = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_savemargin.setObjectName("pushButton_savemargin")
        self.gridLayout_5.addWidget(self.pushButton_savemargin, 2, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 0, 0, 1, 1)
        self.GraphMarginOut = QtWidgets.QTextBrowser(self.layoutWidget)
        self.GraphMarginOut.setObjectName("GraphMarginOut")
        self.gridLayout_5.addWidget(self.GraphMarginOut, 1, 0, 1, 2)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 906, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)       
        
        ls1 = ["2D Plot", "3D Plot"]
        self.GraphCombo.addItems(ls1)
        
        ######################## Function Connections #########################
        self.BrowseCSVBtn.clicked.connect(self.PreviewCSV)
        self.LoadCSVBtn.clicked.connect(self.LoadCSV)
        self.pushButton_Graph.clicked.connect(self.GenerateWindowGraph)
        self.pushButton_Pareto.clicked.connect(self.OpenParetoWindow)
        self.BrowseCSVBtn_2.clicked.connect(self.BrowseMarginFile)
        self.BrowseCSVBtn_3.clicked.connect(self.BrowseSaveDir)
        self.pushButton_loadmargin.clicked.connect(self.LoadMarginFile)
        self.pushButton_refreshmargin.clicked.connect(self.RefreshPreview)
        self.pushButton_savemargin.clicked.connect(self.SaveMargin)
         
         
        #######################################################################
         
    ########################## Function Definitions #############################
    
    
    def PreviewCSV(self):
        global fname
        global header_track
        
        csvfilter = "csv(*.csv)"
        filename = QFileDialog.getOpenFileName(filter = csvfilter)
        self.CSVDir.setText(filename[0])
        
         # Use Tabulate to get the fancy table format
        if self.HeaderCheckbox.isChecked() == True:
             df = pd.read_csv(filename[0])
             self.CSVPreview.setText(tabulate(df.values, headers = df.columns.values.tolist(), tablefmt="github"))
             header_track = True
        else:
             df = pd.read_csv(filename[0], header = None)
             self.CSVPreview.setText(tabulate(df.values, headers = df.columns.values.tolist(), tablefmt="github"))
             header_track = False
        
        buffer = StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        self.textBrowser_4.setText(s)
        fname = filename[0]
        
    def LoadCSV(self):
        global fname
        global ldf
        global header_track
        self.Loadedfilename.setText(fname)
        
        # Add CSV headers to graph axis options 
        
        if header_track == True:
            ldf = pd.read_csv(fname)
            ls =  ldf.columns.values.tolist()
            
            # Reload options for axis combo box
            self.XaxisCombo.clear()
            self.XaxisCombo.addItems(ls)
        
            self.YaxisCombo.clear()
            self.YaxisCombo.addItems(ls)
        
            self.ZaxisCombo.clear()
            self.ZaxisCombo.addItem("None")
            self.ZaxisCombo.addItems(ls)
            
            self.coloraxisCombo.clear()
            self.coloraxisCombo.addItem("None")
            self.coloraxisCombo.addItems(ls)
                  
       
        elif header_track == False:
            ldf = pd.read_csv(fname, header = None)
            
            ls =  ldf.columns.values.tolist()
            ls = [str(i) for i in ls]
            
            # Reload options for axis combo box
            self.XaxisCombo.clear()
            self.XaxisCombo.addItems(ls)
        
            self.YaxisCombo.clear()
            self.YaxisCombo.addItems(ls)
        
            self.ZaxisCombo.clear()
            self.ZaxisCombo.addItems(ls)
            
            self.coloraxisCombo.clear()
            self.coloraxisCombo.addItem("None")
            self.coloraxisCombo.addItems(ls)
    
    def GenerateWindowGraph(self):
        dfx = ldf[str(ui.XaxisCombo.currentText())].to_list()
        dfy = ldf[str(ui.YaxisCombo.currentText())].to_list()
        
        dfc = []
        
        lol = ldf.values.tolist()
        
        
        if ui.GraphCombo.currentText() == "2D Plot":   # 2D Scatter Plot
        
            fig, ax = plt.subplots()
            ax.set_title(str(list(ldf.columns)))
            
            if ui.coloraxisCombo.currentText() == "None":
                plt.scatter(dfx, dfy, color= "green",  marker= "o", s=30)   # w/o color axis
               
            else:                                                           # w/ color axis
                dfc = ldf[str(self.coloraxisCombo.currentText())].to_list()
                plt.scatter(dfx, dfy, c= dfc, cmap = self.colormapin.text(),   marker= "o", s=30) 
                cbar = plt.colorbar()
                cbar.set_label(str(self.coloraxisCombo.currentText()))
            
            
            plt.xlabel(str(ui.XaxisCombo.currentText()), fontsize=16)
            plt.ylabel(str(ui.YaxisCombo.currentText()), fontsize=16)
            crs = mplcursors.cursor(ax,hover=True)

            crs.connect("add", lambda sel: sel.annotation.set_text(
                ' {}'.format(lol[sel.target.index])))
            
        
        elif ui.GraphCombo.currentText() == "3D Plot":   #3D Scatter Plot
            dfz = ldf[str(ui.ZaxisCombo.currentText())].to_list()
            
            fig = plt.figure()
            ax = plt.axes(projection="3d")
            ax.set_title(str(list(ldf.columns)))
            
            if ui.coloraxisCombo.currentText() == "None":   # w/o color axis
                ax.scatter3D(dfx,dfy,dfz)
                
                
            else:                                           # w/ color axis
                dfc = ldf[str(self.coloraxisCombo.currentText())].to_list()
                p = ax.scatter3D(dfx, dfy, dfz, c= dfc, cmap = self.colormapin.text(),   marker= "o", s=30) 
                cbar = fig.colorbar(p)
                cbar.set_label(str(self.coloraxisCombo.currentText()))
            
            
            ax.set_xlabel(str(ui.XaxisCombo.currentText()), fontsize=16)
            ax.set_ylabel(str(ui.YaxisCombo.currentText()), fontsize=16)
            ax.set_zlabel(str(ui.ZaxisCombo.currentText()), fontsize=16)
            crs = mplcursors.cursor(ax,hover=True)

            crs.connect("add", lambda sel: sel.annotation.set_text(
                ' {}'.format(lol[sel.target.index])))
        
        if self.lineEdit_xlim.text() != "":
            plt.xlim(eval(str(self.lineEdit_xlim.text())))
        
        if self.lineEdit_ylim.text() != "":
            plt.ylim(eval(str(self.lineEdit_ylim.text())))
        
        if self.lineEdit_zlim.text() != "" and ui.GraphCombo.currentText() == "3D Plot":
            res = eval(str(self.lineEdit_zlim.text()))
            ax.set_zlim(res[0],res[1])
            
            
        plt.show()
    
    def BrowseMarginFile(self):
        csvfilter = "csv(*.csv)"
        filename = QFileDialog.getOpenFileName(filter = csvfilter)
        self.lineEdit_CSVDir_2.setText(filename[0])
    
    def BrowseSaveDir(self):
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit_MarginDir.setText('{}'.format(directory))
    
    def LoadMarginFile(self):
        filename = self.lineEdit_CSVDir_2.text()
        df = pd.read_csv(filename)
        self.GraphMarginIn.setText(tabulate(df.values, headers = df.columns.values.tolist(), tablefmt="github"))
        
        ls = list(df.columns.values)
        
        self.XaxisCombo_2.clear()
        self.YaxisCombo_2.clear()
        self.ZaxisCombo_2.clear()
        
        
        self.XaxisCombo_2.addItems(ls)
        self.YaxisCombo_2.addItem("None")
        self.YaxisCombo_2.addItems(ls)             
        self.ZaxisCombo_2.addItem("None")
        self.ZaxisCombo_2.addItems(ls)   
    
    margin_df = ''
    
    def RefreshPreview(self):
        global margin_df
        
        try:
            filename = self.lineEdit_CSVDir_2.text()
            df = pd.read_csv(filename)            
            dfx = df[str(ui.XaxisCombo_2.currentText())].to_list()            
            x_shift = int(self.lineEdit_xshift.text())
            
        
        
            if str(ui.ZaxisCombo_2.currentText()) and str(ui.YaxisCombo_2.currentText()) == 'None':
                dfx_new = [i + x_shift for i in dfx]
                
                out = pd.DataFrame(dfx_new, columns = [str(ui.XaxisCombo_2.currentText()) ])
                self.GraphMarginOut.setText(tabulate(out.values, headers = out.columns.values.tolist(), tablefmt="github"))
                margin_df = out
            
            
            elif str(ui.ZaxisCombo_2.currentText()) == 'None':
                dfy = df[str(ui.YaxisCombo_2.currentText())].to_list()
                y_shift = int(self.lineEdit_yshift.text())
                
                dfx_new = [i + x_shift for i in dfx]
                dfy_new = [i + y_shift for i in dfy]
                
                out = pd.DataFrame(list(zip(dfx_new, dfy_new)), columns = [str(ui.XaxisCombo_2.currentText()), str(ui.YaxisCombo_2.currentText())])
                self.GraphMarginOut.setText(tabulate(out.values, headers = out.columns.values.tolist(), tablefmt="github"))
                margin_df = out
            
            else:
                dfy = df[str(ui.YaxisCombo_2.currentText())].to_list()
                y_shift = int(self.lineEdit_yshift.text())
                
                dfz = df[str(ui.ZaxisCombo_2.currentText())].to_list()
                z_shift = int(self.lineEdit_zshift.text())
                
                dfx_new = [i + x_shift for i in dfx]
                dfy_new = [i + y_shift for i in dfy]
                dfz_new = [i + z_shift for i in dfz]
                
                out = pd.DataFrame(list(zip(dfx_new, dfy_new,dfz_new)), columns = [str(ui.XaxisCombo_2.currentText()), str(ui.YaxisCombo_2.currentText()) ,str(ui.ZaxisCombo_2.currentText())])
                self.GraphMarginOut.setText(tabulate(out.values, headers = out.columns.values.tolist(), tablefmt="github"))
                margin_df = out
        
        except:
            return
        
    
    def SaveMargin(self):
        global margin_df
        
        t = time.localtime()
        timestamp = time.strftime('%b-%d-%Y_%H%M', t)
        
        if str(ui.ZaxisCombo_2.currentText()) == 'None':
            filename = str(ui.XaxisCombo_2.currentText()) + "_" + str(ui.YaxisCombo_2.currentText()) + timestamp
        
        else:
            filename = str(ui.XaxisCombo_2.currentText()) + "_" + str(ui.YaxisCombo_2.currentText()) + "_" + str(ui.ZaxisCombo_2.currentText()) + timestamp
        
        df = margin_df
        df.to_csv(str(ui.lineEdit_MarginDir.text()) +'/'+ filename + '.csv', index=False)
        
    def OpenParetoWindow(self):
        ParetoWindow.var_name = fname
        ParetoWindow.df = ldf
        self.window = QtWidgets.QWidget()
        self.ui = ParetoWindow.Ui_Form()
        self.ui.setupUi(self.window)
        
        self.window.show()
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Current File Loaded:"))
        self.Loadedfilename.setText(_translate("MainWindow", "None"))
        self.label.setText(_translate("MainWindow", "File Name"))
        self.BrowseCSVBtn.setText(_translate("MainWindow", "Browse"))
        self.label_24.setText(_translate("MainWindow", "File Information"))
        self.HeaderCheckbox.setText(_translate("MainWindow", "First row contains headers"))
        self.LoadCSVBtn.setText(_translate("MainWindow", "Load File"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "All files used should be in .csv format.\n"
"\n"
"If header checkbox is incorrectly ticked, select the correct option and press the Browse button to reset the formatting.\n"
"\n"
"\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "File Preview"))
        self.label_4.setText(_translate("MainWindow", "x-axis"))
        self.label_5.setText(_translate("MainWindow", "y-axis"))
        self.label_6.setText(_translate("MainWindow", "z-axis"))
        self.label_17.setText(_translate("MainWindow", "Graph Type"))
        self.label_13.setText(_translate("MainWindow", "Color Map"))
        self.colormapin.setText(_translate("MainWindow", "plasma"))
        self.label_18.setText(_translate("MainWindow", "Color Axis"))
        self.label_8.setText(_translate("MainWindow", "x - limits"))
        self.label_9.setText(_translate("MainWindow", "y - limits"))
        self.label_7.setText(_translate("MainWindow", "z - limits"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Axis limits should be placed in the form (lower_limit, upper_limit). \n"
"e.g. Setting (0,5) will create an axis from 0 to 5.\n"
"Leave blank to set axis limits automatically (Recommended, Matplotlib will auto scale to include all points).\n"
"Z - axis settings will be ignored for 2D plots.\n"
"\n"
""))
        self.pushButton_Graph.setText(_translate("MainWindow", "Generate Graph"))
        self.pushButton_Pareto.setText(_translate("MainWindow", "Pareto Front Plotter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Graph Settings"))
        self.label_3.setText(_translate("MainWindow", "Load File"))
        self.BrowseCSVBtn_2.setText(_translate("MainWindow", "Browse"))
        self.label_14.setText(_translate("MainWindow", "Save Directory"))
        self.BrowseCSVBtn_3.setText(_translate("MainWindow", "Browse"))
        self.label_25.setText(_translate("MainWindow", "x-axis"))
        self.label_21.setText(_translate("MainWindow", "x - shift"))
        self.label_26.setText(_translate("MainWindow", "y-axis"))
        self.label_20.setText(_translate("MainWindow", "y - shift"))
        self.label_27.setText(_translate("MainWindow", "z-axis"))
        self.label_19.setText(_translate("MainWindow", "z - shift"))
        self.label_22.setText(_translate("MainWindow", "Input Preview"))
        self.pushButton_loadmargin.setText(_translate("MainWindow", "Load File"))
        self.pushButton_refreshmargin.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_savemargin.setText(_translate("MainWindow", "Save Output"))
        self.label_23.setText(_translate("MainWindow", "Output Preview"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Graph Margins"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
