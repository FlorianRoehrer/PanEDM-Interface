# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './GUI/Interface_Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PanEDMInterfaceMain(object):
    def setupUi(self, PanEDMInterfaceMain):
        PanEDMInterfaceMain.setObjectName("PanEDMInterfaceMain")
        PanEDMInterfaceMain.resize(1180, 702)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/pulse_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PanEDMInterfaceMain.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(PanEDMInterfaceMain)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayoutMain = QtWidgets.QVBoxLayout()
        self.verticalLayoutMain.setObjectName("verticalLayoutMain")
        self.infoarea = QtWidgets.QHBoxLayout()
        self.infoarea.setObjectName("infoarea")
        self.left_side = QtWidgets.QFormLayout()
        self.left_side.setObjectName("left_side")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.left_side.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.username = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.username.setFont(font)
        self.username.setIndent(20)
        self.username.setObjectName("username")
        self.left_side.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)
        self.infoarea.addLayout(self.left_side)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.infoarea.addItem(spacerItem)
        self.middle = QtWidgets.QFormLayout()
        self.middle.setObjectName("middle")
        self.runClockLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.runClockLabel.setFont(font)
        self.runClockLabel.setObjectName("runClockLabel")
        self.middle.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.runClockLabel)
        self.runClockValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.runClockValue.setFont(font)
        self.runClockValue.setIndent(20)
        self.runClockValue.setObjectName("runClockValue")
        self.middle.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.runClockValue)
        self.infoarea.addLayout(self.middle)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.infoarea.addItem(spacerItem1)
        self.right_side = QtWidgets.QFormLayout()
        self.right_side.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.right_side.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.right_side.setObjectName("right_side")
        self.runnumber_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.runnumber_label.setFont(font)
        self.runnumber_label.setObjectName("runnumber_label")
        self.right_side.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.runnumber_label)
        self.runnumber = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.runnumber.setFont(font)
        self.runnumber.setIndent(20)
        self.runnumber.setObjectName("runnumber")
        self.right_side.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.runnumber)
        self.infoarea.addLayout(self.right_side)
        self.verticalLayoutMain.addLayout(self.infoarea)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayoutMain.addItem(spacerItem2)
        self.controlarea = QtWidgets.QHBoxLayout()
        self.controlarea.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.controlarea.setObjectName("controlarea")
        self.controlgroup = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlgroup.sizePolicy().hasHeightForWidth())
        self.controlgroup.setSizePolicy(sizePolicy)
        self.controlgroup.setMaximumSize(QtCore.QSize(612, 2000))
        self.controlgroup.setObjectName("controlgroup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.controlgroup)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.switchlist = QtWidgets.QListWidget(self.controlgroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.switchlist.sizePolicy().hasHeightForWidth())
        self.switchlist.setSizePolicy(sizePolicy)
        self.switchlist.setMaximumSize(QtCore.QSize(75, 16777215))
        self.switchlist.setFocusPolicy(QtCore.Qt.NoFocus)
        self.switchlist.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.switchlist.setAlternatingRowColors(False)
        self.switchlist.setIconSize(QtCore.QSize(70, 70))
        self.switchlist.setTextElideMode(QtCore.Qt.ElideRight)
        self.switchlist.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.switchlist.setViewMode(QtWidgets.QListView.IconMode)
        self.switchlist.setModelColumn(0)
        self.switchlist.setUniformItemSizes(True)
        self.switchlist.setBatchSize(100)
        self.switchlist.setWordWrap(False)
        self.switchlist.setSelectionRectVisible(True)
        self.switchlist.setObjectName("switchlist")
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/autocontrol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.switchlist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/manualcontrol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.switchlist.addItem(item)
        self.horizontalLayout.addWidget(self.switchlist)
        self.stackedWidget = QtWidgets.QStackedWidget(self.controlgroup)
        self.stackedWidget.setObjectName("stackedWidget")
        self.auto_page = QtWidgets.QWidget()
        self.auto_page.setObjectName("auto_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.auto_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.autocontrolgrid = QtWidgets.QGridLayout()
        self.autocontrolgrid.setObjectName("autocontrolgrid")
        self.configFileLineEdit = QtWidgets.QLineEdit(self.auto_page)
        self.configFileLineEdit.setObjectName("configFileLineEdit")
        self.autocontrolgrid.addWidget(self.configFileLineEdit, 0, 0, 1, 1)
        self.autoChooseButton = QtWidgets.QPushButton(self.auto_page)
        self.autoChooseButton.setObjectName("autoChooseButton")
        self.autocontrolgrid.addWidget(self.autoChooseButton, 0, 1, 1, 1)
        self.autoLoadButton = QtWidgets.QPushButton(self.auto_page)
        self.autoLoadButton.setObjectName("autoLoadButton")
        self.autocontrolgrid.addWidget(self.autoLoadButton, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.autocontrolgrid.addItem(spacerItem3, 1, 0, 1, 1)
        self.controlbuttongrid = QtWidgets.QGridLayout()
        self.controlbuttongrid.setObjectName("controlbuttongrid")
        self.autoStopButton = QtWidgets.QPushButton(self.auto_page)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.autoStopButton.setIcon(icon3)
        self.autoStopButton.setIconSize(QtCore.QSize(48, 48))
        self.autoStopButton.setObjectName("autoStopButton")
        self.controlbuttongrid.addWidget(self.autoStopButton, 0, 1, 1, 1)
        self.autoStartButton = QtWidgets.QPushButton(self.auto_page)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.autoStartButton.setIcon(icon4)
        self.autoStartButton.setIconSize(QtCore.QSize(48, 48))
        self.autoStartButton.setObjectName("autoStartButton")
        self.controlbuttongrid.addWidget(self.autoStartButton, 0, 0, 1, 1)
        self.autoPauseButton = QtWidgets.QPushButton(self.auto_page)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.autoPauseButton.setIcon(icon5)
        self.autoPauseButton.setIconSize(QtCore.QSize(48, 48))
        self.autoPauseButton.setObjectName("autoPauseButton")
        self.controlbuttongrid.addWidget(self.autoPauseButton, 1, 0, 1, 1)
        self.autoOnestepButton = QtWidgets.QPushButton(self.auto_page)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/onestep.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.autoOnestepButton.setIcon(icon6)
        self.autoOnestepButton.setIconSize(QtCore.QSize(48, 48))
        self.autoOnestepButton.setObjectName("autoOnestepButton")
        self.controlbuttongrid.addWidget(self.autoOnestepButton, 1, 1, 1, 1)
        self.autocontrolgrid.addLayout(self.controlbuttongrid, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.autocontrolgrid, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.auto_page)
        self.manual_page = QtWidgets.QWidget()
        self.manual_page.setObjectName("manual_page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.manual_page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.manual_page)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.controlarea.addWidget(self.controlgroup)
        self.runStatus = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runStatus.sizePolicy().hasHeightForWidth())
        self.runStatus.setSizePolicy(sizePolicy)
        self.runStatus.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.runStatus.setObjectName("runStatus")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.runStatus)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.runStatusTextEdit = QtWidgets.QTextEdit(self.runStatus)
        self.runStatusTextEdit.setReadOnly(True)
        self.runStatusTextEdit.setObjectName("runStatusTextEdit")
        self.verticalLayout.addWidget(self.runStatusTextEdit)
        self.verticalLayout_10.addLayout(self.verticalLayout)
        self.controlarea.addWidget(self.runStatus)
        self.verticalLayoutMain.addLayout(self.controlarea)
        self.message_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.message_tabs.setObjectName("message_tabs")
        self.all_tab = QtWidgets.QWidget()
        self.all_tab.setObjectName("all_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.all_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.all_text = QtWidgets.QTextEdit(self.all_tab)
        self.all_text.setReadOnly(True)
        self.all_text.setObjectName("all_text")
        self.verticalLayout_5.addWidget(self.all_text)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.message_tabs.addTab(self.all_tab, "")
        self.critical_tab = QtWidgets.QWidget()
        self.critical_tab.setObjectName("critical_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.critical_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.critical_text = QtWidgets.QTextEdit(self.critical_tab)
        self.critical_text.setReadOnly(True)
        self.critical_text.setObjectName("critical_text")
        self.verticalLayout_3.addWidget(self.critical_text)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.message_tabs.addTab(self.critical_tab, "")
        self.comments_tab = QtWidgets.QWidget()
        self.comments_tab.setObjectName("comments_tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.comments_tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.comments_text = QtWidgets.QTextEdit(self.comments_tab)
        self.comments_text.setObjectName("comments_text")
        self.verticalLayout_7.addWidget(self.comments_text)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.message_tabs.addTab(self.comments_tab, "")
        self.verticalLayoutMain.addWidget(self.message_tabs)
        self.verticalLayout_2.addLayout(self.verticalLayoutMain)
        PanEDMInterfaceMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PanEDMInterfaceMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1180, 32))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        PanEDMInterfaceMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PanEDMInterfaceMain)
        self.statusbar.setObjectName("statusbar")
        PanEDMInterfaceMain.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(PanEDMInterfaceMain)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        PanEDMInterfaceMain.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionChange_user = QtWidgets.QAction(PanEDMInterfaceMain)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icons/change-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChange_user.setIcon(icon7)
        self.actionChange_user.setObjectName("actionChange_user")
        self.actionClose = QtWidgets.QAction(PanEDMInterfaceMain)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icons/close_red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon8)
        self.actionClose.setObjectName("actionClose")
        self.actionAbout = QtWidgets.QAction(PanEDMInterfaceMain)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon9)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSettings = QtWidgets.QAction(PanEDMInterfaceMain)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon10)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionChange_user)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionChange_user)
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionClose)
        self.toolBar.addSeparator()

        self.retranslateUi(PanEDMInterfaceMain)
        self.stackedWidget.setCurrentIndex(0)
        self.message_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PanEDMInterfaceMain)

    def retranslateUi(self, PanEDMInterfaceMain):
        _translate = QtCore.QCoreApplication.translate
        PanEDMInterfaceMain.setWindowTitle(_translate("PanEDMInterfaceMain", "PanEDM Control"))
        self.username_label.setText(_translate("PanEDMInterfaceMain", "User:"))
        self.username.setText(_translate("PanEDMInterfaceMain", "Username"))
        self.runClockLabel.setText(_translate("PanEDMInterfaceMain", "Run clock:"))
        self.runClockValue.setText(_translate("PanEDMInterfaceMain", "0:00:00"))
        self.runnumber_label.setText(_translate("PanEDMInterfaceMain", "Run number:"))
        self.runnumber.setText(_translate("PanEDMInterfaceMain", "#1"))
        self.controlgroup.setTitle(_translate("PanEDMInterfaceMain", "Control"))
        __sortingEnabled = self.switchlist.isSortingEnabled()
        self.switchlist.setSortingEnabled(False)
        item = self.switchlist.item(0)
        item.setText(_translate("PanEDMInterfaceMain", "Automatic"))
        item = self.switchlist.item(1)
        item.setText(_translate("PanEDMInterfaceMain", "Manually"))
        self.switchlist.setSortingEnabled(__sortingEnabled)
        self.autoChooseButton.setText(_translate("PanEDMInterfaceMain", "Choose file"))
        self.autoLoadButton.setText(_translate("PanEDMInterfaceMain", "Load file"))
        self.autoStopButton.setText(_translate("PanEDMInterfaceMain", "Stop run"))
        self.autoStartButton.setText(_translate("PanEDMInterfaceMain", "Start run"))
        self.autoPauseButton.setText(_translate("PanEDMInterfaceMain", "Pause"))
        self.autoOnestepButton.setText(_translate("PanEDMInterfaceMain", "Execute one step"))
        self.runStatus.setTitle(_translate("PanEDMInterfaceMain", "Run status"))
        self.message_tabs.setTabText(self.message_tabs.indexOf(self.all_tab), _translate("PanEDMInterfaceMain", "Action Log"))
        self.message_tabs.setTabText(self.message_tabs.indexOf(self.critical_tab), _translate("PanEDMInterfaceMain", "Critical messages"))
        self.message_tabs.setTabText(self.message_tabs.indexOf(self.comments_tab), _translate("PanEDMInterfaceMain", "Comments"))
        self.menuFile.setTitle(_translate("PanEDMInterfaceMain", "Fi&le"))
        self.menuHelp.setTitle(_translate("PanEDMInterfaceMain", "Help"))
        self.toolBar.setWindowTitle(_translate("PanEDMInterfaceMain", "toolBar"))
        self.actionChange_user.setText(_translate("PanEDMInterfaceMain", "Change &user"))
        self.actionClose.setText(_translate("PanEDMInterfaceMain", "&Close"))
        self.actionAbout.setText(_translate("PanEDMInterfaceMain", "&About"))
        self.actionSettings.setText(_translate("PanEDMInterfaceMain", "&Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PanEDMInterfaceMain = QtWidgets.QMainWindow()
    ui = Ui_PanEDMInterfaceMain()
    ui.setupUi(PanEDMInterfaceMain)
    PanEDMInterfaceMain.show()
    sys.exit(app.exec_())

