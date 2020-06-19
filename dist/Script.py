from tkinter import *
from tkinter import messagebox

class Script:
    def __init__(self,root):
        self.root=root
        self.root.title("Script")
        self.root.geometry('1350x700')

        title = Label(self.root, text="Script", font=("times new roman", 40, "bold"), bg="black", fg="white")
        title.pack(side=TOP, fill=X)

        frame_root = Frame(self.root, bd=4, relief=RIDGE, bg="Crimson")
        frame_root.place(x=0, y=68, height=640, width=1350)

        user_name = Label(frame_root, text="Username", font=("times new roman", 10, "bold"), bg="green", fg="white")
        user_name.grid(row=0, column=0)

        user_entry = Entry(frame_root)
        user_entry.grid(row=0, column=1)

        id_name = Label(frame_root, text="ID", font=("times new roman", 10, "bold"), bg="green", fg="white")
        id_name.grid(row=1, column=0)

        id_entry = Entry(frame_root)
        id_entry.grid(row=1, column=1)

        pass_name = Label(frame_root, text="Password", font=("times new roman", 10, "bold"), bg="green", fg="white")
        pass_name.grid(row=2, column=0)

        pass_entry = Entry(frame_root)
        pass_entry.grid(row=2, column=1)

        button = Button(frame_root, text="Submit", command=msg_root)
        button.grid(row=3, column=0)


def msg_root():
    messagebox.showinfo("Script","Your OBB File is protected")



root=Tk()
obj=Script(root)
root.mainloop()
