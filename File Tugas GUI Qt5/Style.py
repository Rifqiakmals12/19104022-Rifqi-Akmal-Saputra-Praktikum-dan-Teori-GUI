# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Style.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Style(object):
    def setupUi(self, Style):
        Style.setObjectName("Style")
        Style.resize(613, 475)
        self.verticalLayoutWidget = QtWidgets.QWidget(Style)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 51, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Style)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(60, 20, 161, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Style)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(240, 20, 216, 31))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        self.groupBox = QtWidgets.QGroupBox(Style)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 301, 161))
        self.groupBox.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 180, 301, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 40, 160, 141))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.radioButton_4.setText("Python")
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_5.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.radioButton_5.setText("Ruby")
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_5.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.radioButton_6.setText("PHP")
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_5.addWidget(self.radioButton_6)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_5.addWidget(self.checkBox_3)
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.radioButton.setText("Python")
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_11.addWidget(self.radioButton)
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(10, 60, 161, 31))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget_14)
        self.radioButton_3.setText("Ruby")
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_14.addWidget(self.radioButton_3)
        self.verticalLayoutWidget_15 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_15)
        self.radioButton_2.setText("PHP")
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setAutoRepeat(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_15.addWidget(self.radioButton_2)
        self.verticalLayoutWidget_16 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_16.setGeometry(QtCore.QRect(10, 120, 161, 31))
        self.verticalLayoutWidget_16.setObjectName("verticalLayoutWidget_16")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_16)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_16)
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setTristate(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_16.addWidget(self.checkBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Style)
        self.groupBox_3.setGeometry(QtCore.QRect(320, 60, 281, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(300, 170, 301, 201))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 40, 160, 141))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.radioButton_10 = QtWidgets.QRadioButton(self.verticalLayoutWidget_7)
        self.radioButton_10.setText("Python")
        self.radioButton_10.setObjectName("radioButton_10")
        self.verticalLayout_7.addWidget(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.verticalLayoutWidget_7)
        self.radioButton_11.setText("Ruby")
        self.radioButton_11.setObjectName("radioButton_11")
        self.verticalLayout_7.addWidget(self.radioButton_11)
        self.radioButton_12 = QtWidgets.QRadioButton(self.verticalLayoutWidget_7)
        self.radioButton_12.setText("PHP")
        self.radioButton_12.setObjectName("radioButton_12")
        self.verticalLayout_7.addWidget(self.radioButton_12)
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_7.addWidget(self.checkBox_5)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 30, 241, 31))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayoutWidget_17 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_17.setGeometry(QtCore.QRect(20, 60, 241, 31))
        self.verticalLayoutWidget_17.setObjectName("verticalLayoutWidget_17")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_17)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_17)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_17.addWidget(self.pushButton)
        self.verticalLayoutWidget_18 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_18.setGeometry(QtCore.QRect(20, 100, 241, 31))
        self.verticalLayoutWidget_18.setObjectName("verticalLayoutWidget_18")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_18)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_18)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_18.addWidget(self.label_2)
        self.groupBox_5 = QtWidgets.QGroupBox(Style)
        self.groupBox_5.setGeometry(QtCore.QRect(320, 230, 281, 201))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_4.setGeometry(QtCore.QRect(0, 0, 92, 23))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayoutWidget_19 = QtWidgets.QWidget(self.groupBox_5)
        self.verticalLayoutWidget_19.setGeometry(QtCore.QRect(20, 30, 241, 31))
        self.verticalLayoutWidget_19.setObjectName("verticalLayoutWidget_19")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_19)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_19)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_19.addWidget(self.lineEdit)
        self.verticalLayoutWidget_20 = QtWidgets.QWidget(self.groupBox_5)
        self.verticalLayoutWidget_20.setGeometry(QtCore.QRect(20, 60, 241, 31))
        self.verticalLayoutWidget_20.setObjectName("verticalLayoutWidget_20")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_20)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_20)
        self.spinBox.setSingleStep(0)
        self.spinBox.setProperty("value", 50)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_20.addWidget(self.spinBox)
        self.verticalLayoutWidget_21 = QtWidgets.QWidget(self.groupBox_5)
        self.verticalLayoutWidget_21.setGeometry(QtCore.QRect(20, 90, 241, 31))
        self.verticalLayoutWidget_21.setObjectName("verticalLayoutWidget_21")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_21)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.verticalLayoutWidget_21)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 5, 22), QtCore.QTime(11, 8, 0)))
        self.dateTimeEdit.setTime(QtCore.QTime(11, 8, 0))
        self.dateTimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateTimeEdit.setCalendarPopup(False)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout_21.addWidget(self.dateTimeEdit)
        self.verticalLayoutWidget_23 = QtWidgets.QWidget(self.groupBox_5)
        self.verticalLayoutWidget_23.setGeometry(QtCore.QRect(20, 160, 171, 21))
        self.verticalLayoutWidget_23.setObjectName("verticalLayoutWidget_23")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_23)
        self.verticalLayout_23.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.verticalLayoutWidget_23)
        self.horizontalScrollBar.setProperty("value", 70)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalLayout_23.addWidget(self.horizontalScrollBar)
        self.verticalLayoutWidget_24 = QtWidgets.QWidget(self.groupBox_5)
        self.verticalLayoutWidget_24.setGeometry(QtCore.QRect(200, 130, 61, 52))
        self.verticalLayoutWidget_24.setObjectName("verticalLayoutWidget_24")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_24)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.dial = QtWidgets.QDial(self.verticalLayoutWidget_24)
        self.dial.setWrapping(False)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.verticalLayout_24.addWidget(self.dial)
        self.verticalLayoutWidget_22 = QtWidgets.QWidget(self.groupBox_5)
        self.verticalLayoutWidget_22.setGeometry(QtCore.QRect(20, 130, 171, 21))
        self.verticalLayoutWidget_22.setObjectName("verticalLayoutWidget_22")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_22)
        self.verticalLayout_22.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget_22)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setProperty("value", 45)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(0)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_22.addWidget(self.horizontalSlider)
        self.progressBar = QtWidgets.QProgressBar(Style)
        self.progressBar.setGeometry(QtCore.QRect(10, 440, 591, 23))
        self.progressBar.setProperty("value", 82)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(Style)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(460, 20, 135, 31))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.checkBox_6 = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_9.addWidget(self.checkBox_6)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(Style)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(10, 260, 301, 171))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_12)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_10.addWidget(self.tableWidget)
        self.tabWidget = QtWidgets.QTabWidget(Style)
        self.tabWidget.setGeometry(QtCore.QRect(10, 230, 301, 199))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.groupBox_5.raise_()
        self.progressBar.raise_()
        self.verticalLayoutWidget_11.raise_()
        self.verticalLayoutWidget_12.raise_()

        self.retranslateUi(Style)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Style)

    def retranslateUi(self, Style):
        _translate = QtCore.QCoreApplication.translate
        Style.setWindowTitle(_translate("Style", "Styles"))
        self.label.setText(_translate("Style", "<html><head/><body><p>Style : </p></body></html>"))
        self.comboBox.setItemText(0, _translate("Style", "Fusion"))
        self.checkBox.setToolTip(_translate("Style", "<html><head/><body><p><span style=\" text-decoration: underline;\">U</span>se style\'s</p></body></html>"))
        self.checkBox.setWhatsThis(_translate("Style", "<html><head/><body><p><span style=\" text-decoration: underline;\">U</span></p><p><br/></p></body></html>"))
        self.checkBox.setText(_translate("Style", "Use style\'s standard palette"))
        self.groupBox.setTitle(_translate("Style", "Group 1"))
        self.groupBox_2.setTitle(_translate("Style", "GroupBox"))
        self.checkBox_3.setText(_translate("Style", "Tri-state"))
        self.checkBox_2.setText(_translate("Style", "Tri-state"))
        self.groupBox_3.setTitle(_translate("Style", "Group 2"))
        self.groupBox_4.setTitle(_translate("Style", "GroupBox"))
        self.checkBox_5.setText(_translate("Style", "Tri-state"))
        self.pushButton_2.setText(_translate("Style", "Default Push Button"))
        self.pushButton.setText(_translate("Style", "Toggle Push Button"))
        self.label_2.setText(_translate("Style", "<html><head/><body><p align=\"center\">Flat Push Button</p></body></html>"))
        self.checkBox_4.setText(_translate("Style", "Group 3"))
        self.lineEdit.setText(_translate("Style", "ffffff"))
        self.dateTimeEdit.setDisplayFormat(_translate("Style", "d/M/yy h:mm "))
        self.checkBox_6.setToolTip(_translate("Style", "<html><head/><body><p><span style=\" text-decoration: underline;\">U</span>se style\'s</p></body></html>"))
        self.checkBox_6.setWhatsThis(_translate("Style", "<html><head/><body><p><span style=\" text-decoration: underline;\">U</span></p><p><br/></p></body></html>"))
        self.checkBox_6.setText(_translate("Style", "Disable widgets"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Style", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Style", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Style", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Style", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Style", "5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Style", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Style", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Style", "3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Style", "4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Style", "List"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Style", "Text Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Style = QtWidgets.QWidget()
    ui = Ui_Style()
    ui.setupUi(Style)
    Style.show()
    sys.exit(app.exec_())
