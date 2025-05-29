# Miao Image CLI Guide

This guide explains how to use the Miao Image program from the command line.

## Convert Image to Miao File

Convert a supported image file (e.g., PNG, JPG) to a `.miao` file:

```
miao convert <input_image> <output.miao>
```

Or, simply provide the image file as the only argument:

```
miao <input_image>
```
The output `.miao` file will be created in the same directory as the input image.

## Convert Miao File to PNG

Convert a `.miao` file back to a PNG image:

```
miao png <input.miao> <output.png>
```

Or, omit the output file to save as `<input>.png`:

```
miao png <input.miao>
```

## Display a Miao File

Display a `.miao` file in a GUI window:

```
miao display <input.miao>
```

Or, simply provide the `.miao` file as the only argument:

```
miao <input.miao>
```

## Spit Hex Data

Print the raw hex data stored in a `.miao` file:

```
miao spit <input.miao>
```

## Demo

Show a demo image (loads `demo.miao`):

```
miao demo
```

## Help

If you run the program with no arguments or with an invalid file, it will display the help image.

---

Supported image formats include: PNG, JPG, JPEG, GIF, BMP, TIFF, WEBP, SVG, ICO, and many more.