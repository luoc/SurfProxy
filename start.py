
import sys
sys.path.append('lib')
from PyQt4 import QtGui
from MainWin import MainWin


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainwindows = MainWin()
    mainwindows.show()
    sys.exit(app.exec_())
