from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont

class RotatedButton(Button):
    def __init__(self, master=None, **kwargs):
        Button.__init__(self, master, **kwargs)
        self.config(compound="top")
        self.bind("<Configure>", self._update)
        
    def _update(self, event):
        text = self["text"]
        width = self.winfo_width()
        height = self.winfo_height()
        image = Image.new("RGBA", (height, width), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 16)
        draw.text((0, 0), text, font=font, fill=(0, 0, 0, 255))
        image = image.rotate(90, expand=True)
        photo = ImageTk.PhotoImage(image)
        self.config(image=photo, width=height, height=width)

root = Tk()
button = RotatedButton(root, text="Hello\nWorld!", font=("Arial", 16), justify="left", width=5, height=10, padx=10)
button.pack()
root.mainloop()
