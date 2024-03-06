import csv
import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QTextEdit,QWidget, QPushButton,QFileDialog, QHBoxLayout,QVBoxLayout
from components.html_parts import html_part_one, html_part_two


class ExifViewer(QWidget):
	def __init__(self, script_dir) -> None:
		super().__init__()
		self.script_dir = script_dir
		
		self.init_ui_and_signals()
		
	def init_ui_and_signals(self):
		"""
		Init the widget ui and signals.
		"""
		self.setWindowTitle("Exif viewer")
		self.setGeometry(40, 40, 830, 600)
		self.setWindowIcon(QIcon(self.script_dir + "\\icons\\exif-viewer-icon.png"))
		self.dir, self.file_name, self.text,self.html_string = None, None, None,None
		self.choose_directory_btn = QPushButton("choose file")
		self.choose_directory_btn.setIcon(QIcon(self.script_dir + "\\icons\\exif-viewer-icon.png"))
		self.save_exif_data = QPushButton("save text")
		self.save_exif_data.setIcon(QIcon(self.script_dir + "\\icons\\save.png"))
		self.save_html_btn = QPushButton("save html")
		self.save_html_btn.setIcon(QIcon(self.script_dir +  "\\icons\\save_html.png"))
		self.save_csv_btn = QPushButton("save csv")
		self.save_csv_btn.setIcon(QIcon(self.script_dir + "\\icons\\save_csv.png"))
		self.text_edit = QTextEdit()
		
		
		layout = QHBoxLayout()
		v_layout = QVBoxLayout()
		layout.addWidget(self.choose_directory_btn,1)
		layout.addWidget(self.save_exif_data,1)
		layout.addWidget(self.save_html_btn,1)
		layout.addWidget(self.save_csv_btn,1)
		v_layout.addLayout(layout)
		v_layout.addWidget(self.text_edit)
		self.setLayout(v_layout)


		
		self.choose_directory_btn.clicked.connect(self.choose_file)
		self.save_exif_data.clicked.connect(self.save_text)
		self.save_html_btn.clicked.connect(self.save_html)
		self.save_csv_btn.clicked.connect(self.save_csv)

	def choose_file(self):
		""" open choose file dialog """
		file_path, _ = QFileDialog.getOpenFileName(caption="Choose file")
		if file_path:
			self.prepare_paths(file_path=file_path)
			...
	
	def prepare_paths(self, file_path: str):
		""" prepare information of user path for later use """
		self.file_path = file_path
		self.dir = "/".join(file_path.split("/")[:-1])+"/"
		self.file_name = file_path.split("/")[-1].split(".")[0]
		self.prepare_data()
	
	def prepare_data(self):
		""" use exiftool and read the file metadata and prepare objects from him """
		result = os.popen(self.script_dir + "\\exiftool.exe {}".format(self.file_path)).read().split("\n")
		self.data = {}
		for line in result:
			line = line.rstrip().split(":")
			if len(line) > 1:
				self.data[line[0].rstrip()] = line[1].rstrip()
			else:
				self.data[line[0].rstrip()] = None
		longest_key = max(len(key) for key in self.data.keys())
		text = ""
		for key, value in self.data.items():
			text +="{:<{}} : {}\n".format(key, longest_key, str(value)) 
		self.text = text
		self.prepare_html()
	
	def prepare_html(self):
		""" prepare a html page from metadata dict """
		html = html_part_one.copy()
		html.append("<h2>{}</h2>".format(self.file_path))
		html.extend(html_part_two)
		for key, value in self.data.items():
			html.append(f"  <tr><td>{key}</td><td>{value}</td></tr>")
		self.html_string = '\n'.join(html)

		
		self.text_edit.clear()
		self.text_edit.setText(self.html_string)
			
	def save_html(self):
		""" open file dialog to save the metadata as html"""
		if self.dir and self.file_name and self.html_string:
			file_name, _ = QFileDialog.getSaveFileName(caption="save exif as html",
							dir=self.dir + self.file_name +".html", filter="HTML Files (*.html);; ")
			if file_name:
				with open(file_name, "w") as html_file:
					html_file.write(self.html_string)
	
	def save_text(self):
		""" open file dialog to save metadata as text """
		if self.text and self.dir and self.file_name:
			file_name, _ = QFileDialog.getSaveFileName(caption="save exif as text",
						   dir=self.dir + self.file_name +".txt", filter="Text Files (*.txt)")
			if file_name:
				with open(file_name, "w") as file:
					file.write(self.text)
	
	def save_csv(self):
		""" open file dialog to save metadata as csv """
		file_name, _ = QFileDialog.getSaveFileName(caption="save exif as html",
						dir=self.dir + self.file_name +".csv", filter="CSV Files (*.csv);; ")
		if self.data and self.dir and self.file_name:
			if file_name:
				fn = ["Key","Value"]
				with open(file_name,"w",newline="") as csv_file:
					dict_writer = csv.DictWriter(csv_file,fieldnames=fn)
					dict_writer.writeheader()
					for key, value in self.data.items():
						dict_writer.writerow({"Key": key, "Value": value})
