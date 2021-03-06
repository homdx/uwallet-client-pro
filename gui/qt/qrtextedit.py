# -*- coding: utf-8 -*-
from uwallet.i18n import _
from uwallet.plugins import run_hook
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from util import ButtonsTextEdit, MessageBoxMixin


class ShowQRTextEdit(ButtonsTextEdit):

    def __init__(self, text=None):
        ButtonsTextEdit.__init__(self, text)
        self.setReadOnly(1)
        # self.addButton(":icons/qrcode.png", self.qr_show, _("Show as QR code"))

        run_hook('show_text_edit', self)

    def qr_show(self):
        from qrcodewidget import QRDialog
        try:
            s = str(self.toPlainText())
        except:
            s = unicode(self.toPlainText())
        QRDialog(s,self.parent()).exec_()

    def contextMenuEvent(self, e):
        m = self.createStandardContextMenu()
        acs = m.actions()

        for ac in acs:
            t = ac.text()
            if "Undo" in t:
                ac.setText(_("Undo        Ctrl+Z"))
                continue
            if "Redo" in t:
                ac.setText(_("Redo        Ctrl+Y"))
                continue
            if "Cu&t" in t:
                ac.setText(_("Cut         Ctrl+X"))
                continue
            if "Copy" in t:
                ac.setText(_("Copy        Ctrl+C"))
                continue
            if "Paste" in t:
                ac.setText(_("Paste       Ctrl+V"))
                continue
            if "Delete" in t:
                ac.setText(_("Delete"))
                continue
            if "Select" in t:
                ac.setText(_("SelectAll   Ctrl+A"))
                continue
        # m.addAction(_("Show as QR code"), self.qr_show)
        m.exec_(e.globalPos())


class ScanQRTextEdit(ButtonsTextEdit, MessageBoxMixin):

    def __init__(self, text=""):
        ButtonsTextEdit.__init__(self, text)
        self.setReadOnly(0)
        button=self.addButton(":icons/ic_folder_pre.png", self.file_input, _("Read file"))
        button.setStyleSheet("QToolButton { border: none; hover {border: 1px;border-image:ic_folder_pre.png;} pressed {border: 1px} padding: 0px; }")
        # button=self.addButton(":icons/ic_qr_code.png", self.qr_input, _("Read QR code"))
        # button.setStyleSheet("QToolButton { border: none; hover {border: 1px} pressed {border: 1px} padding: 0px; }")
        run_hook('scan_text_edit', self)

    def file_input(self):
        fileName = unicode(QFileDialog.getOpenFileName(self, 'select file'))
        if not fileName:
            return
        with open(fileName, "r") as f:
            data = f.read()
        self.setText(data)

    def qr_input(self):
        from uwallet import qrscanner, get_config
        try:
            data = qrscanner.scan_qr(get_config())
        except BaseException as e:
            self.show_error(str(e))
            return ""
        if type(data) != str:
            return
        self.setText(data)
        return data

    def contextMenuEvent(self, e):
        m = self.createStandardContextMenu()

        acs = m.actions()
        for ac in acs:
            t = ac.text()
            if "Undo" in t:
                ac.setText(_("Undo        Ctrl+Z"))
                continue
            if "Redo" in t:
                ac.setText(_("Redo        Ctrl+Y"))
                continue
            if "Cu&t" in t:
                ac.setText(_("Cut         Ctrl+X"))
                continue
            if "Copy" in t:
                ac.setText(_("Copy        Ctrl+C"))
                continue
            if "Paste" in t:
                ac.setText(_("Paste       Ctrl+V"))
                continue
            if "Delete" in t:
                ac.setText(_("Delete"))
                continue
            if "Select" in t:
                ac.setText(_("SelectAll   Ctrl+A"))
                continue
        # m.addAction(_("Read QR code"), self.qr_input)
        m.exec_(e.globalPos())
