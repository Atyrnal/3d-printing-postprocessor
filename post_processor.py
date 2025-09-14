from tkinter import *
import sys
import os

TARGET_PROPERTIES = ["total filament used [g]", "filament_type", "printer_model", "printer_settings_id", "printer_notes", "estimated printing time (normal mode)"]



def main():
    if len(sys.argv) < 2:
        print("Usage: post_processor <gcode filename>")
        exit(1)
    gcode_filepath = sys.argv[1]
    if not os.path.exists(gcode_filepath):
        print("GCode file does not found.")
        exit(1)
    gcode_file = open(gcode_filepath, "r")
    gcode_properties = {}
    for line in gcode_file:
        for p in TARGET_PROPERTIES:
            if p+" = " in line:
                gcode_properties[p] = line.split("=")[1].strip()
    gui()
    

def gui():
    root = Tk()

    title = Label(root, text="UMass Makerspace 3D Print Form")
    title.pack()

    submit = Button(root, text="Submit", command=root.destroy)
    submit.pack()
    root.mainloop()

if __name__ == "__main__":
    main()