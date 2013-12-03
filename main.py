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

class SurfWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #TODO: absolute path
        self._ini = 'surf.ini'
        self.cfg = None
        self.user = None
        self.pwd = None
        self.srf = None
        self.fpath = None
        self.step = 0
        self.timer = QtCore.QBasicTimer()
        QtCore.QObject.connect(self.ui.btn_choose, QtCore.SIGNAL("clicked()"), self.chooseUrlFile)
        QtCore.QObject.connect(self.ui.btn_start, QtCore.SIGNAL("clicked()"), self.surf)
        QtCore.QObject.connect(self.ui.lineEdit_user, QtCore.SIGNAL("editingFinished()"), self.setBtn)
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
        self.srf = surf.Surf(self.fpath, '119.254.227.62', self.user, self.pwd)
        self.ui.progressBar.setMaximum(self.srf.total_url)
        self.ui.progressBar.reset()
        t = self.refreshThread(self)
        t.start(QtCore.QThread.HighPriority)
        self.srf.start()
        self.popSuccess()

    class refreshThread(QtCore.QThread):
        def __init__(self, main):
            QtCore.QThread.__init__(self)
            self.main = main
        def run(self):
            t = self.main.srf.total_url
            while True:
                s = len(self.main.srf.logs['success'])
                f = len(self.main.srf.logs['failed'])
                self.main.ui.progressBar.setValue(s+f)
                QtCore.QThread.msleep(70)
                if t >= s+f:
                    break

    def timerEvent(self, event):
        t = self.srf.total_url
        s = len(self.srf.logs['success'])
        f = len(self.srf.logs['failed'])
        self.ui.progressBar.setValue(s+f)
        if t >= s+f:
            self.timer.stop()
        #while True:
        #    s = len(self.srf.logs['success'])
        #    f = len(self.srf.logs['failed'])
        #    self.ui.progressBar.setValue(s+f)
        #    if t >= s+f:
        #        break

    def popSuccess(self):
        msg = QtGui.QMessageBox(self)
        msg.setText(_translate('拨测结束，请查看日志'))
        msg.setWindowTitle(_translate('代理拨测专用'))
        msg.setStandardButtons(QtGui.QMessageBox.Ok|QtGui.QMessageBox.Close)
        msg.setInformativeText(_translate('现在打开日志文件？'))
        msg.exec_()
        response = msg.clickedButton().text()
        if response == 'OK':
            os.startfile(self.srf.fname)

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

