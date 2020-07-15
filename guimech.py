# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guimech.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(800, 480)
        main.setMinimumSize(QtCore.QSize(800, 480))
        main.setMaximumSize(QtCore.QSize(800, 480))
        main.setStyleSheet("")
        self.gridLayout_3 = QtWidgets.QGridLayout(main)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mainTabs = QtWidgets.QTabWidget(main)
        self.mainTabs.setFocusPolicy(QtCore.Qt.TabFocus)
        self.mainTabs.setAutoFillBackground(False)
        self.mainTabs.setStyleSheet("")
        self.mainTabs.setTabPosition(QtWidgets.QTabWidget.South)
        self.mainTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.mainTabs.setElideMode(QtCore.Qt.ElideNone)
        self.mainTabs.setUsesScrollButtons(False)
        self.mainTabs.setDocumentMode(True)
        self.mainTabs.setTabsClosable(False)
        self.mainTabs.setMovable(True)
        self.mainTabs.setTabBarAutoHide(False)
        self.mainTabs.setObjectName("mainTabs")
        self.setupTab = QtWidgets.QWidget()
        self.setupTab.setObjectName("setupTab")
        self.insertGroup = QtWidgets.QGroupBox(self.setupTab)
        self.insertGroup.setGeometry(QtCore.QRect(10, 10, 211, 361))
        self.insertGroup.setObjectName("insertGroup")
        self.jogZplus = QtWidgets.QPushButton(self.insertGroup)
        self.jogZplus.setGeometry(QtCore.QRect(110, 200, 91, 71))
        self.jogZplus.setMinimumSize(QtCore.QSize(77, 0))
        self.jogZplus.setMaximumSize(QtCore.QSize(1000, 1000))
        self.jogZplus.setStyleSheet("")
        self.jogZplus.setFlat(False)
        self.jogZplus.setObjectName("jogZplus")
        self.jogZminus = QtWidgets.QPushButton(self.insertGroup)
        self.jogZminus.setGeometry(QtCore.QRect(10, 200, 91, 71))
        self.jogZminus.setMinimumSize(QtCore.QSize(77, 0))
        self.jogZminus.setMaximumSize(QtCore.QSize(1000, 1000))
        self.jogZminus.setStyleSheet("")
        self.jogZminus.setFlat(False)
        self.jogZminus.setObjectName("jogZminus")
        self.setZdist = QtWidgets.QPushButton(self.insertGroup)
        self.setZdist.setGeometry(QtCore.QRect(10, 280, 191, 71))
        self.setZdist.setMinimumSize(QtCore.QSize(77, 0))
        self.setZdist.setMaximumSize(QtCore.QSize(1000, 1000))
        self.setZdist.setStyleSheet("")
        self.setZdist.setFlat(False)
        self.setZdist.setObjectName("setZdist")
        self.insertSpeed = QtWidgets.QSpinBox(self.insertGroup)
        self.insertSpeed.setGeometry(QtCore.QRect(20, 50, 171, 51))
        self.insertSpeed.setStyleSheet("")
        self.insertSpeed.setWrapping(False)
        self.insertSpeed.setFrame(False)
        self.insertSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.insertSpeed.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.insertSpeed.setMinimum(5)
        self.insertSpeed.setMaximum(100)
        self.insertSpeed.setSingleStep(5)
        self.insertSpeed.setObjectName("insertSpeed")
        self.motspeedLab = QtWidgets.QLabel(self.insertGroup)
        self.motspeedLab.setGeometry(QtCore.QRect(60, 30, 91, 21))
        self.motspeedLab.setStyleSheet("")
        self.motspeedLab.setAlignment(QtCore.Qt.AlignCenter)
        self.motspeedLab.setObjectName("motspeedLab")
        self.setZhome = QtWidgets.QPushButton(self.insertGroup)
        self.setZhome.setGeometry(QtCore.QRect(10, 120, 191, 71))
        self.setZhome.setMinimumSize(QtCore.QSize(77, 0))
        self.setZhome.setMaximumSize(QtCore.QSize(1000, 1000))
        self.setZhome.setStyleSheet("")
        self.setZhome.setFlat(False)
        self.setZhome.setObjectName("setZhome")
        self.jogZplus.raise_()
        self.jogZminus.raise_()
        self.setZdist.raise_()
        self.insertSpeed.raise_()
        self.setZhome.raise_()
        self.motspeedLab.raise_()
        self.rotGroup = QtWidgets.QGroupBox(self.setupTab)
        self.rotGroup.setGeometry(QtCore.QRect(230, 10, 211, 361))
        self.rotGroup.setObjectName("rotGroup")
        self.jogZRotplus = QtWidgets.QPushButton(self.rotGroup)
        self.jogZRotplus.setGeometry(QtCore.QRect(110, 200, 91, 71))
        self.jogZRotplus.setMinimumSize(QtCore.QSize(77, 71))
        self.jogZRotplus.setMaximumSize(QtCore.QSize(1000, 1000))
        self.jogZRotplus.setStyleSheet("")
        self.jogZRotplus.setFlat(False)
        self.jogZRotplus.setObjectName("jogZRotplus")
        self.jogZRotminus = QtWidgets.QPushButton(self.rotGroup)
        self.jogZRotminus.setGeometry(QtCore.QRect(10, 200, 91, 71))
        self.jogZRotminus.setMinimumSize(QtCore.QSize(77, 71))
        self.jogZRotminus.setMaximumSize(QtCore.QSize(1000, 1000))
        self.jogZRotminus.setStyleSheet("")
        self.jogZRotminus.setFlat(False)
        self.jogZRotminus.setObjectName("jogZRotminus")
        self.setZrot = QtWidgets.QPushButton(self.rotGroup)
        self.setZrot.setGeometry(QtCore.QRect(10, 280, 191, 71))
        self.setZrot.setMinimumSize(QtCore.QSize(77, 0))
        self.setZrot.setMaximumSize(QtCore.QSize(1000, 1000))
        self.setZrot.setStyleSheet("")
        self.setZrot.setFlat(False)
        self.setZrot.setObjectName("setZrot")
        self.rotSpeed = QtWidgets.QSpinBox(self.rotGroup)
        self.rotSpeed.setGeometry(QtCore.QRect(20, 50, 171, 51))
        self.rotSpeed.setStyleSheet("")
        self.rotSpeed.setWrapping(False)
        self.rotSpeed.setFrame(False)
        self.rotSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.rotSpeed.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.rotSpeed.setMinimum(5)
        self.rotSpeed.setMaximum(100)
        self.rotSpeed.setSingleStep(5)
        self.rotSpeed.setObjectName("rotSpeed")
        self.rotspeedLab = QtWidgets.QLabel(self.rotGroup)
        self.rotspeedLab.setGeometry(QtCore.QRect(60, 30, 101, 21))
        self.rotspeedLab.setAlignment(QtCore.Qt.AlignCenter)
        self.rotspeedLab.setObjectName("rotspeedLab")
        self.zerZRotHome = QtWidgets.QPushButton(self.rotGroup)
        self.zerZRotHome.setGeometry(QtCore.QRect(10, 120, 191, 71))
        self.zerZRotHome.setMinimumSize(QtCore.QSize(77, 71))
        self.zerZRotHome.setMaximumSize(QtCore.QSize(1000, 1000))
        self.zerZRotHome.setStyleSheet("")
        self.zerZRotHome.setFlat(False)
        self.zerZRotHome.setObjectName("zerZRotHome")
        self.jogZRotplus.raise_()
        self.jogZRotminus.raise_()
        self.setZrot.raise_()
        self.rotSpeed.raise_()
        self.zerZRotHome.raise_()
        self.rotspeedLab.raise_()
        self.readyStatus = QtWidgets.QFrame(self.setupTab)
        self.readyStatus.setGeometry(QtCore.QRect(460, 310, 111, 61))
        self.readyStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.readyStatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.readyStatus.setObjectName("readyStatus")
        self.label_17 = QtWidgets.QLabel(self.readyStatus)
        self.label_17.setGeometry(QtCore.QRect(60, 10, 41, 41))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/icons/icons/online.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_15 = QtWidgets.QLabel(self.readyStatus)
        self.label_15.setGeometry(QtCore.QRect(10, 20, 41, 20))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.pushButton_22 = QtWidgets.QPushButton(self.setupTab)
        self.pushButton_22.setGeometry(QtCore.QRect(460, 240, 111, 61))
        self.pushButton_22.setMinimumSize(QtCore.QSize(77, 0))
        self.pushButton_22.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_22.setStyleSheet("")
        self.pushButton_22.setFlat(False)
        self.pushButton_22.setObjectName("pushButton_22")
        self.insertSetStatus = QtWidgets.QGroupBox(self.setupTab)
        self.insertSetStatus.setGeometry(QtCore.QRect(460, 10, 141, 101))
        self.insertSetStatus.setStyleSheet("")
        self.insertSetStatus.setObjectName("insertSetStatus")
        self.homeIset = QtWidgets.QLabel(self.insertSetStatus)
        self.homeIset.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.homeIset.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.homeIset.setObjectName("homeIset")
        self.label_9 = QtWidgets.QLabel(self.insertSetStatus)
        self.label_9.setGeometry(QtCore.QRect(100, 60, 31, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/icons/icons/green-led-on.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.distanceIset = QtWidgets.QLabel(self.insertSetStatus)
        self.distanceIset.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.distanceIset.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.distanceIset.setObjectName("distanceIset")
        self.homeInsertLED = QtWidgets.QLabel(self.insertSetStatus)
        self.homeInsertLED.setGeometry(QtCore.QRect(100, 20, 31, 31))
        self.homeInsertLED.setText("")
        self.homeInsertLED.setPixmap(QtGui.QPixmap(":/icons/icons/green-led-on.png"))
        self.homeInsertLED.setScaledContents(True)
        self.homeInsertLED.setObjectName("homeInsertLED")
        self.pushButton_23 = QtWidgets.QPushButton(self.setupTab)
        self.pushButton_23.setGeometry(QtCore.QRect(580, 310, 181, 61))
        self.pushButton_23.setMinimumSize(QtCore.QSize(77, 0))
        self.pushButton_23.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_23.setStyleSheet("")
        self.pushButton_23.setFlat(False)
        self.pushButton_23.setObjectName("pushButton_23")
        self.rotateSetStatus = QtWidgets.QGroupBox(self.setupTab)
        self.rotateSetStatus.setGeometry(QtCore.QRect(620, 10, 141, 101))
        self.rotateSetStatus.setStyleSheet("")
        self.rotateSetStatus.setObjectName("rotateSetStatus")
        self.homeSet = QtWidgets.QLabel(self.rotateSetStatus)
        self.homeSet.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.homeSet.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.homeSet.setObjectName("homeSet")
        self.rotateLED = QtWidgets.QLabel(self.rotateSetStatus)
        self.rotateLED.setGeometry(QtCore.QRect(100, 60, 31, 31))
        self.rotateLED.setText("")
        self.rotateLED.setPixmap(QtGui.QPixmap(":/icons/icons/green-led-on.png"))
        self.rotateLED.setScaledContents(True)
        self.rotateLED.setObjectName("rotateLED")
        self.rotationSet = QtWidgets.QLabel(self.rotateSetStatus)
        self.rotationSet.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.rotationSet.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rotationSet.setObjectName("rotationSet")
        self.homeRotSet = QtWidgets.QLabel(self.rotateSetStatus)
        self.homeRotSet.setGeometry(QtCore.QRect(100, 20, 31, 31))
        self.homeRotSet.setText("")
        self.homeRotSet.setPixmap(QtGui.QPixmap(":/icons/icons/green-led-on.png"))
        self.homeRotSet.setScaledContents(True)
        self.homeRotSet.setObjectName("homeRotSet")
        self.pushButton_21 = QtWidgets.QPushButton(self.setupTab)
        self.pushButton_21.setGeometry(QtCore.QRect(580, 240, 181, 61))
        self.pushButton_21.setMinimumSize(QtCore.QSize(77, 0))
        self.pushButton_21.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_21.setStyleSheet("")
        self.pushButton_21.setFlat(False)
        self.pushButton_21.setObjectName("pushButton_21")
        self.textBox = QtWidgets.QTextBrowser(self.setupTab)
        self.textBox.setGeometry(QtCore.QRect(460, 150, 301, 61))
        self.textBox.setObjectName("textBox")
        self.mainTabs.addTab(self.setupTab, "")
        self.gridLayout_3.addWidget(self.mainTabs, 0, 0, 1, 1)

        self.retranslateUi(main)
        self.mainTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.insertGroup.setTitle(_translate("main", "Key Insert/Extract"))
        self.jogZplus.setText(_translate("main", "JOG (+)"))
        self.jogZminus.setText(_translate("main", "JOG (–)"))
        self.setZdist.setText(_translate("main", "SET DISTANCE"))
        self.insertSpeed.setSuffix(_translate("main", " %"))
        self.motspeedLab.setText(_translate("main", "Motion Speed"))
        self.setZhome.setText(_translate("main", "SET HOME"))
        self.rotGroup.setTitle(_translate("main", "Key Rotation"))
        self.jogZRotplus.setText(_translate("main", "JOG (+)"))
        self.jogZRotminus.setText(_translate("main", "JOG (–)"))
        self.setZrot.setText(_translate("main", "SET ROTATION"))
        self.rotSpeed.setSuffix(_translate("main", " %"))
        self.rotspeedLab.setText(_translate("main", "Rotation Speed"))
        self.zerZRotHome.setText(_translate("main", "SET HOME"))
        self.label_15.setText(_translate("main", "READY"))
        self.pushButton_22.setText(_translate("main", "CLEAR"))
        self.insertSetStatus.setTitle(_translate("main", "Insert"))
        self.homeIset.setText(_translate("main", "Home I Set"))
        self.distanceIset.setText(_translate("main", "Distance Set"))
        self.pushButton_23.setText(_translate("main", "START TEST"))
        self.rotateSetStatus.setTitle(_translate("main", "Rotate"))
        self.homeSet.setText(_translate("main", "Home II Set"))
        self.rotationSet.setText(_translate("main", "Rotation Set"))
        self.pushButton_21.setText(_translate("main", "INITIALIZE"))
        self.textBox.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">TEST</span></p></body></html>"))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.setupTab), _translate("main", "SETUP"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QWidget()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())