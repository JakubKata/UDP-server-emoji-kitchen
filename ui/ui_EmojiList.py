# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EmojiList.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QListView, QListWidget,
    QListWidgetItem, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget_emoji_list = QListWidget(Dialog)
        self.listWidget_emoji_list.setObjectName(u"listWidget_emoji_list")
        font = QFont()
        font.setPointSize(36)
        self.listWidget_emoji_list.setFont(font)
        self.listWidget_emoji_list.setResizeMode(QListView.ResizeMode.Adjust)
        self.listWidget_emoji_list.setSpacing(10)
        self.listWidget_emoji_list.setViewMode(QListView.ViewMode.IconMode)

        self.verticalLayout.addWidget(self.listWidget_emoji_list)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

