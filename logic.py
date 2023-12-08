from PyQt6.QtWidgets import *
from gui import *
import csv


class Logic(QMainWindow, Ui_MainWindow):
    """
    A class representing details for the logic
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_submit.setHidden(True)
        self.radio_john.setHidden(True)
        self.radio_jane.setHidden(True)
        self.button_check.clicked.connect(lambda: self.check())
        self.button_submit.clicked.connect(lambda: self.submit())

    def check(self) -> None:
        """
        Method to check the user's ID
        """
        try:
            user_id = str(self.user_input.text().strip())
            user = []
            with open('userchoices.csv', 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                next(reader)
                for rows in reader:
                    user.append(rows)

                for x in user:
                    for y in x:
                        if y == user_id:
                            raise IndexError
                        break
                self.button_submit.show()
                self.radio_john.show()
                self.radio_jane.show()
                self.label_error_message.setText('')
        except IndexError:
            self.label_error_message.setText(f'Error: User already voted.')

    def submit(self) -> None:
        """
        Method to submit vote to csv file
        """
        user_id = self.user_input.text()
        with open('userchoices.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if self.radio_john.isChecked():
                info = [user_id, "John"]
            elif self.radio_jane.isChecked():
                info = [user_id, 'Jane']
            writer.writerow(info)
        self.radio_jane.setAutoExclusive(False)
        self.radio_jane.setChecked(False)
        self.radio_jane.setAutoExclusive(True)
        self.radio_john.setAutoExclusive(False)
        self.radio_john.setChecked(False)
        self.radio_john.setAutoExclusive(True)
        self.button_submit.setHidden(True)
        self.radio_john.setHidden(True)
        self.radio_jane.setHidden(True)
        self.user_input.clear()
