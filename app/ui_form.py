# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
                               QMainWindow, QSizePolicy, QVBoxLayout, QWidget)


class Ui_ChristmasCountdown(object):
    def setupUi(self, ChristmasCountdown):
        if not ChristmasCountdown.objectName():
            ChristmasCountdown.setObjectName(u"ChirstmasCountdown")
        ChristmasCountdown.setEnabled(True)
        ChristmasCountdown.resize(800, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChristmasCountdown.sizePolicy().hasHeightForWidth())
        ChristmasCountdown.setSizePolicy(sizePolicy)
        ChristmasCountdown.setMaximumSize(QSize(800, 800))
        icon = QIcon()
        icon.addFile(u"img/ornament_red.png", QSize(), QIcon.Normal, QIcon.Off)
        ChristmasCountdown.setWindowIcon(icon)
        ChristmasCountdown.setAutoFillBackground(False)
        ChristmasCountdown.setStyleSheet(
            u"QMainWindow {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.666667, y2:1, stop:0 rgba(0, 123, 187, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QWidget(ChristmasCountdown)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, -1, -1)
        self.countdown_img_left = QLabel(self.centralwidget)
        self.countdown_img_left.setObjectName(u"countdown_img_left")
        sizePolicy.setHeightForWidth(self.countdown_img_left.sizePolicy().hasHeightForWidth())
        self.countdown_img_left.setSizePolicy(sizePolicy)
        self.countdown_img_left.setMaximumSize(QSize(100, 100))
        self.countdown_img_left.setPixmap(QPixmap(u"img/snowman.png"))
        self.countdown_img_left.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.countdown_img_left)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.countdown_label_top = QLabel(self.centralwidget)
        self.countdown_label_top.setObjectName(u"countdown_label_top")
        self.countdown_label_top.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamilies([u"FontAwesome"])
        font.setPointSize(20)
        font.setBold(True)
        self.countdown_label_top.setFont(font)
        self.countdown_label_top.setStyleSheet(u"")
        self.countdown_label_top.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.countdown_label_top, 0, Qt.AlignHCenter)

        self.countdown_label_bottom = QLabel(self.centralwidget)
        self.countdown_label_bottom.setObjectName(u"countdown_label_bottom")
        font1 = QFont()
        font1.setPointSize(20)
        self.countdown_label_bottom.setFont(font1)

        self.verticalLayout_2.addWidget(self.countdown_label_bottom, 0, Qt.AlignHCenter)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.countdown_img_right = QLabel(self.centralwidget)
        self.countdown_img_right.setObjectName(u"countdown_img_right")
        self.countdown_img_right.setMaximumSize(QSize(100, 100))
        self.countdown_img_right.setPixmap(QPixmap(u"img/hat.png"))
        self.countdown_img_right.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.countdown_img_right)

        self.mainLayout.addLayout(self.horizontalLayout_2)

        self.tree = QLabel(self.centralwidget)
        self.tree.setObjectName(u"tree")
        self.tree.setPixmap(QPixmap(u"img/christmas-tree.png"))
        self.tree.setScaledContents(False)

        self.mainLayout.addWidget(self.tree, 0, Qt.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(200, -1, 200, -1)
        self.blue_present = QLabel(self.centralwidget)
        self.blue_present.setObjectName(u"blue_present")
        self.blue_present.setMaximumSize(QSize(100, 100))
        self.blue_present.setPixmap(QPixmap(u"img/blue_gift.png"))
        self.blue_present.setScaledContents(True)

        self.horizontalLayout.addWidget(self.blue_present)

        self.red_present = QLabel(self.centralwidget)
        self.red_present.setObjectName(u"red_present")
        self.red_present.setMaximumSize(QSize(100, 100))
        self.red_present.setPixmap(QPixmap(u"img/red_gift.png"))
        self.red_present.setScaledContents(True)

        self.horizontalLayout.addWidget(self.red_present)

        self.green_present = QLabel(self.centralwidget)
        self.green_present.setObjectName(u"green_present")
        self.green_present.setMaximumSize(QSize(100, 100))
        self.green_present.setPixmap(QPixmap(u"img/green_gift.png"))
        self.green_present.setScaledContents(True)

        self.horizontalLayout.addWidget(self.green_present)

        self.mainLayout.addLayout(self.horizontalLayout)

        ChristmasCountdown.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChristmasCountdown)

        QMetaObject.connectSlotsByName(ChristmasCountdown)

    # setupUi

    def retranslateUi(self, ChristmasCountdown):
        ChristmasCountdown.setWindowTitle(
            QCoreApplication.translate("ChristmasCountdown", u"Christmas Countdown", None))
        self.countdown_img_left.setText("")
        self.countdown_label_top.setText(
            QCoreApplication.translate("ChristmasCountdown", u"Time Remaining Until Chirstmas", None))
        self.countdown_label_bottom.setText(
            QCoreApplication.translate("ChristmasCountdown", u"99 Hours 99 Minutes 99 Seconds", None))
        self.countdown_img_right.setText("")
        self.tree.setText("")
        self.blue_present.setText("")
        self.red_present.setText("")
        self.green_present.setText("")
    # retranslateUi
