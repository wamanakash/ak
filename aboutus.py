import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Alzheimer Disease Detection")


label_l1 = tk.Label(root, text="Land Classification Using Satellite Image",font=("Times New Roman", 30, 'bold'),
                    background="#006400", fg="white", width=67, height=2)
label_l1.place(x=0, y=0)


label_l2 = tk.Label(root, text="___ About us ___",font=("Times New Roman", 30, 'bold'),
                    background="#EEEE00", fg="black", width=67, height=3)
label_l2.place(x=0, y=90)

img1 = Image.open('img2.jpg')
img1 = img1.resize((750,600), Image.ANTIALIAS)
logo_image1 = ImageTk.PhotoImage(img1)

logo_label1 = tk.Label(root, image=logo_image1)
logo_label1.image = logo_image1
logo_label1.place(x=0, y=250)


label_l2 = tk.Label(root, text="Land Classification Using Satellite Image",font=("Times New Roman", 20, 'bold'),
                    background="#006400", fg="white", width=48, height=2)
label_l2.place(x=750, y=350)
label_l2 = tk.Text(root,font=("Times New Roman", 15, 'italic'),
                    background="#006400", fg="white", width=77, height=12)
label_l2.place(x=750, y=420)



Fact=""" 
*****************************************************************************
     The  classification  of  the  large  satellite  images  presents  significant \n challenges  in  comprehending  and representing information related to land cover.\n Land cover it refers to the physical features that present on the Earth’s  surface,  including \n rivers,  forests,  crop  fields,  and  barren  lands.  Accurate information  about \n  the land cover  is crucial  for  categorizing,  planning,  monitoring,  and  making  informed  \n decisions  regarding  the  use  of earth’s  resources  for  the  benefit \n of  human  mankind.
*****************************************************************************
"""

label_l2.insert(tk.END, Fact)


def log():
    from subprocess import call
    call(["python","GUI_main.py"])
    root.destroy()
    
def window():
  root.destroy()
     
    
button1 = tk.Button(label_l1, text="Home", command=log, width=14, height=1,font=('times 16 bold underline'),bd=0, bg="#006400", fg="white")
button1.place(x=1200, y=60)

button2 = tk.Button(label_l1, text="Exit",width=14, height=1,font=('times 16 bold underline'), bd=0,bg="#006400", fg="white")
button2.place(x=1330, y=60)



label_l1 = tk.Label(root, text="** Alzheimer Disease Detection @ 2021 by Bitmap Technology **",font=("Times New Roman", 10, 'bold'),
                    background="black", fg="white", width=200, height=2)
label_l1.place(x=0, y=800)


root.mainloop()