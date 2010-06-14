#!/usr/bin/env python
#Copyright (c) 2010, Thomas H. Chace

import sys

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
        self.webpage = QWebPage(self.webkit)
        self.tbar = QToolBar(self.widget)
        self.window.resize(350, 500)
        self.window.setWindowTitle("Relax Twitter")
        self.window.setCentralWidget(self.widget)

        self.tbar = QToolBar(self.widget)

        self.actionReload = QAction(self.window)
        self.actionReload.setIcon(QIcon.fromTheme("reload"))
        self.actionReload.setObjectName("actionReload")
        self.actionReload.setIconText(QApplication.translate("MainWindow", "Reload", None, QApplication.UnicodeUTF8))

        self.actionBack = QAction(self.window)
        self.actionBack.setIcon(QIcon.fromTheme("go-previous"))
        self.actionBack.setObjectName("actionBack")

        self.actionHome = QAction(self.window)
        self.actionHome.setIcon(QIcon.fromTheme("go-home"))
        self.actionHome.setObjectName("actionHome")

        self.actionForward = QAction(self.window)
        self.actionForward.setIcon(QIcon.fromTheme("go-next"))
        self.actionForward.setObjectName("actionForward")

        self.tbar.addAction(self.actionReload)
        self.tbar.addAction(self.actionBack)
        self.tbar.addAction(self.actionHome)
        self.tbar.addAction(self.actionForward)

        self.layout = QVBoxLayout(self.widget)
        self.layout.setMargin(0)

        self.progress = QProgressBar()
        self.progress.setTextVisible(False)

        self.layout.addWidget(self.webkit)
        self.layout.addWidget(self.tbar)
        self.layout.addWidget(self.progress)

        self.webpage.setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        self.webkit.load(QUrl("https://mobile.twitter.com/session/new"))

        QObject.connect(self.actionReload, SIGNAL("triggered()"), self.webkit, SLOT("reload()")) # Reloads web page upon hitting reload
        QObject.connect(self.actionBack, SIGNAL("triggered()"), self.webkit, SLOT("back()")) # Goes Back in history upon clicking back
        QObject.connect(self.actionForward, SIGNAL("triggered()"), self.webkit, SLOT("forward()")) # Goes next upon clicking next
        QObject.connect(self.actionHome, SIGNAL("triggered()"), self.goHome) # Goes back to twitter
        QObject.connect(self.actionReload, SIGNAL("triggered()"), self.webkit, SLOT("reload()")) # Reloads web page upon hitting reload
        QObject.connect(self.webkit, SIGNAL("urlChanged (const QUrl&)"), self.urlChanged)
        QObject.connect(self.webkit, SIGNAL("loadProgress (int)"), self.loadProgress) # Tracks progress for progressbar

    def urlChanged(self, const):
        url = const.toString()
        url = str(url)
        if url.index("twitter.com"):
            pass
        else:
            print url

    def goHome(self):
        self.webkit.load(QUrl("https://mobile.twitter.com/"))

    def loadProgress(self, int):
        if int == 100:
            self.progress.setValue(0)
            self.progress.hide()
        else:
            self.progress.show()
            self.progress.setValue(int)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QCoreApplication.setOrganizationName("RelaxOS")
    QCoreApplication.setOrganizationDomain("http://thomaschace.ath.cx")
    QCoreApplication.setApplicationName("Relax Twitter")
    QCoreApplication.setApplicationVersion("0.1.0")
    twitter = Twitter()
    app.exec_()
    sys.exit()
