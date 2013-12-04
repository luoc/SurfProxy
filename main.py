#coding:GB2312
__author__ = 'LuoCheng'
import sys
sys.path.append('lib')
import surf
import ConfigParser
import os
import threading
from PyQt4 import QtCore, QtGui
from UI import Ui_Form

def _translate(text):
    return unicode(text, 'gb2312', 'ignore')

class QthreadUI(QtCore.QThread):
    signal = QtCore.pyqtSignal(int)
    finish =  QtCore.pyqtSignal()
    def __init__(self, UI):
        QtCore.QThread.__init__(self)
        self.UI = UI

    def run(self):
        total_url = self.UI.surfs.total_url

        while True:
            success = len(self.UI.surfs.logs['success'])
            fails = len(self.UI.surfs.logs['failed'])
            self.signal.emit(success+fails)
            QtCore.QThread.msleep(50)
            if total_url == success + fails:
                break
        self.finish.emit()

class QThreadSurf(QtCore.QThread):
    def __init__(self, UI):
        QtCore.QThread.__init__(self)
        self.UI = UI

    def run(self):
        self.UI.surfs.start()



class SurfWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._ini = 'surf.ini'
        self.cfg = None
        self.user = None
        self.pwd = None
        self.surfs = None
        self.fpath = None
        QtCore.QObject.connect(self.ui.btn_choose, QtCore.SIGNAL("clicked()"), self.chooseUrlFile)
        QtCore.QObject.connect(self.ui.btn_start, QtCore.SIGNAL("clicked()"), self.surf)
        QtCore.QObject.connect(self.ui.lineEdit_user, QtCore.SIGNAL("editingFinished()"), self.setBtn)
        #create thread to refresh ui(progressbar)
        self.threadui = QthreadUI(self)
        self.threadui.signal.connect(self.QRefreshUI)
        self.threadui.finish.connect(self.QpopSuccess)
        self.getCfgInfo()

    def getCfgInfo(self): #get user name and password from surf.ini if exists.
        if os.path.exists(self._ini) and os.path.isfile(self._ini):
            self.cfg = ConfigParser.ConfigParser()
            self.cfg.read(self._ini)
            self.user = self.cfg.get('Account', 'User')
            self.pwd = self.cfg.get('Account', 'Password')
            self.ui.lineEdit_user.setText(self.user)
            self.ui.lineEdit_pwd.setText(self.pwd)

    def chooseUrlFile(self):
        fd = QtGui.QFileDialog(self)
        self.fpath = unicode(fd.getOpenFileName())
        self.ui.lineEdit_urlpath.setText(self.fpath)
        self.setBtn()

    def setBtn(self):
        if self.fpath and self.ui.lineEdit_user.text().length():
            self.ui.btn_start.setEnabled(True)
        else:
            self.ui.btn_start.setEnabled(False)

    def surf(self):
        self.user = str(self.ui.lineEdit_user.text())
        self.pwd = str(self.ui.lineEdit_pwd.text())
        self.surfs = surf.Surf(self.fpath, '119.254.227.62', self.user, self.pwd)
        self.ui.progressBar.setMaximum(self.surfs.total_url)
        self.ui.progressBar.reset()
        self.threadui.start()
        self.threadsurfs = QThreadSurf(self)
        self.threadsurfs.start()

    def QRefreshUI(self, step):
        self.ui.progressBar.setValue(step)

    def QpopSuccess(self):
        msg = QtGui.QMessageBox(self)
        msg.setText(_translate('拨测结束，请查看日志'))
        msg.setWindowTitle(_translate('代理拨测专用'))
        msg.setStandardButtons(QtGui.QMessageBox.Ok|QtGui.QMessageBox.Close)
        msg.setInformativeText(_translate('现在打开日志文件？'))
        msg.exec_()
        response = msg.clickedButton().text()
        if response == 'OK':
            os.startfile(self.surfs.fname)

    def __del__(self):
        if not self.cfg:
            self.cfg = ConfigParser.ConfigParser()
            self.cfg.add_section('Account')
        self.user = self.ui.lineEdit_user.text()
        self.pwd = self.ui.lineEdit_pwd.text()
        self.cfg.set('Account', 'User', self.user)
        self.cfg.set('Account', 'Password', self.pwd)
        with open(self._ini, 'w') as f:
            self.cfg.write(f)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    surfbyproxy = SurfWin()
    surfbyproxy.show()
    sys.exit(app.exec_())

