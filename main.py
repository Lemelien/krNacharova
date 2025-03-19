from PySide6.QtWidgets import QApplication
from main_window import MainWindow

# Запуск приложения
app = QApplication([])
window = MainWindow()
window.show()
app.exec()