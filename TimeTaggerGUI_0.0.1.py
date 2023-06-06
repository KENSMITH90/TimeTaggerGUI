# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TimeTaggerGUI_0.0.1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import TimeTagger
import pandas as pd
from pathlib import Path


def unit_conversion(pre_num, pre_unit: str):
    """
    To avoid float calculation, all the time unit variables are converted to the smallest unit
    unit_conversion take the number and its unit, convert its unit to ps (picoseconds), and return a new number
    :param pre_num: numeral part before unit conversion
    :param pre_unit: previous unit to be converted
    :return: an integer that represent time in picoseconds
    """
    # initialize variable and determine conversion factor
    factor = 1
    if pre_unit == "min":
        factor = 6e13
    elif pre_unit == "sec":
        factor = 1e12
    elif pre_unit == "ms":
        factor = 1e9
    elif pre_unit == "μs":
        factor = 1e6
    elif pre_unit == "ns":
        factor = 1e3
    # convert time to picoseconds and return the value
    converted_value = pre_num * factor
    return converted_value


class Ui_MainWindow(object):
    def __init__(self):
        # create class variables for instrument control
        self.bin_width = None
        self.total_time = None
        self.trail_num = None
        self.bin_num = None
        self.gap_time = 0
        self.start_channel = None
        self.click_channel = None
        self.data = None
        self.counts = None
        self.time_data = None


    def setupUi(self, MainWindow):

        # create main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.bin_num_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.bin_num_entry.setGeometry(QtCore.QRect(192, 126, 137, 22))
        self.bin_num_entry.setObjectName("bin_num_entry")
        self.bin_num_entry.setText("0")

        # define and connect start button to its function
        self.start_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_start())
        self.start_button.setGeometry(QtCore.QRect(240, 350, 291, 51))
        self.start_button.setObjectName("start_button")
        self.start_button.setEnabled(False)

        # define total time entry box
        self.total_time_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.total_time_entry.setGeometry(QtCore.QRect(192, 97, 137, 22))
        self.total_time_entry.setObjectName("total_time_entry")
        self.total_time_entry.setText("0")

        # define bin width entry box
        self.bin_width_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.bin_width_entry.setGeometry(QtCore.QRect(192, 155, 137, 22))
        self.bin_width_entry.setObjectName("bin_width_entry")
        self.bin_width_entry.setText("0")

        # define click channel label
        self.click_channel_label = QtWidgets.QLabel(self.centralwidget)
        self.click_channel_label.setGeometry(QtCore.QRect(421, 70, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.click_channel_label.setFont(font)
        self.click_channel_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.click_channel_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.click_channel_label.setLineWidth(3)
        self.click_channel_label.setTextFormat(QtCore.Qt.AutoText)
        self.click_channel_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.click_channel_label.setWordWrap(False)
        self.click_channel_label.setObjectName("click_channel_label")

        #define and set gap_time_entry
        self.gap_time_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.gap_time_entry.setGeometry(QtCore.QRect(192, 68, 137, 22))
        self.gap_time_entry.setObjectName("gap_time_entry")
        self.gap_time_entry.setText("0")

        # define gap time unit combo box
        self.gap_time_unit = QtWidgets.QComboBox(self.centralwidget)
        self.gap_time_unit.setGeometry(QtCore.QRect(336, 68, 52, 22))
        self.gap_time_unit.setObjectName("gap_time_unit")
        self.gap_time_unit.addItem("")
        self.gap_time_unit.addItem("")
        self.gap_time_unit.addItem("")
        self.gap_time_unit.addItem("")
        self.gap_time_unit.addItem("")
        self.gap_time_unit.addItem("")

        # define total time unit combo box
        self.total_time_unit = QtWidgets.QComboBox(self.centralwidget)
        self.total_time_unit.setGeometry(QtCore.QRect(336, 97, 52, 22))
        self.total_time_unit.setObjectName("total_time_unit")
        self.total_time_unit.addItem("")
        self.total_time_unit.addItem("")
        self.total_time_unit.addItem("")
        self.total_time_unit.addItem("")
        self.total_time_unit.addItem("")
        self.total_time_unit.addItem("")

        # define bin width unit combo box
        self.bin_width_unit = QtWidgets.QComboBox(self.centralwidget)
        self.bin_width_unit.setGeometry(QtCore.QRect(336, 155, 52, 22))
        self.bin_width_unit.setObjectName("bin_width_unit")
        self.bin_width_unit.addItem("")
        self.bin_width_unit.addItem("")
        self.bin_width_unit.addItem("")
        self.bin_width_unit.addItem("")
        self.bin_width_unit.addItem("")
        self.bin_width_unit.addItem("")

        # define start channel label
        self.start_channel_label = QtWidgets.QLabel(self.centralwidget)
        self.start_channel_label.setGeometry(QtCore.QRect(422, 41, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.start_channel_label.setFont(font)
        self.start_channel_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.start_channel_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.start_channel_label.setLineWidth(3)
        self.start_channel_label.setTextFormat(QtCore.Qt.AutoText)
        self.start_channel_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.start_channel_label.setWordWrap(False)
        self.start_channel_label.setObjectName("start_channel_label")

        # define start channel entry box
        self.start_channel_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.start_channel_entry.setGeometry(QtCore.QRect(550, 41, 137, 22))
        self.start_channel_entry.setObjectName("start_channel_entry")
        self.start_channel_entry.setText("0")

        # define click channel entry box
        self.click_channel_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.click_channel_entry.setGeometry(QtCore.QRect(550, 70, 137, 22))
        self.click_channel_entry.setObjectName("click_channel_entry")
        self.click_channel_entry.setText("0")

        # define number of trail entry box
        self.num_trail_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.num_trail_entry.setGeometry(QtCore.QRect(192, 39, 137, 22))
        self.num_trail_entry.setObjectName("num_trail_entry")
        self.num_trail_entry.setText("0")

        # define and connect save button to its function
        self.save_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_save())
        self.save_button.setGeometry(QtCore.QRect(240, 410, 291, 51))
        self.save_button.setObjectName("save_button")

        # define and connect confirm button to its function
        self.confirm_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda : self.press_confirm())
        self.confirm_button.setGeometry(QtCore.QRect(70, 270, 291, 51))
        self.confirm_button.setObjectName("confirm_button")

        # define and connect clear button to its function
        self.clear_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_clear())
        self.clear_button.setGeometry(QtCore.QRect(410, 270, 291, 51))
        self.clear_button.setObjectName("clear_button")

        # create a layout form
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(22, 42, 158, 130))
        self.layoutWidget.setObjectName("layoutWidget")
        # define layout as vertical
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # create trail_num_label
        self.trail_num_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.trail_num_label.setFont(font)
        self.trail_num_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.trail_num_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trail_num_label.setLineWidth(3)
        self.trail_num_label.setTextFormat(QtCore.Qt.AutoText)
        self.trail_num_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.trail_num_label.setWordWrap(False)
        self.trail_num_label.setObjectName("trail_num")
        self.verticalLayout.addWidget(self.trail_num_label)

        # create trail_gap_label
        self.trail_gap_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.trail_gap_label.setFont(font)
        self.trail_gap_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.trail_gap_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trail_gap_label.setLineWidth(3)
        self.trail_gap_label.setTextFormat(QtCore.Qt.AutoText)
        self.trail_gap_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.trail_gap_label.setWordWrap(False)
        self.trail_gap_label.setObjectName("trail_gap_label")
        self.verticalLayout.addWidget(self.trail_gap_label)

        # create total time label
        self.total_time_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.total_time_label.setFont(font)
        self.total_time_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.total_time_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.total_time_label.setLineWidth(3)
        self.total_time_label.setTextFormat(QtCore.Qt.AutoText)
        self.total_time_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.total_time_label.setWordWrap(False)
        self.total_time_label.setObjectName("total_time")
        self.verticalLayout.addWidget(self.total_time_label)

        # create number of bins label
        self.num_bin_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.num_bin_label.setFont(font)
        self.num_bin_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.num_bin_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.num_bin_label.setLineWidth(3)
        self.num_bin_label.setTextFormat(QtCore.Qt.AutoText)
        self.num_bin_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.num_bin_label.setWordWrap(False)
        self.num_bin_label.setObjectName("num_bin_label")
        self.verticalLayout.addWidget(self.num_bin_label)

        # create bin width label
        self.bin_width_label = QtWidgets.QLabel(self.layoutWidget)
        self.bin_width_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bin_width_label.setFont(font)
        self.bin_width_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bin_width_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bin_width_label.setLineWidth(3)
        self.bin_width_label.setTextFormat(QtCore.Qt.AutoText)
        self.bin_width_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bin_width_label.setWordWrap(False)
        self.bin_width_label.setObjectName("bin_width_label")
        self.verticalLayout.addWidget(self.bin_width_label)

        # define count_rate_label
        self.count_rate_label = QtWidgets.QLabel(self.centralwidget)
        self.count_rate_label.setGeometry(QtCore.QRect(440, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.count_rate_label.setFont(font)
        self.count_rate_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.count_rate_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.count_rate_label.setLineWidth(3)
        self.count_rate_label.setTextFormat(QtCore.Qt.AutoText)
        self.count_rate_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.count_rate_label.setWordWrap(False)
        self.count_rate_label.setObjectName("count_rate_label")

        # define count_rate entry
        self.count_rate_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.count_rate_entry.setGeometry(QtCore.QRect(550, 150, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.count_rate_entry.setFont(font)
        self.count_rate_entry.setText("")
        self.count_rate_entry.setObjectName("count_rate_entry")

        # generate a basic menubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # implement label, button, and combo box content
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def press_start(self):
        """
        press_start wait to be finished
        the function is called when start button is clicked, it starts the timetagger and generate a histogram

        """
        # create time tagger object
        tagger = TimeTagger.createTimeTagger()

        click = self.click_channel  # set click to user defined channel
        start = self.start_channel  # set start to user defined channel

        # Set trigger level of input channel to 1.1 V
        tagger.setTriggerLevel(click, 1.1)
        # Sets the dead_time of the input channel to 24000 ps
        tagger.setDeadtime(1, 6000)

        width = self.bin_width
        bin_number = self.bin_num
        int_time = 3e13                 # how do we want to define this integration time ? 3e13 is an example case
        acquire_time = int_time / 1e12

        trigger = tagger.getTriggerLevel(1)
        serial = tagger.getSerial()
        model = tagger.getModel()

        # create message box promoting information about this experiment
        exp_info_message = QMessageBox()
        exp_info_message.setWindowTitle("Trail Information")
        exp_info_message.setText(f"Model {model}.\n"
                                 f"Serial number: {serial}.\n"
                                 f"Channel {click} trigger level set to {trigger} Volts.\n"
                                 f"Bin_width = {width} ps, {bin_number} bins\n"
                                 f"Integration time set to {acquire_time} seconds.")
        exp_info_message.exec_()

        # create TimeTagger.Histogram for data collection
        histogram = TimeTagger.Histogram(tagger,
                                         click_channel=click,
                                         start_channel=start,
                                         binwidth=width,
                                         n_bins=bin_number)
        histogram.startFor(int(int_time))  # Sets the integration time (ps)
        histogram.waitUntilFinished()

        # record data
        counts = np.array(histogram.getData())  # Counts, integer data type
        time_data = np.array(histogram.getIndex())  # Time bins (ps), int data type
        self.data = pd.DataFrame({"Time (ps)": time_data, "Counts": counts})
        self.counts = histogram.getData()
        self.time_data = histogram.getIndex()

        # plot the data
        plt.plot(histogram.getIndex() / (1 * 10 ** 12),
                 histogram.getData(),
                 label="EFFA Scan 5 histogram")
        plt.title("PLE Histogram")
        plt.xlabel("Time [s]")
        plt.ylabel("Counts")
        plt.grid(True)
        plt.legend(loc='upper right')
        plt.show()

        TimeTagger.freeTimeTagger(tagger)  # free the time tagger

        # create a message box prompts user the end of data acquisition
        finish_message = QMessageBox()
        finish_message.setWindowTitle("Done!")
        finish_message.setText("Acquisition completed\nConnection to Time Tagger closed.")
        finish_message.exec_()

    def press_save(self):
        """
        press_save wait to be finished
        the function is called when save button is clicked, it save the data into desginated files,
        format of data dna file are not decided yet
        :return:
        """
        # get absolute path of save file directory  and save file name
        f_name = QFileDialog.getSaveFileName(self, "Save File", "", "csv(*.csv)")
        file_path = Path(f_name[0]+".csv")
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # save data as csv file
        self.data.to_csv(file_path)

        # save figure based on collected data
        file_path = Path(f_name[0])
        file_path.parent.mkdir(parents=True, exist_ok=True)
        plt.plot(self.time_data / (1 * 10 ** 12),
                 self.counts,
                 label="EFFA Scan 5 histogram")
        plt.title("PLE Histogram")
        plt.xlabel("Time [s]")
        plt.ylabel("Counts")
        plt.grid(True)
        plt.legend(loc='upper right')
        plt.savefig(file_path)

    def press_clear(self):
        """
        press_clear is activated when Clear button is pressed
        it clear all the Line Edit entry box in convenience to re-edit its content, also reset all variables to 0
        """
        # clear box entry
        self.bin_width_entry.setText("")
        self.num_trail_entry.setText("")
        self.click_channel_entry.setText("")
        self.start_channel_entry.setText("")
        self.bin_num_entry.setText("")
        self.gap_time_entry.setText("")
        self.total_time_entry.setText("")

        # reset variables to 0
        self.bin_width = 0
        self.total_time = 0
        self.trail_num = 0
        self.bin_num = 0
        self.gap_time = 0
        self.start_channel = 0
        self.click_channel = 0

        # disable start button for next confirm test
        self.start_button.setEnabled(False)


    def press_confirm(self):
        """
        press_confirm check the user input and check for conflict item
        if conflict exist, promote user to change conflict item
        if conflict resolved, store input data into class variables and disable entry
        """
        error_message = "Double Check Input Variables! \n"
        validity = True
        # check validity for total time input
        total_time_input = self.total_time_entry.text()
        try:
            total_time_input = float(total_time_input)
            total_unit = self.gap_time_unit.currentText()
            self.total_time = unit_conversion(total_time_input, total_unit)
            if total_time_input < 0:
                validity = False
                self.total_time_entry.setText("ERROR")
                error_message += "Warning: Invalid Total Time Input, must be a positive number!\n"
        except ValueError:
            error_message += "Warning: Invalid Total Time Input, must be a number!\n"
            self.total_time_entry.setText("ERROR")
            validity = False

        # check validity for number of trails input
        num_trail_input = self.num_trail_entry.text()
        try:
            num_trail_input = int(num_trail_input)
            self.trail_num = num_trail_input
            if num_trail_input < 1:
                validity = False
                self.num_trail_entry.setText("ERROR")
                error_message += "Warning: Invalid Number of Trails, must be greater than 0!\n"
        except ValueError:
            error_message += "Warning: Invalid Number of Trails, must be a Integer!\n"
            self.num_trail_entry.setText("ERROR")
            validity = False

        # check validity for gap time between trails
        gap_time_input = self.gap_time_entry.text()
        try:
            gap_time_input = float(gap_time_input)
            gap_unit = self.gap_time_unit.currentText()
            self.gap_time = unit_conversion(gap_time_input, gap_unit)
            if gap_time_input < 0:
                validity = False
                self.gap_time_entry.setText("ERROR")
                error_message += "Warning: Invalid Gap Time Input, must be 0 or a positive number!\n"
        except ValueError:
            error_message += "Warning: Invalid Gap Time Input, must be a number!\n"
            self.gap_time_entry.setText("ERROR")
            validity = False

        # check validity for number of Bins
        bin_num_input = self.bin_num_entry.text()
        try:
            bin_num_input = int(bin_num_input)
            self.bin_num = bin_num_input
            if bin_num_input < 1:
                validity = False
                self.bin_num_entry.setText("ERROR")
                error_message += "Warning: Invalid Number of Bins Input, must be a Integer greater than 1!\n"
        except ValueError:
            error_message += "Warning: Invalid Number of Bins Input, must be a Integer!\n"
            validity = False
            self.bin_num_entry.setText("ERROR")

        # check validity for Bin Width
        bin_width_input = self.bin_width_entry.text()
        try:
            bin_width_input = float(bin_width_input)
            width_unit = self.bin_width_unit.currentText()
            self.bin_width = unit_conversion(bin_width_input, width_unit)
            if bin_width_input <= 0:
                error_message += "Warning: Invalid Bin Width Input, must be greater than 0!\n"
                validity = False
                self.bin_width_entry.setText("ERROR")
        except ValueError:
            error_message += "Warning: Invalid Bin Width Input, must be a number!\n"
            validity = False
            self.bin_width_entry.setText("ERROR")

        # check validity for start channel input
        start_channel_input = self.start_channel_entry.text()
        try:
            start_channel_input = int(start_channel_input)
            # check validity for start channel range
            if start_channel_input < 0 or start_channel_input > 8:
                error_message += "Warning: Start Channel must be selected from Channel 0 to 8!\n"
                validity = False
                self.start_channel_entry.setText("ERROR")
            else:
                self.start_channel = start_channel_input
        except ValueError:
            error_message += "Warning: Invalid Start Channel Input, must be a Integer!\n"
            validity = False
            self.start_channel_entry.setText("ERROR")

        # check validity for click channel input
        click_channel_input = self.click_channel_entry.text()
        try:
            click_channel_input = int(click_channel_input)
            # check validity for click channel range
            if click_channel_input < 0 or click_channel_input > 8:
                error_message += "Warning: Click Channel must be selected from Channel 0 to 8!\n"
                validity = False
                self.click_channel_entry.setText("ERROR")
            else:
                self.click_channel = click_channel_input
        except ValueError:
            error_message += "Warning: Invalid Click Channel Input, must be a Integer! \n"
            validity = False
            self.click_channel_entry.setText("ERROR")

        # Click channel and Start Channel can not be the same channel, check for validity
        if self.start_channel == self.click_channel:
            error_message += "Warning: Start Channel must be different from Click Channel!\n"
            validity = False
            self.click_channel_entry.setText("ERROR")
            self.start_channel.setText("ERROR")

        # check for time conflict and make change suggestion under valid input condition
        if validity:
            single_trail_time = self.bin_width * self.bin_num
            expect_time = self.trail_num * single_trail_time + (self.trail_num-1) * self.gap_time
            if expect_time != self.total_time:
                validity = False
                error_message = "Total Time Seems have conflict with other variables.\n" \
                                + f"We had changed total time from {self.total_time} to {expect_time} \n" \
                                "DOUBLE CHECK INPUT VARIABLES!"

        # output prompt box for error message, change, or confirmed input
        if not validity:
            err_message = QMessageBox()
            err_message.setWindowTitle("Error Message")
            err_message.setText(error_message)
            err_message.exec_()
        else:
            self.start_button.setEnabled(True)
            confirm_message = QMessageBox()
            confirm_message.setWindowTitle("Confirmed!")
            confirm_message.setText("All Input Variables are Valid\nYou are Ready to GO!")
            confirm_message.exec_()

        # the print line below is for test
        print(error_message)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TimeTagger Histogram Generator"))
        # the following lines define label text
        # set text for click Channel_label
        self.click_channel_label.setText(_translate("MainWindow", "Click Channel:"))
        # set count_rate label text
        self.count_rate_label.setText(_translate("MainWindow", "Count Rate:"))
        # set start channel label text
        self.start_channel_label.setText(_translate("MainWindow", "Start Channel:"))
        # set gap_time_label text
        self.trail_gap_label.setText(_translate("MainWindow", "Time Between Trail:"))
        # set total_time_label text
        self.total_time_label.setText(_translate("MainWindow", "Total Time:"))
        # set num_bin_label text
        self.num_bin_label.setText(_translate("MainWindow", "Number of Bins:"))
        # set bin_width_label text
        self.bin_width_label.setText(_translate("MainWindow", "Bin Width:"))
        # set text for number of trail label
        self.trail_num_label.setText(_translate("MainWindow", "Number of Trails:"))

        # the following lines define button text
        # set text for start button
        self.start_button.setText(_translate("MainWindow", "Start"))
        # set text for save button
        self.save_button.setText(_translate("MainWindow", "Save Data"))
        # set text for confirm button
        self.confirm_button.setText(_translate("MainWindow", "Confirm"))
        # set text for clear button
        self.clear_button.setText(_translate("MainWindow", "Clear"))

        # The following lines define combo box element
        # set up gap time unit combo box element
        self.gap_time_unit.setItemText(0, _translate("MainWindow", "min"))
        self.gap_time_unit.setItemText(1, _translate("MainWindow", "sec"))
        self.gap_time_unit.setItemText(2, _translate("MainWindow", "ms"))
        self.gap_time_unit.setItemText(3, _translate("MainWindow", "μs"))
        self.gap_time_unit.setItemText(4, _translate("MainWindow", "ns"))
        self.gap_time_unit.setItemText(5, _translate("MainWindow", "ps"))
        # set up total_time unit combo box element
        self.total_time_unit.setItemText(0, _translate("MainWindow", "min"))
        self.total_time_unit.setItemText(1, _translate("MainWindow", "sec"))
        self.total_time_unit.setItemText(2, _translate("MainWindow", "ms"))
        self.total_time_unit.setItemText(3, _translate("MainWindow", "μs"))
        self.total_time_unit.setItemText(4, _translate("MainWindow", "ns"))
        self.total_time_unit.setItemText(5, _translate("MainWindow", "ps"))
        # set up bin width unit combo box element
        self.bin_width_unit.setItemText(0, _translate("MainWindow", "min"))
        self.bin_width_unit.setItemText(1, _translate("MainWindow", "sec"))
        self.bin_width_unit.setItemText(2, _translate("MainWindow", "ms"))
        self.bin_width_unit.setItemText(3, _translate("MainWindow", "μs"))
        self.bin_width_unit.setItemText(4, _translate("MainWindow", "ns"))
        self.bin_width_unit.setItemText(5, _translate("MainWindow", "ps"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
