from tkinter import *
from tkinter import filedialog, messagebox

import PIL.PSDraw
from PIL import Image, ImageTk, ImageDraw, ImageFont

FONT_NAME = "Courier"
COLOR_1 = "#A5D7E8"
COLOR_2 = "#576CBC"
COLOR_3 = "#19376D"
COLOR_4 = "#0B2447"


def refresh(self):
    self.destroy()
    self.__init__()


def getimage():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("JPG Images",
                                                      "*.jpg*",),
                                                     ("PNG Images",
                                                      "*.png*",),
                                                     ("all files",
                                                      "*.*")))

    print(filename)
    img_path_label.config(text=f"Selected file: {filename}")
    global img
    img = ImageTk.PhotoImage(Image.open(filename))
    mini = ImageTk.PhotoImage(Image.open(filename).resize((100, 112), Image.ANTIALIAS))
    canvas.itemconfig(user_img, image=mini)
    refresh()


def addwatermark():
    try:
        img_x = img.width()
        img_y = img.height()
        with Image.open(filename).convert("RGBA") as base:
            txt = Image.new ("RGBA", base.size, (255, 255, 255, 0))

            watermark_font = ImageFont.truetype("arial", size.get())

            if pos.get() == "center":
                # if size.get() == 20:
                #     watermark_x = img_x / 2 - 40
                #     watermark_y = img_y / 2
                #
                # elif size.get() == 40:
                #     watermark_x = img_x / 2 - 80
                #     watermark_y = img_y / 2
                #
                # else:
                #     watermark_x = img_x / 2 - 120
                #     watermark_y = img_y / 2
                watermark_x = (img_x / 2) - (size.get()*2)
                watermark_y = img_y / 2

            elif pos.get() == "top left":
                watermark_x = 10
                watermark_y = 10

            else:
                # if size.get() == 20:
                #     watermark_x = img_x - img_x / 5
                #     watermark_y = img_y - img_y / 12
                #
                # elif size.get() == 40:
                #     watermark_x = img_x - img_x / 3
                #     watermark_y = img_y - img_y / 9
                #
                # else:
                #     watermark_x = img_x - img_x / 2
                #     watermark_y = img_y - img_y / 6
                watermark_x = img_x - (size.get() * 6)
                watermark_y = img_y - (size.get() * 2)


            watermark = ImageDraw.Draw(txt)

            watermark.text((watermark_x, watermark_y), watermark_text_input.get(), font=watermark_font, fill=(255, 255, 255, 128))

            # watermark.text((10, 60), "Watermark hehe", font=fnt, fill=(255, 255, 255, 255))

            out = Image.alpha_composite(base, txt)

            out.show()

    except NameError:
        messagebox.showerror(title="Error!", message="You need to choose a file!")


window = Tk()
window.title("Watermarking tool")
window.minsize(750, 600)
window.maxsize(900, 600)
window.config(padx=50, pady=50, bg=COLOR_1)

title_label = Label(text="Add a watermark to your photo", font=(FONT_NAME, 20, "bold"), bg=COLOR_1, fg=COLOR_4, pady=25)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=COLOR_2, highlightthickness=0)
img_default = ImageTk.PhotoImage(Image.open("default.jpg"))
user_img = canvas.create_image(100, 112, image=img_default)
canvas.grid(row=1, column=1)

img_path_label = Label(text="Selected file: none", font=(FONT_NAME, 10, "bold"), bg=COLOR_1, fg=COLOR_4)
img_path_label.grid(row=2, column=1)

get_image_button = Button(text="Choose photo", highlightthickness=0, command=getimage)
get_image_button.grid(row=3, column=0)

watermark_button = Button(text="Add watermark", highlightthickness=0, command=addwatermark)
watermark_button.grid(row=3, column=2)

watermark_text_input_label = Label(text="Watermark text:", font=(FONT_NAME, 15, "bold"), bg=COLOR_1, fg=COLOR_4)
watermark_text_input_label.grid(row=4, column=1)

watermark_text_input = Entry(width=37)
watermark_text_input.insert("0", "Watermark")
watermark_text_input.grid(row=5, column=1)

watermark_size_label = Label(text="Size:", font=(FONT_NAME, 15, "bold"), bg=COLOR_1, fg=COLOR_4)
watermark_size_label.grid(row=6, column=1)

size = IntVar()
size.set(40)
size1 = Radiobutton(window, text="Small", variable=size, value=20, bg=COLOR_1, fg=COLOR_4)
size1.grid(row=7, column=0)
size2 = Radiobutton(window, text="Medium", variable=size, value=40, bg=COLOR_1, fg=COLOR_4)
size2.grid(row=7, column=1)
size3 = Radiobutton(window, text="Big", variable=size, value=60, bg=COLOR_1, fg=COLOR_4)
size3.grid(row=7, column=2)

watermark_position_label = Label(text="Position:", font=(FONT_NAME, 15, "bold"), bg=COLOR_1, fg=COLOR_4)
watermark_position_label.grid(row=8, column=1)

pos = StringVar()
pos.set("center")
size1 = Radiobutton(window, text="top left", variable=pos, value="top left", bg=COLOR_1, fg=COLOR_4)
size1.grid(row=9, column=0)
size2 = Radiobutton(window, text="center", variable=pos, value="center", bg=COLOR_1, fg=COLOR_4)
size2.grid(row=9, column=1)
size3 = Radiobutton(window, text="bottom right", variable=pos, value="bottom_right", bg=COLOR_1, fg=COLOR_4)
size3.grid(row=9, column=2)

# fnt = StringVar()
# fnt.set("center")
# size1 = Radiobutton(window, text="top left", variable=fnt, value="top left", bg=COLOR_1, fg=COLOR_4)
# size1.grid(row=9, column=0)
# size2 = Radiobutton(window, text="center", variable=fnt, value="center", bg=COLOR_1, fg=COLOR_4)
# size2.grid(row=9, column=1)
# size3 = Radiobutton(window, text="bottom right", variable=fnt, value="bottom_right", bg=COLOR_1, fg=COLOR_4)
# size3.grid(row=9, column=2)
#
# pos = StringVar()
# pos.set("center")
# size1 = Radiobutton(window, text="top left", variable=pos, value="top left", bg=COLOR_1, fg=COLOR_4)
# size1.grid(row=9, column=0)
# size2 = Radiobutton(window, text="center", variable=pos, value="center", bg=COLOR_1, fg=COLOR_4)
# size2.grid(row=9, column=1)
# size3 = Radiobutton(window, text="bottom right", variable=pos, value="bottom_right", bg=COLOR_1, fg=COLOR_4)
# size3.grid(row=9, column=2)
window.mainloop()