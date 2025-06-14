from PIL import Image, ImageTk
import tkinter as tk
from zlib import compress as zlibcompress
from zlib import decompress as zlibdecompress
import sys, os
import json, urllib.request
import webbrowser
import ssl
import certifi
from tkinter import messagebox

version = "0.1.9"
endpoints = {
    "latest": "https://api.github.com/repos/daniel4-scratch/miao-image/releases/latest"
}

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def open_latest():
    webbrowser.open("https://github.com/Daniel4-Scratch/miao-image/releases/latest")

def update_check():
    context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(endpoints["latest"], context=context) as url:
        data = json.loads(url.read().decode())
        ver = data["tag_name"].split("v")[1]
        #check if version >
        if ver > version:
            answer = messagebox.askyesno("Miao Image","Update available, would you like to open the latest release page?")
            if answer:
                open_latest()

update_check()


image_file_extensions = [
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".svg",
    ".ico", ".heif", ".heic", ".raw", ".cr2", ".nef", ".orf", ".sr2", ".arw",
    ".dng", ".rw2", ".pef", ".raf", ".3fr", ".ai", ".eps", ".psd"
]

def spit_json(image_path):
    filename, file_extension = os.path.splitext(image_path)
    if file_extension == ".miao":
        with open(image_path, "rb") as f:
            compressed_image = f.read()

        image_data = zlibdecompress(compressed_image).decode('utf-8')

        print(image_data)
    else:
        print("Not a valid miao file")

# Function to save the image data
def save_image_data(image_path, output_path):
    im = Image.open(image_path)
    pix = im.convert("RGBA").load()  # Convert to RGBA mode explicitly
    width, height = im.size

    image = ""

    # Iterate over each pixel in the image
    for y in range(height):
        for x in range(width):
            rgba = pix[x, y]
            if len(rgba) == 4:  # Ensure RGBA tuple has four elements
                hex_value = '#{:02x}{:02x}{:02x}{:02x}'.format(rgba[0], rgba[1], rgba[2], rgba[3])
                image += hex_value
            else:
                raise ValueError("Pixel data does not have RGBA format.")

        image += "\n"

    compressed_image = zlibcompress(image.encode('utf-8'))

    with open(output_path, "wb") as f:
        f.write(compressed_image)

def miao_to_png(image_path, output_path):
    with open(image_path, "rb") as f:
        compressed_image = f.read()

    image_data = zlibdecompress(compressed_image).decode('utf-8')

    # Create a new image
    width = len(image_data.split('\n')[0]) // 9
    height = len(image_data.split('\n')) - 1
    im = Image.new("RGBA", (width, height))
    pix = im.load()

    for y, row in enumerate(image_data.split('\n')):
        if row:
            for x in range(width):
                hex_value = row[x*9:(x+1)*9]
                rgba = tuple(int(hex_value[i:i+2], 16) for i in (1, 3, 5, 7))
                pix[x, y] = rgba

    im.save(output_path)

class ImageDisplayer:
    def __init__(self, image_path=None):
        self.image_path = image_path
        self.root = tk.Tk()
        self.root.iconbitmap(resource_path("miao.ico"))
        self.root.title("Miao Image Viewer")
        self.root.geometry("500x500")  # Set an initial size

        # Make the window resizable
        self.root.resizable(True, True)

        # Bind resize event to handle window resizing
        self.root.bind("<Configure>", self.on_window_resize)

        if image_path:
            # Load and display the image if image_path is provided
            self.load_image()

    def load_image(self):
        if self.image_path:
            with open(self.image_path, "rb") as f:
                compressed_image = f.read()

            image_data = zlibdecompress(compressed_image).decode('utf-8')

            # Create a new image
            width = len(image_data.split('\n')[0]) // 9
            height = len(image_data.split('\n')) - 1
            self.original_image = Image.new("RGBA", (width, height))
            pix = self.original_image.load()

            for y, row in enumerate(image_data.split('\n')):
                if row:
                    for x in range(width):
                        hex_value = row[x*9:(x+1)*9]
                        rgba = tuple(int(hex_value[i:i+2], 16) for i in (1, 3, 5, 7))
                        pix[x, y] = rgba

            # Display the image
            self.display_image()

    def raw(self, imagedata):
        # imagedata should be a string containing the encoded image data
        image_data = zlibdecompress(imagedata).decode('utf-8')

        # Create a new image
        width = len(image_data.split('\n')[0]) // 9
        height = len(image_data.split('\n')) - 1
        self.original_image = Image.new("RGBA", (width, height))
        pix = self.original_image.load()

        for y, row in enumerate(image_data.split('\n')):
            if row:
                for x in range(width):
                    hex_value = row[x*9:(x+1)*9]
                    rgba = tuple(int(hex_value[i:i+2], 16) for i in (1, 3, 5, 7))
                    pix[x, y] = rgba

        # Display the image
        self.display_image()

    def display_image(self):
        # Get current window size
        self.window_width = self.root.winfo_width()
        self.window_height = self.root.winfo_height()

        # Calculate scale factor
        if self.original_image.width > 0 and self.original_image.height > 0:
            scale_factor = min(self.window_width / self.original_image.width, self.window_height / self.original_image.height)
        else:
            scale_factor = 1.0
        
        new_width = max(1, int(self.original_image.width * scale_factor))  # Ensure width is at least 1
        new_height = max(1, int(self.original_image.height * scale_factor))  # Ensure height is at least 1

        # Resize image
        resized_image = self.original_image.resize((new_width, new_height), Image.NEAREST)

        # Update displayed image
        self.photo = ImageTk.PhotoImage(resized_image)
        if hasattr(self, 'image_label'):
            self.image_label.config(image=self.photo)
        else:
            self.image_label = tk.Label(self.root, image=self.photo)
            self.image_label.pack(fill=tk.BOTH, expand=tk.YES)

    def on_window_resize(self, event):
        # Redisplay the image on window resize
        self.display_image()

if len(sys.argv) > 1:
    if sys.argv[1] == "convert":
        if os.path.isfile(sys.argv[2]):
            save_image_data(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "png":
        if os.path.isfile(sys.argv[2]):
            #check if arg 3 wasnt provided
            if len(sys.argv) < 4:
                miao_to_png(sys.argv[2], sys.argv[2].replace(".miao", ".png"))
            else:
                miao_to_png(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "display":
        if os.path.isfile(sys.argv[2]):
            ImageDisplayer(sys.argv[2]).root.mainloop()
    elif sys.argv[1] == "demo":
        print("the demo file is large it will take a while to load")
        ImageDisplayer(resource_path("demo.miao")).root.mainloop()
    elif sys.argv[1] == "spit":
        spit_json(sys.argv[2])
    else:
        if os.path.isfile(sys.argv[1]):
            filename, file_extension = os.path.splitext(sys.argv[1])
            if file_extension == ".miao":
                ImageDisplayer(sys.argv[1]).root.mainloop()
            elif file_extension in image_file_extensions:
                save_image_data(sys.argv[1], filename+".miao")
        else:
            ImageDisplayer(resource_path("help.miao")).root.mainloop()
else:
    ImageDisplayer(resource_path("help.miao")).root.mainloop()