import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QListWidgetItem
from PySide6.QtCore import QObject, QEvent, Qt

from ui_EmojiKitchen import Ui_MainWindow
from ui_EmojiList import Ui_Dialog

test_pool_1 = ["😀", "😂", "😍", "🤔", "😎", "😭", "🎉", "👍", "👎", "🎉","😀", "😂", "🥰", "😎", "🤔", "😭", "😡"]
test_pool_2 = ["😀", "😂", "😍", "🤔", "😎", "😭", "😡", "👍", "👎", "😡","🍕", "🚗", "🔥", "✨", "❤️", "🍔", "⚽"]

class ClickFilter(QObject):
    def __init__(self, destination_func, emoji_list, parent=None):
        super().__init__(parent)
        self.destination_func = destination_func
        self.emoji_list = emoji_list

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
             self.destination_func(obj, self.emoji_list)
             return True
        return super().eventFilter(obj, event)
            
    

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.lineEdit_1.setCursor(Qt.PointingHandCursor)
        self.lineEdit_2.setCursor(Qt.PointingHandCursor)

        self.click_filter_1 = ClickFilter(self.open_emoji_list, test_pool_1, self)
        self.click_filter_2 = ClickFilter(self.open_emoji_list, test_pool_2, self)

        self.lineEdit_1.installEventFilter(self.click_filter_1)
        self.lineEdit_2.installEventFilter(self.click_filter_2)
    
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

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()