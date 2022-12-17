import datetime
import sys

from PyQt6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_form import Ui_ChristmasCountdown


class ChristmasCountdown(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ChristmasCountdown()
        self.ui.setupUi(self)

        self.setFixedSize(800, 800)

        # Update the countdown every second using a QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_countdown_label)
        self.timer.start(10)

    def update_countdown_label(self):
        # Get the current date and time
        now = datetime.datetime.now()

        # Calculate the difference between the current date and time and Christmas 2022
        christmas = datetime.datetime(2022, 12, 25)
        delta = christmas - now

        # Calculate the number of days, hours, minutes, and seconds until Christmas
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Display the countdown in a label
        if now < christmas:
            top_message = "Time Remaining Until Christmas"
            bottom_message = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
        else:
            top_message = "Merry Christmas"
            bottom_message = ""

        self.ui.countdown_label_top.setText(top_message)
        self.ui.countdown_label_bottom.setText(bottom_message)
        self.ui.countdown_label_top.show()
        self.ui.countdown_label_bottom.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ChristmasCountdown()
    widget.show()
    sys.exit(app.exec())
