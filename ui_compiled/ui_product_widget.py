

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_ProductWidget(object):
    def setupUi(self, ProductWidget):
        if not ProductWidget.objectName():
            ProductWidget.setObjectName(u"ProductWidget")
        ProductWidget.resize(783, 532)
        ProductWidget.setStyleSheet(u"\n"
"#middle{\n"
"border-radius : 8px;\n"
"border : 1px solid rgba(171, 173, 174, 40%); \n"
"background-color : #fff;\n"
"}\n"
"#description{\n"
"color : #abadae;\n"
"font-size : 10pt;\n"
"font-weight : 500;\n"
"}\n"
"\n"
"\n"
"#searchBar{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius : 8px;\n"
"padding : 50px;\n"
"border : 1px solid rgba(171, 173, 174, 40%);\n"
"\n"
"}\n"
" #pageName , #add {\n"
"font-weight : bold;\n"
"background : transparent;\n"
"}\n"
"QPushButton , QComboBox{\n"
"padding : 8px 16px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(ProductWidget)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchBar = QWidget(ProductWidget)
        self.searchBar.setObjectName(u"searchBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy)
        self.searchBar.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.searchBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.searchBar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pageName = QLabel(self.frame_2)
        self.pageName.setObjectName(u"pageName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pageName.sizePolicy().hasHeightForWidth())
        self.pageName.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.pageName.setFont(font)
        self.pageName.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pageName)

        self.description = QLabel(self.frame_2)
        self.description.setObjectName(u"description")

        self.verticalLayout_3.addWidget(self.description)


        self.horizontalLayout.addWidget(self.frame_2)

        self.add = QFrame(self.searchBar)
        self.add.setObjectName(u"add")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy2)
        self.add.setStyleSheet(u"")
        self.add.setFrameShape(QFrame.Shape.StyledPanel)
        self.add.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.add)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(self.add)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setStyleSheet(u"QPushButton { background-color : #0d6efd;\n"
"color : #ffffff;\n"
"border : none;\n"
"border-radius : 8px;\n"
"font : bold;\n"
"padding : 12px; }\n"
"QPushButton:hover { background-color : #0b5ed7; }\n"
"QPushButton:pressed { background-color : #0a58ca; }")
        icon = QIcon()
        icon.addFile(u":/icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAdd.setIcon(icon)
        self.btnAdd.setIconSize(QSize(17, 17))

        self.horizontalLayout_2.addWidget(self.btnAdd)


        self.horizontalLayout.addWidget(self.add)


        self.verticalLayout.addWidget(self.searchBar)

        self.middle = QWidget(ProductWidget)
        self.middle.setObjectName(u"middle")
        self.middle.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(self.middle)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.middle)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 20, -1, 20)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.searchInput = QLineEdit(self.frame)
        self.searchInput.setObjectName(u"searchInput")
        self.searchInput.setStyleSheet(u"padding : 8px 16px;\n"
"border : 1px solid rgba(171, 173, 174, 80%); background-color : #fff;")

        self.horizontalLayout_5.addWidget(self.searchInput)

        self.btnSearch = QPushButton(self.frame)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setStyleSheet(u"QPushButton { background-color : #0d6efd;\n"
"color : #ffffff;\n"
"border : none;\n"
"border-radius : 8px;\n"
"font : bold;\n"
"padding : 12px; }\n"
"QPushButton:hover { background-color : #0b5ed7; }\n"
"QPushButton:pressed { background-color : #0a58ca; }")
        icon1 = QIcon()
        icon1.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSearch.setIcon(icon1)
        self.btnSearch.setIconSize(QSize(17, 17))

        self.horizontalLayout_5.addWidget(self.btnSearch)

        self.btnEdit = QPushButton(self.frame)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setStyleSheet(u"QPushButton { background-color : #198754;\n"
"color : #ffffff;\n"
"border : none;\n"
"border-radius : 8px;\n"
"font : bold;\n"
"padding : 12px; }\n"
"QPushButton:hover { background-color : #157347; }\n"
"QPushButton:pressed { background-color : #146c43; }")
        icon2 = QIcon()
        icon2.addFile(u":/icons/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEdit.setIcon(icon2)
        self.btnEdit.setIconSize(QSize(17, 17))

        self.horizontalLayout_5.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.frame)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setStyleSheet(u"QPushButton { background-color : #dc3545;\n"
"color : #ffffff;\n"
"border : none;\n"
"border-radius : 8px;\n"
"font : bold;\n"
"padding : 12px; }\n"
"QPushButton:hover { background-color : #bb2d3e; }\n"
"QPushButton:pressed { background-color : #b02a37; }")
        icon3 = QIcon()
        icon3.addFile(u":/icons/trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDelete.setIcon(icon3)
        self.btnDelete.setIconSize(QSize(17, 17))

        self.horizontalLayout_5.addWidget(self.btnDelete)


        self.verticalLayout_2.addWidget(self.frame)

        self.productTable = QTableWidget(self.middle)
        if (self.productTable.columnCount() < 3):
            self.productTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.productTable.setObjectName(u"productTable")
        self.productTable.setStyleSheet(u"")
        self.productTable.setAlternatingRowColors(True)
        self.productTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.productTable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.productTable)


        self.verticalLayout.addWidget(self.middle)


        self.retranslateUi(ProductWidget)

        QMetaObject.connectSlotsByName(ProductWidget)

    def retranslateUi(self, ProductWidget):
        ProductWidget.setWindowTitle(QCoreApplication.translate("ProductWidget", u"Form", None))
        self.pageName.setText(QCoreApplication.translate("ProductWidget", u"Gestion et listage des produits", None))
        self.description.setText(QCoreApplication.translate("ProductWidget", u"Consultez les \u00e9quipements disponibles et suivez les quantit\u00e9s en stock en temps r\u00e9el", None))
        self.btnAdd.setText(QCoreApplication.translate("ProductWidget", u"Ajouter un produit", None))
        self.label_2.setText(QCoreApplication.translate("ProductWidget", u"Filtrer par :", None))
        self.searchInput.setPlaceholderText(QCoreApplication.translate("ProductWidget", u"Num\u00e9ro du produit ou designation", None))
        self.btnSearch.setText(QCoreApplication.translate("ProductWidget", u"Recherche", None))
        self.btnEdit.setText(QCoreApplication.translate("ProductWidget", u"Modifier", None))
        self.btnDelete.setText(QCoreApplication.translate("ProductWidget", u"Supprimer", None))
        ___qtablewidgetitem = self.productTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ProductWidget", u"N\u00b0 Produit", None))
        ___qtablewidgetitem1 = self.productTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ProductWidget", u"Designation", None))
        ___qtablewidgetitem2 = self.productTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ProductWidget", u"Stock", None))

