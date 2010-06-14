#!/usr/bin/env python
#Copyright (c) 2010, Thomas H. Chace

import sys, time

# PySide is preferred because it is directly from Nokia,
# but they aren't as common as PyQt4 - both have the same syntax
# so it doesn't matter, but PySide is preferred.
try:
    from PySide.QtCore import *
    from PySide.QtGui import *
    from PySide.QtWebKit import *
except:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtWebKit import *

class Twitter:
    def __init__(self):
        self.window = QMainWindow()
        self.window.show()
        self.widget = QWidget()
        self.webkit = QWebView(self.widget)
        self.tbar = QToolBar(self.widget)
        self.window.resize(250, 500)
        self.window.setWindowTitle("Relax Twitter")
        self.window.setCentralWidget(self.widget)

        self.tbar = QToolBar(self.widget)

        self.actionReload = QAction(self.window)
        self.actionReload.setIcon(QIcon.fromTheme("reload"))
        self.actionReload.setObjectName("actionReload")
        self.actionReload.setIconText(QApplication.translate("MainWindow", "Reload", None, QApplication.UnicodeUTF8))
        self.tbar.addAction(self.actionReload)

        self.layout = QVBoxLayout(self.widget)
        self.layout.setMargin(0)

        self.layout.addWidget(self.webkit)
        self.layout.addWidget(self.tbar)

        self.webkit.load(QUrl("https://mobile.twitter.com/session/new"))

        QObject.connect(self.actionReload, SIGNAL("triggered()"), self.webkit, SLOT("reload()")) # Reloads web page upon hitting reload

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QCoreApplication.setOrganizationName("RelaxOS")
    QCoreApplication.setOrganizationDomain("http://thomaschace.ath.cx")
    QCoreApplication.setApplicationName("Relax Twitter")
    QCoreApplication.setApplicationVersion("0.1.0")
    twitter = Twitter()
    app.exec_()
    sys.exit()
