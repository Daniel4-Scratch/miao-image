[Back to Index](./README.md)
# Building miao image
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
pyinstaller --noconfirm --onefile --windowed --icon "miao.ico" --version-file "version.rc" --add-data "demo.miao;." --add-data "help.miao;." --add-data "miao.ico;."  "miao.pyw"
```

## Building with auto-py-to-exe
Open auto-py-to-exe and import the `build.json` file under Settings. Then click on the `Convert .py to .exe` button to build the exe.

```
auto-py-to-exe
```