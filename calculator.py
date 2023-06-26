import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setGeometry(200, 200, 300, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.result_display = QLineEdit()
        self.layout.addWidget(self.result_display)

        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C", "⌫"
        ]

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        row = 0
        col = 0

        for button_text in self.buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.button_clicked)
            self.grid_layout.addWidget(button, row, col)
            col += 1

            if col > 3:
                col = 0
                row += 1

        self.result_display.setText("")
        self.equation = ""

    def button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                result = eval(self.equation)
                self.result_display.setText(str(result))
                self.equation = str(result)
            except Exception as e:
                self.result_display.setText("Error")
        elif text == "C":
            self.result_display.setText("")
            self.equation = ""
        elif text == "⌫":
            current_text = self.result_display.text()
            self.result_display.setText(current_text[:-1])
            self.equation = self.result_display.text()
        else:
            self.equation += text
            self.result_display.setText(self.equation)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
