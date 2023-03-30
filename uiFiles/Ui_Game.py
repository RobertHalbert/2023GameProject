# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Project\GameProject\uiFiles\Game.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1089, 711)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameWindow = QtWidgets.QFrame(self.centralwidget)
        self.frameWindow.setGeometry(QtCore.QRect(0, 0, 1081, 651))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frameWindow.setFont(font)
        self.frameWindow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameWindow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameWindow.setObjectName("frameWindow")
        self.mainTextBox = QtWidgets.QPlainTextEdit(self.frameWindow)
        self.mainTextBox.setGeometry(QtCore.QRect(270, 0, 581, 381))
        self.mainTextBox.setReadOnly(True)
        self.mainTextBox.setObjectName("mainTextBox")
        self.frameInfo = QtWidgets.QFrame(self.frameWindow)
        self.frameInfo.setGeometry(QtCore.QRect(0, 0, 271, 611))
        self.frameInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInfo.setObjectName("frameInfo")
        self.formLayoutWidget = QtWidgets.QWidget(self.frameInfo)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 251, 571))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayoutInfo = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayoutInfo.setContentsMargins(0, 0, 0, 0)
        self.formLayoutInfo.setObjectName("formLayoutInfo")
        self.labelName = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelName.setObjectName("labelName")
        self.formLayoutInfo.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.labelName)
        self.labelPlayerHealth = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelPlayerHealth.setObjectName("labelPlayerHealth")
        self.formLayoutInfo.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.labelPlayerHealth)
        self.barHealth = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.barHealth.setProperty("value", 100)
        self.barHealth.setObjectName("barHealth")
        self.formLayoutInfo.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.barHealth)
        self.labelLocation = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelLocation.setObjectName("labelLocation")
        self.formLayoutInfo.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.labelLocation)
        self.labelTime = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelTime.setObjectName("labelTime")
        self.formLayoutInfo.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.labelTime)
        self.labelDate = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelDate.setObjectName("labelDate")
        self.formLayoutInfo.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.labelDate)
        spacerItem = QtWidgets.QSpacerItem(5, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayoutInfo.setItem(9, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.labelGold = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelGold.setObjectName("labelGold")
        self.formLayoutInfo.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.labelGold)
        self.labelWeapon = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelWeapon.setObjectName("labelWeapon")
        self.formLayoutInfo.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.labelWeapon)
        self.labelWEquippped = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelWEquippped.setObjectName("labelWEquippped")
        self.formLayoutInfo.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.labelWEquippped)
        self.labelArmor = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelArmor.setObjectName("labelArmor")
        self.formLayoutInfo.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.labelArmor)
        self.labelAEquipped = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelAEquipped.setObjectName("labelAEquipped")
        self.formLayoutInfo.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.labelAEquipped)
        spacerItem1 = QtWidgets.QSpacerItem(5, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayoutInfo.setItem(5, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.labelLevel = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelLevel.setObjectName("labelLevel")
        self.formLayoutInfo.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.labelLevel)
        self.labelXp = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelXp.setObjectName("labelXp")
        self.formLayoutInfo.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.labelXp)
        spacerItem2 = QtWidgets.QSpacerItem(38, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayoutInfo.setItem(13, QtWidgets.QFormLayout.SpanningRole, spacerItem2)
        self.labelStrength = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelStrength.setObjectName("labelStrength")
        self.formLayoutInfo.setWidget(14, QtWidgets.QFormLayout.SpanningRole, self.labelStrength)
        self.labelDexterity = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelDexterity.setObjectName("labelDexterity")
        self.formLayoutInfo.setWidget(15, QtWidgets.QFormLayout.SpanningRole, self.labelDexterity)
        self.labelArcane = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelArcane.setObjectName("labelArcane")
        self.formLayoutInfo.setWidget(16, QtWidgets.QFormLayout.SpanningRole, self.labelArcane)
        self.labelConstitution = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelConstitution.setObjectName("labelConstitution")
        self.formLayoutInfo.setWidget(17, QtWidgets.QFormLayout.SpanningRole, self.labelConstitution)
        self.labelCharisma = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelCharisma.setObjectName("labelCharisma")
        self.formLayoutInfo.setWidget(18, QtWidgets.QFormLayout.SpanningRole, self.labelCharisma)
        spacerItem3 = QtWidgets.QSpacerItem(38, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayoutInfo.setItem(19, QtWidgets.QFormLayout.SpanningRole, spacerItem3)
        self.labelSlots = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelSlots.setObjectName("labelSlots")
        self.formLayoutInfo.setWidget(20, QtWidgets.QFormLayout.SpanningRole, self.labelSlots)
        self.frameButtons = QtWidgets.QFrame(self.frameWindow)
        self.frameButtons.setGeometry(QtCore.QRect(290, 390, 541, 261))
        self.frameButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameButtons.setObjectName("frameButtons")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frameButtons)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 541, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutButtons = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayoutButtons.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutButtons.setObjectName("gridLayoutButtons")
        self.ButtonD = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonD.setMinimumSize(QtCore.QSize(0, 60))
        self.ButtonD.setObjectName("ButtonD")
        self.gridLayoutButtons.addWidget(self.ButtonD, 1, 2, 1, 1)
        self.ButtonC = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonC.setMinimumSize(QtCore.QSize(0, 60))
        self.ButtonC.setObjectName("ButtonC")
        self.gridLayoutButtons.addWidget(self.ButtonC, 2, 2, 1, 1)
        self.ButtonW = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonW.setMinimumSize(QtCore.QSize(0, 60))
        self.ButtonW.setObjectName("ButtonW")
        self.gridLayoutButtons.addWidget(self.ButtonW, 0, 1, 1, 1)
        self.ButtonX = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonX.setMinimumSize(QtCore.QSize(0, 60))
        self.ButtonX.setObjectName("ButtonX")
        self.gridLayoutButtons.addWidget(self.ButtonX, 2, 1, 1, 1)
        self.ButtonE = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonE.setMinimumSize(QtCore.QSize(0, 60))
        self.ButtonE.setObjectName("ButtonE")
        self.gridLayoutButtons.addWidget(self.ButtonE, 0, 2, 1, 1)
        self.ButtonA = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonA.setMinimumSize(QtCore.QSize(0, 60))
        self.ButtonA.setObjectName("ButtonA")
        self.gridLayoutButtons.addWidget(self.ButtonA, 1, 0, 1, 1)
        self.ButtonQ = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonQ.setMinimumSize(QtCore.QSize(0, 60))
        self.ButtonQ.setObjectName("ButtonQ")
        self.gridLayoutButtons.addWidget(self.ButtonQ, 0, 0, 1, 1)
        self.ButtonS = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonS.setMinimumSize(QtCore.QSize(0, 60))
        self.ButtonS.setObjectName("ButtonS")
        self.gridLayoutButtons.addWidget(self.ButtonS, 1, 1, 1, 1)
        self.ButtonZ = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonZ.setMinimumSize(QtCore.QSize(0, 60))
        self.ButtonZ.setObjectName("ButtonZ")
        self.gridLayoutButtons.addWidget(self.ButtonZ, 2, 0, 1, 1)
        self.ButtonR = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonR.setMinimumSize(QtCore.QSize(0, 60))
        self.ButtonR.setObjectName("ButtonR")
        self.gridLayoutButtons.addWidget(self.ButtonR, 0, 3, 1, 1)
        self.ButtonF = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonF.setMinimumSize(QtCore.QSize(0, 60))
        self.ButtonF.setObjectName("ButtonF")
        self.gridLayoutButtons.addWidget(self.ButtonF, 1, 3, 1, 1)
        self.ButtonV = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonV.setMinimumSize(QtCore.QSize(0, 60))
        self.ButtonV.setObjectName("ButtonV")
        self.gridLayoutButtons.addWidget(self.ButtonV, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.frameButtons)
        self.label.setGeometry(QtCore.QRect(240, 230, 61, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frameEnemyInfo = QtWidgets.QFrame(self.frameWindow)
        self.frameEnemyInfo.setGeometry(QtCore.QRect(880, 0, 201, 461))
        self.frameEnemyInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameEnemyInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameEnemyInfo.setObjectName("frameEnemyInfo")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frameEnemyInfo)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 181, 321))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayoutEnemy = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayoutEnemy.setContentsMargins(0, 0, 0, 0)
        self.formLayoutEnemy.setObjectName("formLayoutEnemy")
        self.labelEnemy = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.labelEnemy.setObjectName("labelEnemy")
        self.formLayoutEnemy.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.labelEnemy)
        self.labelHPEnemy = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.labelHPEnemy.setObjectName("labelHPEnemy")
        self.formLayoutEnemy.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.labelHPEnemy)
        self.progressBarEnemyHp = QtWidgets.QProgressBar(self.formLayoutWidget_2)
        self.progressBarEnemyHp.setProperty("value", 100)
        self.progressBarEnemyHp.setObjectName("progressBarEnemyHp")
        self.formLayoutEnemy.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.progressBarEnemyHp)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1089, 29))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Game = QtWidgets.QAction(MainWindow)
        self.actionNew_Game.setObjectName("actionNew_Game")
        self.actionLoad_Game = QtWidgets.QAction(MainWindow)
        self.actionLoad_Game.setObjectName("actionLoad_Game")
        self.actionSave_Game = QtWidgets.QAction(MainWindow)
        self.actionSave_Game.setObjectName("actionSave_Game")
        self.actionExit_Game = QtWidgets.QAction(MainWindow)
        self.actionExit_Game.setObjectName("actionExit_Game")
        self.actionSave_Game_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_Game_2.setObjectName("actionSave_Game_2")
        self.actionLoad_Game_2 = QtWidgets.QAction(MainWindow)
        self.actionLoad_Game_2.setObjectName("actionLoad_Game_2")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuMenu.addAction(self.actionNew_Game)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionSave_Game_2)
        self.menuMenu.addAction(self.actionLoad_Game_2)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionHelp)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit_Game)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelName.setText(_translate("MainWindow", "TESTNAME"))
        self.labelPlayerHealth.setText(_translate("MainWindow", "Health"))
        self.labelLocation.setText(_translate("MainWindow", "location"))
        self.labelTime.setText(_translate("MainWindow", "time"))
        self.labelDate.setText(_translate("MainWindow", "date"))
        self.labelGold.setText(_translate("MainWindow", "gold"))
        self.labelWeapon.setText(_translate("MainWindow", "Weapon:"))
        self.labelWEquippped.setText(_translate("MainWindow", "TextLabel"))
        self.labelArmor.setText(_translate("MainWindow", "Armor:"))
        self.labelAEquipped.setText(_translate("MainWindow", "TextLabel"))
        self.labelLevel.setText(_translate("MainWindow", "Level"))
        self.labelXp.setText(_translate("MainWindow", "xp"))
        self.labelStrength.setText(_translate("MainWindow", "Strength"))
        self.labelDexterity.setText(_translate("MainWindow", "Dexterity"))
        self.labelArcane.setText(_translate("MainWindow", "Arcane"))
        self.labelConstitution.setText(_translate("MainWindow", "Constitution"))
        self.labelCharisma.setText(_translate("MainWindow", "Charisma"))
        self.labelSlots.setText(_translate("MainWindow", "slots"))
        self.ButtonD.setText(_translate("MainWindow", "PushButton"))
        self.ButtonC.setText(_translate("MainWindow", "PushButton"))
        self.ButtonW.setText(_translate("MainWindow", "PushButton"))
        self.ButtonX.setText(_translate("MainWindow", "PushButton"))
        self.ButtonE.setText(_translate("MainWindow", "PushButton"))
        self.ButtonA.setText(_translate("MainWindow", "PushButton"))
        self.ButtonQ.setText(_translate("MainWindow", "PushButton"))
        self.ButtonS.setText(_translate("MainWindow", "PushButton"))
        self.ButtonZ.setText(_translate("MainWindow", "PushButton"))
        self.ButtonR.setText(_translate("MainWindow", "PushButton"))
        self.ButtonF.setText(_translate("MainWindow", "PushButton"))
        self.ButtonV.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "[5,5]"))
        self.labelEnemy.setText(_translate("MainWindow", "TextLabel"))
        self.labelHPEnemy.setText(_translate("MainWindow", "TextLabel"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionNew_Game.setText(_translate("MainWindow", "New Game (F3)"))
        self.actionLoad_Game.setText(_translate("MainWindow", "Load Game"))
        self.actionSave_Game.setText(_translate("MainWindow", "Save Game"))
        self.actionExit_Game.setText(_translate("MainWindow", "Exit Game (F4)"))
        self.actionSave_Game_2.setText(_translate("MainWindow", "Save Game (F5)"))
        self.actionLoad_Game_2.setText(_translate("MainWindow", "Load Game (F6)"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
