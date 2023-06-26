from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Калькулятор")
        self.setFixedSize(300, 400)

        self.layout = QVBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setReadOnly(True)
        self.layout.addWidget(self.input_field)

        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'CA', 'Backspace'
        ]

        self.button_grid = QWidget()
        self.button_grid.setLayout(self.layout)

        self.button_grid_layout = QVBoxLayout()

        button_row_layout = None
        for index, button_text in enumerate(self.buttons):
            if index % 4 == 0:
                button_row_layout = QVBoxLayout()
                self.button_grid_layout.addLayout(button_row_layout)
            button = QPushButton(button_text)
            button.clicked.connect(self.button_click)
            button_row_layout.addWidget(button)

        self.layout.addLayout(self.button_grid_layout)

        self.setLayout(self.layout)

        self.equation = ""

    def button_click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                result = eval(self.equation)
                self.input_field.setText(str(result))
                self.equation = str(result)
            except ZeroDivisionError:
                self.input_field.setText("Ошибка: деление на ноль")
                self.equation = ""
        elif text == "CA":
            self.input_field.clear()
            self.equation = ""
        elif text == "Backspace":
            self.equation = self.equation[:-1]
        else:
            self.equation += text
            self.input_field.setText(self.equation)


if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()
