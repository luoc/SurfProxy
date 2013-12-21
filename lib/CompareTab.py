__author__ = 'LuoCheng'
from CompareTabUI import Ui_Form
from PyQt4 import QtGui, QtCore
from compare import Compare

class QThreadCmp(QtCore.QThread):
    finish = QtCore.pyqtSignal(str)
    def __init__(self, surf_url_path, log_url_path):
        self.surf_url_path = surf_url_path
        self.log_url_path = log_url_path
        QtCore.QThread.__init__(self)

    def run(self):
        cmp = Compare(self.surf_url_path, self.log_url_path)
        cmp.do_compare()
        self.finish.emit(str(cmp))


class CompareWin(QtGui.QWidget):
    def __init__(self, parent=None):
        super(CompareWin, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.surf_url_path = None
        self.log_url_path = None
        self.threadcmp = None
        QtCore.QObject.connect(self.ui.btn_chooseurl, QtCore.SIGNAL("clicked()"), self.chooseUrlFile)
        QtCore.QObject.connect(self.ui.btn_chooselog, QtCore.SIGNAL("clicked()"), self.chooseLogFile)

    def chooseUrlFile(self):
        fd = QtGui.QFileDialog(self)
        self.surf_url_path = unicode(fd.getOpenFileName())
        self.ui.lineEdit_urlpath.setText(self.surf_url_path)
        self.compare()

    def chooseLogFile(self):
        fd = QtGui.QFileDialog(self)
        self.log_url_path = unicode(fd.getOpenFileName())
        self.ui.lineEdit_logpath.setText(self.log_url_path)
        self.compare()

    def compare(self):
        if self.log_url_path and self.surf_url_path:
            self.threadcmp = QThreadCmp(self.surf_url_path, self.log_url_path)
            self.threadcmp.finish.connect(self.showResult)
            self.threadcmp.start()
            self.surf_url_path = None
            self.log_url_path = None
            self.ui.lineEdit_urlpath.clear()
            self.ui.lineEdit_logpath.clear()

    def showResult(self, result):
        self.ui.textEdit.setText(result)


