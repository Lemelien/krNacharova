from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget, QTableWidget,
                               QTableWidgetItem, QComboBox, QLabel)
from user_class import Connect, Employee, Task, Department

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Компания")
        self.resize(800, 600)

        # Основной виджет и layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.session = Connect.create_connection()

        # Фильтр
        self.filter_label = QLabel("Фильтр по отделу:")
        self.department_combo = QComboBox()
        self.department_combo.addItem("Все отделы", 0)
        
        for dep in self.session.query(Department).all():
            self.department_combo.addItem(dep.name, dep.id)
        self.department_combo.currentIndexChanged.connect(self.update_table)

        # Таблица сотрудников
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Имя", "Фамилия", "Должность", "Зарплата", "Отдел"])
        
        # Добавляем в layout
        self.layout.addWidget(self.filter_label)
        self.layout.addWidget(self.department_combo)
        self.layout.addWidget(self.table)
        
        self.update_table()

    def update_table(self):
        self.table.setRowCount(0)
        department_id = self.department_combo.currentData()

        if department_id == 0:
            employees = self.session.query(Employee).all()
        else:
            employees = self.session.query(Employee).filter(Employee.department_id == department_id).all()
        
        self.table.setRowCount(len(employees))
        for row, emp in enumerate(employees):
            self.table.setItem(row, 0, QTableWidgetItem(emp.first_name))
            self.table.setItem(row, 1, QTableWidgetItem(emp.last_name))
            self.table.setItem(row, 2, QTableWidgetItem(emp.position))
            self.table.setItem(row, 3, QTableWidgetItem(str(emp.salary)))
            self.table.setItem(row, 4, QTableWidgetItem(emp.department.name if emp.department else ""))
        
        self.table.resizeColumnsToContents()
