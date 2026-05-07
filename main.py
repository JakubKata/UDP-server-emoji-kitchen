import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QListWidgetItem
from PySide6.QtCore import QObject, QEvent, Qt
from PySide6.QtGui import QPixmap

from ui.ui_EmojiKitchen import Ui_MainWindow
from ui.ui_EmojiList import Ui_Dialog
from api.network import Network


class ClickFilter(QObject):
    def __init__(self, destination_func, emoji_list, parent=None):
        super().__init__(parent)
        self.destination_func = destination_func
        self.emoji_list = emoji_list

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            self.destination_func(obj, self.emoji_list())
            return True
        return super().eventFilter(obj, event)
            
    
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, network = None):
        super().__init__()

        self.network = network or Network()
        self.setupUi(self)

        self.lineEdit_1.setCursor(Qt.PointingHandCursor)
        self.lineEdit_2.setCursor(Qt.PointingHandCursor)

        self.click_filter_1 = ClickFilter(self.open_emoji_list, lambda: self.network.get_pool_1(), self)
        self.click_filter_2 = ClickFilter(self.open_emoji_list, lambda: self.network.get_pool_2(), self)

        self.lineEdit_1.installEventFilter(self.click_filter_1)
        self.lineEdit_2.installEventFilter(self.click_filter_2)

        self.lineEdit_1.textChanged.connect(lambda: self.emoji_changed(1))
        self.lineEdit_2.textChanged.connect(lambda: self.emoji_changed(2))

    def open_emoji_list(self, output_emoji, emoji_list):
        dialog = QDialog(self)
        ui_dialog = Ui_Dialog()
        ui_dialog.setupUi(dialog)

        for emoji in emoji_list:
            item = QListWidgetItem(emoji)
            ui_dialog.listWidget_emoji_list.addItem(item)

        def on_item_clicked(item):
            output_emoji.setText(item.text())
            dialog.accept()

        ui_dialog.listWidget_emoji_list.itemClicked.connect(on_item_clicked)

        dialog.exec()

    def emoji_changed(self, line_number):
        text_1 = self.lineEdit_1.text()
        text_2 = self.lineEdit_2.text()
        
        result = self.network.emoji_change(text_1, text_2, line_number)

        pixmap = QPixmap()
        pixmap.loadFromData(result)
        self.label_picture.setScaledContents(True)
        self.label_picture.setPixmap(pixmap)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()