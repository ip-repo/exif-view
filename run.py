import sys
import os
from components.exif_viewer import ExifViewer
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    #uncomment if you want the script to be run from the script folder
    #os.chdir(script_dir)
    app = QApplication()
    with open(script_dir + "\\components\\style.qss") as style_file:
        style = style_file.read()
    app.setStyleSheet(style)
    ev = ExifViewer(script_dir)

    if len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
            ev.prepare_paths(file_path=sys.argv[1])           
    ev.show()
    app.exec()
