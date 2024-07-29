from PIL import Image, ImageTk
import tkinter as tk
import base64
import zlib
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

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

    compressed_image = zlib.compress(image.encode('utf-8'))

    with open(output_path, "wb") as f:
        f.write(compressed_image)

class ImageDisplayer:
    def __init__(self, image_path=None):
        self.image_path = image_path
        self.root = tk.Tk()
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

            image_data = zlib.decompress(compressed_image).decode('utf-8')

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
        image_data = zlib.decompress(imagedata).decode('utf-8')

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
    elif sys.argv[1] == "display":
        if os.path.isfile(sys.argv[2]):
            ImageDisplayer(sys.argv[2]).root.mainloop()
    elif sys.argv[1] == "demo":
        print("the demo file is large it will take a while to load")
        ImageDisplayer(resource_path("demo.miao")).root.mainloop()
    elif sys.argv[1] == "decode":
        with open(sys.argv[2]) as f:
            print(zlib.decompress(f.read()).decode('utf-8'))
            f.close()
    else:
        ImageDisplayer(resource_path("help.miao")).root.mainloop()
else:
    ImageDisplayer(resource_path("help.miao")).root.mainloop()