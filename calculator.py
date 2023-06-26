import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(200, 200, 300, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.equation_label = QLabel()
        self.layout.addWidget(self.equation_label)

        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

        self.buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["←", "CE"],
        ]

        self.input_line = QLineEdit()
        self.input_line.setReadOnly(True)
        self.layout.addWidget(self.input_line)

        self.buttons_layout = QVBoxLayout()

        for row in self.buttons:
            row_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.handle_button_click)
                row_layout.addWidget(button)
            self.buttons_layout.addLayout(row_layout)

        self.layout.addLayout(self.buttons_layout)

        self.current_equation = ""
        self.current_result = None

    def handle_button_click(self):
        button = self.sender()
        button_text = button.text()

        if button_text == "=":
            self.calculate_result()
        elif button_text == "C":
            self.clear_input()
        elif button_text == "CE":
            self.clear_all()
        else:
            self.add_to_input(button_text)

    def add_to_input(self, text):
        self.current_equation += text
        self.input_line.setText(self.current_equation)

    def calculate_result(self):
        try:
            self.current_result = eval(self.current_equation)
            self.result_label.setText(f"Result: {self.current_result}")
        except Exception as e:
            self.result_label.setText("Error")
            print(e)

        self.current_equation = ""
        self.input_line.clear()

    def clear_input(self):
        self.current_equation = self.current_equation[:-1]
        self.input_line.setText(self.current_equation)

    def clear_all(self):
        self.current_equation = ""
        self.current_result = None
        self.input_line.clear()
        self.result_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())
