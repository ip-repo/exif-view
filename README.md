
<h1 align="center" >Exif Viewer</h1>
<p align="center" width="100%">
<img width="80%" alt="exifscren" src="https://github.com/ip-repo/exif-view/assets/123945379/271f6438-2b0f-4fc9-91f7-48fdae8d846a">
</p>

This program relay on <a href="https://exiftool.org/">ExifTool</a>.

ExifTool program is used for reading, writing and manipulating metadata in various file formats.
Exif Viewer allow the users to choose a file and then by using ExifTool the metadata of the file is displayed in a neat html format. Exif Viewer also allow to save the metadata as text, html or csv.

## Install ExifTool
This program was built to be used on windows so we will need to download the windows version of exiftool.
Navigate to <a href="https://exiftool.org/">ExifTool</a> homepage and download the `Windows Executable` zip folder. 
Inside the zip folder usally there is a exe file name `exiftool(-k)` change the name of this exe file to `exiftool`.
This is the ExifTool executable and we will need a copy of that in our project directory.

## How to use the program

```console
git clone
python -m venv exif_venv
exif_venv\Scripts\activate
pip install PySide6 #6.6.2
cd exif-view
python run.py
```
You can also call the program with one additional parameter that represent a file path that you want to view his metadata and the program will load those details for you see in the gui.
If add a file path to run command is it recommended to use the file full path

```console
python run.py c:\A\FileSome\where\On\The\System\file.txt
python run.py c:/A/FileSome/where/On/The/System/file.html
```


