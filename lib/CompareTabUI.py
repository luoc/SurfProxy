# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\CompareTab.ui'
#
# Created: Sat Dec 21 14:13:04 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(405, 275)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        Form.setFont(font)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.groupBox_path = QtGui.QGroupBox(Form)
        self.groupBox_path.setGeometry(QtCore.QRect(10, 10, 381, 121))
        self.groupBox_path.setObjectName(_fromUtf8("groupBox_path"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_path)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 91))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(-1, 6, -1, 6)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_urlpath = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_urlpath.sizePolicy().hasHeightForWidth())
        self.lineEdit_urlpath.setSizePolicy(sizePolicy)
        self.lineEdit_urlpath.setReadOnly(True)
        self.lineEdit_urlpath.setObjectName(_fromUtf8("lineEdit_urlpath"))
        self.gridLayout.addWidget(self.lineEdit_urlpath, 0, 1, 1, 1)
        self.btn_chooseurl = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_chooseurl.sizePolicy().hasHeightForWidth())
        self.btn_chooseurl.setSizePolicy(sizePolicy)
        self.btn_chooseurl.setObjectName(_fromUtf8("btn_chooseurl"))
        self.gridLayout.addWidget(self.btn_chooseurl, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_logpath = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_logpath.sizePolicy().hasHeightForWidth())
        self.lineEdit_logpath.setSizePolicy(sizePolicy)
        self.lineEdit_logpath.setReadOnly(True)
        self.lineEdit_logpath.setObjectName(_fromUtf8("lineEdit_logpath"))
        self.gridLayout.addWidget(self.lineEdit_logpath, 1, 1, 1, 1)
        self.btn_chooselog = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_chooselog.sizePolicy().hasHeightForWidth())
        self.btn_chooselog.setSizePolicy(sizePolicy)
        self.btn_chooselog.setObjectName(_fromUtf8("btn_chooselog"))
        self.gridLayout.addWidget(self.btn_chooselog, 1, 2, 1, 1)
        self.groupBox_result = QtGui.QGroupBox(Form)
        self.groupBox_result.setGeometry(QtCore.QRect(10, 140, 381, 121))
        self.groupBox_result.setObjectName(_fromUtf8("groupBox_result"))
        self.textEdit = QtGui.QTextEdit(self.groupBox_result)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 361, 91))
        self.textEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "数据对比", None))
        self.groupBox_path.setTitle(_translate("Form", "数据对比选项", None))
        self.label.setText(_translate("Form", "拨测URL列表：", None))
        self.btn_chooseurl.setText(_translate("Form", "选  择..", None))
        self.label_2.setText(_translate("Form", "URL日志文件：", None))
        self.btn_chooselog.setText(_translate("Form", "选  择..", None))
        self.groupBox_result.setTitle(_translate("Form", "对比结果", None))

