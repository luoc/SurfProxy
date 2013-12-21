

from PyQt4 import QtGui
from MainWinUI import Ui_Dialog

class MainWin(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)