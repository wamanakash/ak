from subprocess import call
import tkinter as tk

from PIL import Image, ImageTk
from tkinter import ttk


root = tk.Tk()
root.title("GUI")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

image2 = Image.open('img2.jpg')

image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)


background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)




lbl = tk.Label(root, text="Land Classification Using Satellite Image", font=('times', 35,' bold '), height=1, width=32,bg="black",fg="white")
lbl.place(x=300, y=10)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
def log():
    from subprocess import call
    call(["python", "login.py"])

def reg():
    from subprocess import call
    call(["python", "registration.py"])






def window():
    root.destroy()

button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Login", command=log, width=15, height=2)
button2.place(x=5, y=90)

button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Registration", command=reg, width=15, height=2)
button3.place(x=5, y=170)

exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=5, y=330)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''