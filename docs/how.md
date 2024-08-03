[Back to Index](./README.md)
# How Miao Image Works
Miao Image is a file type that stores images in miao format.

First of all miao image stores each hex value of each pixel in the image. The data is then compressed with [zlib](https://zlib.net/).
> ![TIP]
> you can fetch the hex data using the [spit cli command](cli.md#spit-hex-data)

When displaying an image, the data is decompressed and built back into a temporary image so that the gui window can display the file.

Miao image is not at all designed to save space or be efficient. It is designed to be funny and a meme. It is not recommended to use this file type for any serious work.