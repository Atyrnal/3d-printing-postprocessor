from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
import sys
import os
from ui import Ui_MainWindow
import re
from datetime import datetime
import uuid

TARGET_PROPERTIES = ["total filament used [g]", "filament_type", "printer_settings_id", "estimated printing time (normal mode)", "filament_settings_id", "print_settings_id", "job_name"]


def main():
    if len(sys.argv) < 2:
        print("Usage: post_processor <gcode filename>")
        sys.exit(1)
    gcode_filepath = sys.argv[1]
    if not os.path.exists(gcode_filepath):
        print("GCode file not found.")
        sys.exit(1)
    gcode_file = open(gcode_filepath, "r")
    gcode_properties = {}
    for line in gcode_file:
        for p in TARGET_PROPERTIES:
            if line.startswith(f"; {p} = "):
                gcode_properties[p] = line.split("=").pop().strip()
    name, email, filament_owner = gui({
        "name" : gcode_properties[TARGET_PROPERTIES[6]] if TARGET_PROPERTIES[6] in gcode_properties.keys() else "Unknown",
        "printer" : gcode_properties[TARGET_PROPERTIES[2]] if TARGET_PROPERTIES[2] in gcode_properties.keys() else "Unknown",
        "filament" : str(gcode_properties[TARGET_PROPERTIES[4]]).replace("\"", "") if TARGET_PROPERTIES[4] in gcode_properties.keys() else "Unknown",
        "print_settings" : gcode_properties[TARGET_PROPERTIES[5]] if TARGET_PROPERTIES[5] in gcode_properties.keys() else "Unknown",
        "weight" : gcode_properties[TARGET_PROPERTIES[0]] if TARGET_PROPERTIES[0] in gcode_properties.keys() else "Unknown",
        "duration" : gcode_properties[TARGET_PROPERTIES[3]] if TARGET_PROPERTIES[3] in gcode_properties.keys() else "Unknown"
    })

    if (not name or not email or not filament_owner): #Exit if closed
        sys.exit(2)

    now = datetime.now()

    output = {
        "HumanName" : name.strip(),
        "Email" : email.strip(),
        "FileName" : str(gcode_properties[TARGET_PROPERTIES[6]] if TARGET_PROPERTIES[6] in gcode_properties.keys() else "Unknown").strip(),
        "FilamentType" : str(gcode_properties[TARGET_PROPERTIES[1]]).replace("\"", "").strip() if TARGET_PROPERTIES[1] in gcode_properties.keys() else "Unknown",
        "FilamentOwner" : filament_owner.strip(),
        "FilamentWeight" : str(gcode_properties[TARGET_PROPERTIES[0]]) + "g" if TARGET_PROPERTIES[0] in gcode_properties.keys() else "Unknown",
        "Time" : now.strftime(r"%b, %e, %Y, %I:%M:%S %p"),
        "UUID" : uuid.uuid4(),
        "Timestamp" : now.timestamp()
    }

    if TARGET_PROPERTIES[2] in gcode_properties:
        full_str = str(gcode_properties[TARGET_PROPERTIES[2]])
        printer_type = full_str.split("(")[0].strip()
        printer_number = full_str.split("#")[1].split(" ")[0].strip()
        printer_name = full_str.split("#")[1].split(" ").pop(0)
        printer_name = printer_name.join(" ").strip()
        printer = f"{printer_type} #{printer_number} - {printer_name}"

        printer_regex = re.compile(r"^[A-Za-z0-9 ]+\s+#[0-9]+\s+-[A-Za-z0-9 ]+$")
        if printer_regex.match(printer):
            output["PrinterName"] = printer
        else:
            output["PrinterName"] = full_str
    else:
        output["PrinterName"] = "Unknown"

    print(output)
    sys.exit(0)
    
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, printInfo):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Makerspace 3D Printing Form")

        self.cancel.clicked.connect(self.cancel_slot)
        self.submit.clicked.connect(self.submit_slot)
        self.submission = None

        self.nameInfo.setText("Name: " + printInfo["name"])
        self.printerInfo.setText("Printer: " + printInfo["printer"])
        self.filamentInfo.setText("Filament: " + printInfo["filament"])
        self.printInfo.setText("Print Settings: " + printInfo["print_settings"])
        self.weightInfo.setText("Weight: " + printInfo["weight"] + "g")
        self.durationInfo.setText("Duration: " + printInfo["duration"])

    def cancel_slot(self):
        sys.exit(1)

    def submit_slot(self):
        name = self.nameInput.text()
        email = self.emailInput.text()

        name_regex = re.compile(r"^[A-Za-z\. ]+$")
        email_regex = re.compile(r"^[-A-Za-z0-9!#$%&'*+/=?^_`{|}~]+(?:\.[-A-Za-z0-9!#$%&'*+/=?^_`{|}~]+)*@umass\.edu$")
        if not name_regex.match(name):
            self.error.setText("Invalid Name")
            return
        elif not email_regex.match(email):
            self.error.setText("Invalid Email")
            return
        else:
            self.error.setText("")

        self.submission = (name,  email, "makerspace" if self.mkspace.isChecked() else "personal")
        self.close()
       



def gui(printInfo):
    app = QApplication([])
    window = MainWindow(printInfo)
    window.show()
    app.exec()
    return window.submission

if __name__ == "__main__":
    main()

