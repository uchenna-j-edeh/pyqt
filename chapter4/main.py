import sys
import argparse
import pandas as pd

from PySide2.QtCore import QDateTime, QTimeZone
from PySide2.QtWidgets import QApplication
from qmain_window import MainWindow
from main_widget import widget

def transform_date(utc, timezone=None):
    utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
    new_date = QDateTime().fromString(utc, utc_fmt)
    if timezone:
        new_date.setTimeZone(timezone)
    return new_date


def read_data(fname):
    # Read the CSV content
    df = pd.read_csv(fname)

    # Remove wrong magnitudes
    df = df.drop(df[df.mag < 0].index)
    magnitudes = df["mag"]

    # My local timezone
    timezone = QTimeZone(b"Europe/Berlin")

    # Get timestamp transformed to our timezone
    times = df["time"].apply(lambda x: transform_date(x, timezone))

    return times, magnitudes



if __name__ == "__main__":
    # options = argparse.ArgumentParser()
    # options.add_argument("-f", "--file", type=str, required=True)
    # args = options.parse_args()
    # data = read_data(args.file)
    data = read_data('/Users/uchenna/pyqt/tutorial/qt_tables/all_day_1.csv')
    
    app = QApplication(sys.argv)

    widget = widget(data)
    window = MainWindow(widget)
    window.show()

    sys.exit(app.exec_())