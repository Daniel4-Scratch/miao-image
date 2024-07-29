# Miao Image File Type

reasons not to use

- slow asf
- large file size
- unoptimised, prune to crashes

reasons to use

- its funny

![image](https://github.com/user-attachments/assets/487658a6-b13b-4763-add7-7cbe8abf2ef7)



## how to use
### convert png to miao
i recommend using png for the input file. try to use small sized pngs
```bat
python miao.py convert <input.png> <output.miao>
```
### display miao file
```bat
python miao.py display <file.miao> 
```
### demo img
```
python miao.py demo
```

## Building Portable App
### auto-py-to-exe
Settings > Import Config File from JSON > build.json
### pyinstaller
```
pyinstaller --noconfirm --onefile --windowed --icon "C:\Users\danie\Desktop\sandbox\miao\miao-image\miao.ico" --version-file "C:\Users\danie\Desktop\sandbox\miao\miao-image\version.rc" --add-data "C:\Users\danie\Desktop\sandbox\miao\miao-image\demo.miao;." --add-data "C:\Users\danie\Desktop\sandbox\miao\miao-image\help.miao;." --add-data "C:\Users\danie\Desktop\sandbox\miao\miao-image\miao.ico;."  "C:\Users\danie\Desktop\sandbox\miao\miao-image\miao.pyw"```

