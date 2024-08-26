# Get Started with Miao Image

- [Using CLI](#miao-image-cli-guide)
- [Using EXE](#miao-image-exe-guide)
- [Building from Source](#building-miao-image)
- [How it Works](#how-miao-image-works)
- [Using on Different Operating Systems](#using-on-different-operating-systems)

## About Miao Image
reasons not to use

- slow asf
- large file size
- unoptimised, prune to crashes

reasons to use

- its funny

![miao image working on linux mint](https://github.com/user-attachments/assets/17e23cd0-ae27-487f-9a35-c8f4256b22d4)

# Miao Image CLI Guide
[Back to Index](#get-started-with-miao-image)

Miao Image can be used in multiple ways. This guide will show you how to use Miao Image through the command line interface.

Make sure you have either the `miao.pyw` file or the `miao.exe` file. If you dont have it, you can download it from the [releases page](https://github.com/Daniel4-Scratch/miao-image/releases)

This documentaion will cover using the exe for examples, but you can replace `miao.exe` with `python miao.pyw` for the same results with the python file

## Convert Image to Miao File
Miao Image supports most common image formats to convert into a Miao file. It is recommended to use small dimension images for quicker conversion, quicker loading and smaller file size.
```
miao.exe convert <input.png> <output.miao>
```
Alternatively you can use one parameter. The output file will be located in the working directory with the same file name but with the `.miao` file extension
```
miao.exe <input.png>
```

## Convert Miao File to Png
Miao Image can convert a miao file back into an image. The larger the image, the longer it will take to convert.
```
miao.exe png <input.miao> <output.png>
```
Alternatively you can use two parameters to convert. The output file will be located in the working directory with the same name but with the `.png` extension
```
miao.exe png <input.miao>
```

## Display Miao File
Miao Image convert the miao file back into an image to display though a gui window.
The larger the image, the longer it will take to display.
```
miao.exe display <input.miao>
```
Miao Image can also display the miao file through one parameter. If the given file path is a miao file it will display it.
```
miao.exe <input.miao>
```

## Spit Hex Data
Miao Image can spit out the hex data of the miao file.
```
miao.exe spit <input.miao>
```

## Demo
You can use the demo command to see a demo of Miao Image.
```
miao.exe demo
```

# Miao Image Exe Guide
[Back to Index](#get-started-with-miao-image)

Miao Image can be used in multiple ways. This guide will show you how to use Miao Image through the exe file.

Make sure you have the `miao.exe` file. If you dont have it, you can download it from the [releases page](https://github.com/Daniel4-Scratch/miao-image/releases)

## Convert Image to Miao File
Drag and drop an image file onto the `miao.exe` file to convert it into a Miao file. The output file will be located in the working directory with the same name as the input file but with the `.miao` extension.

## Display Miao File
Drag and drop a Miao file onto the `miao.exe` file to display it as an image. The larger the image, the longer it will take to display.

## Installer
Alternatively, you can use the installer to install Miao Image on your system. The installer will create a shortcut on your desktop and in the start menu for easy access.

# Building miao image
[Back to Index](#get-started-with-miao-image)

Miao Image is built using PyInstaller. The following steps will show you how to build Miao Image from source.

## Requirements
First you need to install the required packages. You can do this by running the following command in the terminal.
```
pip install -r requirements.txt
```
Make sure to install pyinstaller and install auto-py-to-exe if you want to use GUI to build the exe.

```
pip install pyinstaller auto-py-to-exe
```

## Building with PyInstaller

Run the following command to build Miao Image using PyInstaller.
```
pyinstaller --noconfirm --onefile --windowed --icon "miao.ico" --name "Miao Image" --version-file "version.rc" --add-data "demo.miao;." --add-data "help.miao;." --add-data "miao.ico;." "miao.pyw"
```

## Building with auto-py-to-exe
Open auto-py-to-exe and import the `build.json` file under Settings. Then click on the `Convert .py to .exe` button to build the exe.

```
auto-py-to-exe
```

# How Miao Image Works
[Back to Index](#get-started-with-miao-image)

Miao Image is a file type that stores images in miao format.

First of all miao image stores each hex value of each pixel in the image. The data is then compressed with [zlib](https://zlib.net/).

When displaying an image, the data is decompressed and built back into a temporary image so that the gui window can display the file.

Miao image is not at all designed to save space or be efficient. It is designed to be funny and a meme. It is not recommended to use this file type for any serious work.

# Using on Different Operating Systems
[Back to Index](#get-started-with-miao-image)

What to do if you are using a different operating system.
- Windows: Use the exe
- MacOS and Linux: Use the Python source

## Python
Python is a cross-platform language, so the code should work on any operating system. You will need pip installed. Then you can install the required packages by running `pip install -r requirements.txt`.

## Exe
For MacOS and Linux I recommend using the Python source instead. But if you wish you should use [wine](https://www.winehq.org/) to run the exe. For MacOS you can use [winebottler](https://winebottler.kronenberg.org/). The exe will run significantly slower than the Python source and the exe on Windows.


![miao image working on ubuntu](https://github.com/user-attachments/assets/42dba949-5bb8-4433-a8d7-001a5c07f0ee)

## Notes
- I will try to keep this project cross-platform compatible, but I will not be able to test it on other platforms. I recommend using Windows for this project
- Do not use this file type for any serious work
  
This has been a very fun project to work on. Its taught me how to maintain and publish a project. 
