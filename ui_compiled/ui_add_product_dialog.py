

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QDialog,
    QDialogButtonBox, QFrame, QLabel, QLineEdit,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_ProdDialog(object):
    def setupUi(self, ProdDialog):
        if not ProdDialog.objectName():
            ProdDialog.setObjectName(u"ProdDialog")
        ProdDialog.resize(500, 400)
        ProdDialog.setStyleSheet(u"QDialog { background: #f5f7f9; }\n"
"QDialogButtonBox QPushButton { min-width: 84px; }")
        ProdDialog.setStyleSheet(u"QLineEdit, QSpinBox , QDateEdit{\n"
"padding : 8px 16px;\n"
"border-radius : 8px;\n"
"}\n"
"\n"
"QLabel{\n"
"font-size : 14px\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(ProdDialog)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(ProdDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignTop)

        self.numProdInput = QLineEdit(self.frame)
        self.numProdInput.setObjectName(u"numProdInput")

        self.verticalLayout.addWidget(self.numProdInput)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(ProdDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.designationInput = QLineEdit(self.frame_2)
        self.designationInput.setObjectName(u"designationInput")

        self.verticalLayout_2.addWidget(self.designationInput)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(ProdDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.stockInput = QSpinBox(self.frame_3)
        self.stockInput.setObjectName(u"stockInput")
        self.stockInput.setReadOnly(False)
        self.stockInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.stockInput.setMinimum(1)

        self.verticalLayout_3.addWidget(self.stockInput)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.buttonBox = QDialogButtonBox(ProdDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_5.addWidget(self.buttonBox)


        self.retranslateUi(ProdDialog)
        self.buttonBox.accepted.connect(ProdDialog.accept)
        self.buttonBox.rejected.connect(ProdDialog.reject)

        QMetaObject.connectSlotsByName(ProdDialog)

    def retranslateUi(self, ProdDialog):
        ProdDialog.setWindowTitle(QCoreApplication.translate("ProdDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ProdDialog", u"Num\u00e9ro du produit", None))
        self.numProdInput.setText("")
        self.numProdInput.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("ProdDialog", u"D\u00e9signation", None))
        self.designationInput.setPlaceholderText(QCoreApplication.translate("ProdDialog", u"Riz", None))
        self.label_3.setText(QCoreApplication.translate("ProdDialog", u"Stock", None))

