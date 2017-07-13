import PyQt5
import sys

from PyQt5.QtWidgets import *



class Example(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QBoxLayout(QBoxLayout.Down, self)

        self.label1 = QLabel('Программа: Бьют ли друг друга фигуры? \n\nВыберите фигуру:', self)
        layout.addWidget(self.label1)

        self.combo = QComboBox(self)
        self.combo.addItems(["Пешка", "Конь", "Ладья", "Слон", "Ферзь", "Король"])
        layout.addWidget(self.combo)

        self.label2 = QLabel('Введите координаты расположения первой фигуры: ', self)
        layout.addWidget(self.label2)

        self.line1 = QLineEdit("", self)
        self.line1.setPlaceholderText("Например: a6")
        layout.addWidget(self.line1)

        self.label3 = QLabel('Введите координаты расположения второй фигуры: ', self)
        layout.addWidget(self.label3)

        self.line2 = QLineEdit("", self)
        self.line2.setPlaceholderText("Например: b5")
        layout.addWidget(self.line2)

        self.qbut = QPushButton('Проверить', self)
        self.qbut.clicked.connect(self.myfunc)
        layout.addWidget(self.qbut)

        self.label4 = QLabel('Результат: ', self)
        layout.addWidget(self.label4)

        self.line3 = QLineEdit("", self)
        self.line3.setPlaceholderText("Окно вывода!")
        layout.addWidget(self.line3)


        self.setWindowTitle('MyChess')
        self.show()


    def myfunc(self):

        def func0(a, b):  # пешка#
            if abs((ord(str(a[0])) - 96) - (ord(str(b[0])) - 96)) * abs(int(a[1]) - int(b[1])) == 1:
                return str("Бьют!")
            else:
                return str("Не бьют!")

        def func1(a, b):  # конь#
            if abs((ord(str(a[0])) - 96) - (ord(str(b[0])) - 96)) * abs(int(a[1]) - int(b[1])) == 2:
                return str("Бьют!")
            else:
                return str("Не бьют!")

        def func2(a, b):  # ладья#
            if a[0] == b[0] or a[1] == b[1]:
                return str("Бьют!")
            else:
                return str("Не бьют!")

        def func3(a, b):  # slon#
            if abs((ord(str(a[0])) - 96) - (ord(str(b[0])) - 96)) == abs(int(a[1]) - int(b[1])):
                return str("Бьют!")
            else:
                return str("Не бьют!")

        def func4(a, b):  # ferz-dama#
            if abs((ord(str(a[0])) - 96) - (ord(str(b[0])) - 96)) == abs(int(a[1]) - int(b[1])) or (
                            a[0] == b[0] or a[1] == b[1]):
                return str("Бьют!")
            else:
                return str("Не бьют!")

        def func5(a, b):  # king#
            if abs((ord(str(a[0])) - 96) - (ord(str(b[0])) - 96)) * abs(int(a[1]) - int(b[1])) == 1 or abs(
                            (ord(str(a[0])) - 96) - (ord(str(b[0])) - 96)) + abs(int(a[1]) - int(b[1])) == 1:
                return str("Бьют!")
            else:
                return str("Не бьют!")

        a = str(self.line1.text())
        b = str(self.line2.text())
        self.line1.setText("")
        self.line2.setText("")

        try:
            if self.combo.currentIndex() == 0:
                c = func0(a, b)
                self.line3.setText(str(c))
            elif self.combo.currentIndex() == 1:
                c = func1(a, b)
                self.line3.setText(str(c))
            elif self.combo.currentIndex() == 2:
                c = func2(a, b)
                self.line3.setText(str(c))
            elif self.combo.currentIndex() == 3:
                c = func3(a, b)
                self.line3.setText(str(c))
            elif self.combo.currentIndex() == 4:
                c = func4(a, b)
                self.line3.setText(str(c))
            elif self.combo.currentIndex() == 5:
                c = func5(a, b)
                self.line3.setText(str(c))
        except:
            self.line3.setText("Wrong input!")
            self.line1.setText("")
            self.line2.setText("")


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())