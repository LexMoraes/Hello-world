import sys

import controlers
import main_window
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        self.nomes = []
        super(MainWindow, self).__init__(parent=parent)
        self.setWindowTitle('Tela principal')
        self.setupUi(self)
        # self.pushButtonSalvar.clicked.connect(self.on_click_save)

    def on_click_save(self):
        if self.lineEditNome.text() != "":
            self.nomes.append(self.lineEditNome.text())
            self.lineEditNome.setText("")
            print(self.nomes)

    def populate_table(self):
        self.tableWidgetNomes.setRowCount(len(self.nomes))
        for index, n in enumerate(self.nomes):
            item = QtWidgets.QTableWidgetItem()
            item.setText(n)
            self.tableWidgetNomes.setItem(index, 0, item)


app = QtWidgets.QApplication(sys.argv)
window = controlers.MainWindow
window.show()
sys.exit(app.exec_())
