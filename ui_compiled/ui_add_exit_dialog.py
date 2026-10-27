

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QDateEdit,
    QDialog, QDialogButtonBox, QFrame, QLabel,
    QLineEdit, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_ExitDialog(object):
    def setupUi(self, ExitDialog):
        if not ExitDialog.objectName():
            ExitDialog.setObjectName(u"ExitDialog")
        ExitDialog.resize(500, 400)
        ExitDialog.setStyleSheet(u"QDialog { background: #f5f7f9; }\n"
"QDialogButtonBox QPushButton { min-width: 84px; }")
        ExitDialog.setStyleSheet(u"QLineEdit, QSpinBox , QDateEdit{\n"
"padding : 8px 16px;\n"
"border-radius : 8px;\n"
"}\n"
"\n"
"QLabel{\n"
"font-size : 14px\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(ExitDialog)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(ExitDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignTop)

        self.numBonInput = QLineEdit(self.frame)
        self.numBonInput.setObjectName(u"numBonInput")

        self.verticalLayout.addWidget(self.numBonInput)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(ExitDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.numProdInput = QLineEdit(self.frame_2)
        self.numProdInput.setObjectName(u"numProdInput")

        self.verticalLayout_2.addWidget(self.numProdInput)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(ExitDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.qteInput = QSpinBox(self.frame_3)
        self.qteInput.setObjectName(u"qteInput")
        self.qteInput.setReadOnly(False)
        self.qteInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.qteInput.setMinimum(1)

        self.verticalLayout_3.addWidget(self.qteInput)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(ExitDialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.dateInput = QDateEdit(self.frame_4)
        self.dateInput.setObjectName(u"dateInput")

        self.verticalLayout_4.addWidget(self.dateInput)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.buttonBox = QDialogButtonBox(ExitDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"background-color : #2d66e4;\n"
"font : bold;\n"
"border : none;\n"
"color:  white")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_5.addWidget(self.buttonBox)


        self.retranslateUi(ExitDialog)
        self.buttonBox.accepted.connect(ExitDialog.accept)
        self.buttonBox.rejected.connect(ExitDialog.reject)

        QMetaObject.connectSlotsByName(ExitDialog)

    def retranslateUi(self, ExitDialog):
        ExitDialog.setWindowTitle(QCoreApplication.translate("ExitDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ExitDialog", u"Num\u00e9ro du bon", None))
        self.numBonInput.setPlaceholderText(QCoreApplication.translate("ExitDialog", u"BS-0000", None))
        self.label_2.setText(QCoreApplication.translate("ExitDialog", u"Num\u00e9ro du produit", None))
        self.numProdInput.setPlaceholderText(QCoreApplication.translate("ExitDialog", u"PRD-0000", None))
        self.label_3.setText(QCoreApplication.translate("ExitDialog", u"Quantit\u00e9 de sortie", None))
        self.label_4.setText(QCoreApplication.translate("ExitDialog", u"Date", None))

