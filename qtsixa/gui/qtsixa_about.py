#!/usr/bin/env python2
# -*- coding: utf-8 -*-


# Imports
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
import ui_qtsixa_aboutw


class AboutW(QDialog, ui_qtsixa_aboutw.Ui_AboutW):
    def __init__(self, *args):
        QDialog.__init__(self, *args)
        self.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/qtsixa.png"))


