import sys
# pip install pyqt5
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
# just change the name
from gui import Ui_MainWindow

# thu vien mo rong
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
import mysql.connector

timer = QTimer()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # the way app working
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.thread = {}

        # khai bao nut an
        self.uic.Button_start_1.clicked.connect(self.show_diagram)
        self.uic.Button_start_2.clicked.connect(self.start_worker)

        self.uic.Button_stop_1.clicked.connect(self.stop_update)

    def closeEvent(self, event):
        print("close")
        self.stop_update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            print("enter press")
            self.start_worker()

    def stop_update(self):
        timer.stop()

    def show_diagram(self):
        if self.uic.screen.isEmpty():
            self.uic.screen.addWidget(show_chart())
        elif self.uic.screen is not None:
            timer.start(2000)

    def start_worker(self):
        a = self.uic.lineEdit_1.text()
        self.thread[1] = ThreadClass(index=1, number=a)
        self.thread[1].start()
        self.thread[1].signal.connect(self.stop_worker)
        self.uic.Button_start_2.setEnabled(False)

    def stop_worker(self):
        self.thread[1].stop()
        self.uic.Button_start_2.setEnabled(True)

class show_chart(FigureCanvasQTAgg):
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)

        timer.timeout.connect(self.loop)
        timer.start(2000)

        plt.ion()
    def loop(self):
        db = mysql.connector.connect(user='root', password='1234',
                                     host='127.0.0.1', database='new_database')
        # lenh chay
        code_8 = 'SELECT name,km FROM distance'
        # lệnh chạy code
        mycursor = db.cursor()
        mycursor.execute(code_8)  # make database
        result = mycursor.fetchall()

        datas = (result[0][0], result[1][0], result[2][0], result[3][0], result[4][0])
        datas1 = (result[0][1], result[1][1], result[2][1], result[3][1], result[4][1])
        explode = (0.2, 0.1, 0, 0, 0)
        print("label: ", datas)
        print("data: ", datas1)

        self.ax.clear()
        self.ax.pie(datas1, labels=datas, autopct='%1.2f%%', explode=explode,
               shadow=True, startangle=90)  # , explode=explode

class ThreadClass(QThread):
    signal = pyqtSignal()

    def __init__(self, index=0, number=0):
        super().__init__()
        self.index = index
        self.number = number

    def run(self):
        print('Starting thread...', self.index)

        db = mysql.connector.connect(user='root', password='1234',
                                     host='127.0.0.1', database='new_database')
        # lenh chay
        sql = "UPDATE `new_database`.`distance` SET `km` = %s WHERE (`ID` = %s);"
        val = (self.number, "A1")
        # lệnh chạy code
        mycursor = db.cursor()
        mycursor.execute(sql, val)  # make database
        db.commit()
        print(mycursor.rowcount, "record affected")
        self.signal.emit()

    def stop(self):
        print('Stopping thread...', self.index)
        self.terminate()

if __name__ == "__main__":
    # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())