
<h1 align="center" >Exif Viewer</h1>
<p align="center" width="100%">
<img width="80%" alt="exifscren" src="https://github.com/ip-repo/exif-view/assets/123945379/271f6438-2b0f-4fc9-91f7-48fdae8d846a">
</p>

This program  relies on <a href="https://exiftool.org/">ExifTool</a>.

ExifTool program is used for reading, writing and manipulating metadata in various file formats.<br>
Exif Viewer allow the users to choose a file and then by using ExifTool the metadata of the file is displayed in a neat html format.<br>ExifViewer also allow to save the metadata as text, html or csv.

## Install ExifTool
This program was built to be used on windows so we will need to download the windows version of exiftool.<br>
Navigate to <a href="https://exiftool.org/">ExifTool</a> homepage and download the `Windows Executable` zip folder.<br> 
Inside the zip folder there is a exe file named `exiftool(-k)` change the name of this exe file to `exiftool`.<br>
This is the ExifTool executable and we will need a copy of that in our project directory.<br>
Note: If you add exiftool to environment PATH variables then you dont to have a copy of exiftool in `exif-view` project directory.

## How to use the program
After you have downloaded ExifTool its time to clone this repo.

```console
git clone https://github.com/ip-repo/exif-view.git
```
Go to where ever you cloned this repo on your system and find the file `run.py` and paste next to him a copy of `exiftool.exe`.
Now your project directory should look something like that:
```
exif-view 📁
    components 📁
    icons      📁
    run.py
    exiftool.exe
```
Lets continue and create a virtual environment, activate it and `pip install PySide6`.

```console
python -m venv exif-venv
exif_venv\Scripts\activate
pip install PySide6 #6.6.2
```
Now with an active venv we can run the file `run.py`.
```consle
cd exif-view
python run.py
```
You can also call the program with one additional parameter that represent a file path that you want to view its metadata and the program will show it you.
If you add a file path when running the file it is recommended to use the file full path.

```console
python run.py c:\A\FileSome\where\On\The\System\file.txt
python run.py c:/A/FileSome/where/On/The/System/file.html
```
## How to launch ExifViewer from command line
On windows you can execute bat files from cmd so we will use that to launch ExifViewer when ever we type in a specific command.<br>
Lets say we have some where on the system a folder that holds have bat files in it`my-scripts` lets create a bat file called `exifview.bat` and place him in that folder.<br>
Note that the command syntx in command line will be the name of the bat file so for us the command will be `exifview`.

Now our bat script is simple.<br>
First we activate the venv of exif-view or a venv that has `PySide6`.<br>
Then we run the exif-view python entry point `run.py`.<br> Note that the symbols `%*` mean that every argument we send from the command line will be passed to the run.py when it is executed.<br>
This script will work better with full paths, try avoiding partial paths.

```console
call c:\path\to\exif-venv\Scripts\activate
python c:\path\to\python\script\exif-view\run.py %*
call c:\path\to\exif-venv\Scripts\deactivate.bat
```
At this point we have the script `exifview.bat` and the python project `exif-view` lets continue and see how we can call `exifview.bat` from the command line and launch exif-view gui program.

The first step is to let the system know where is your bat file and to do that we need to add to enivronment variables the path to the directory that holds our bat file named `my-scripts`.

Go to-> System properties -> Advanced -> Environment Variables -> Select Path -> Edit -> New ->
Now type in the the path to `my-scripts` directory: C:\path\to\my-scripts\ -> OK -> OK

And the second step is to open a cmd window and type in `exifview`.<br>
Now you should see ExifViewer.<br>
You can also send a file with the command.

```console
C:\Users\user\photos> exifview c:\Users\user\phots\photo.png
```
This will load to ExifViewer the file metadata.

