[Back to Index](./README.md)
# Miao Image CLI Guide
Miao Image can be used in multiple ways. This guide will show you how to use Miao Image through the command line interface.

Make sure you have either the `miao.pyw` file or the `miao.exe` file. If you dont have it, you can download it from the [releases page](https://github.com/Daniel4-Scratch/miao-image/releases)

This documentaion will cover using the exe for examples, but you can replace `miao.exe` with `python miao.pyw` for the same results with the python file

## Convert Image to Miao File
Miao Image supports most common image formats to convert into a Miao file. Its recommended to use small dimension images for quicker conversion, quicker loading and smaller file size.
```bat
miao.exe convert <input.png> <output.miao>
```
### Alternate Method
Miao image can also conver through one parameter. If the given file path is a common image type it will convert it. The output file will be located in the working directory with the same name as the input file but with the `.miao` extension. 
```bat
miao.exe <input.png>
```

## Display Miao File
Miao Image convert the miao file back into an image to display though a gui window.
The larger the image, the longer it will take to display.
```bat
miao.exe display <input.miao>
```
### Alternate Method
Miao Image can also display the miao file through one parameter. If the given file path is a miao file it will display it.
```bat
miao.exe <input.miao>
```

## Spit Hex Data
Miao Image can spit out the hex data of the miao file.
```bat
miao.exe spit <input.miao>
```

## Demo
You can use the demo command to see a demo of Miao Image.
```bat
miao.exe demo
```