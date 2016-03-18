from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class MainScreen:
    def __init__(self, master):
        self.pic = ""

        master.minsize(width=600, height=400)
        #master.configure(background="firebrick3")
        frame = Frame(master)

        self.directoryLabel = Label(frame, text="Choose Photo")
        self.picEntry = Entry(frame, width=50)
        self.directoryLabel.grid(row=4, sticky=E)
        self.picEntry.grid(row=4, column=1)

        self.choosePic = Button(frame, text="Browse", command=self.askFile)
        self.choosePic.grid(row=4, column = 2)

        self.enterButton = Button(frame, text="Enter", command=self.submit)
        self.enterButton.grid(row=5, columnspan=1)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.grid(row=5, columnspan=4)

        frame.pack()
        frame.mainloop()

    def askFile(self):
        self.pic = filedialog.askopenfilename()
        self.picEntry.insert(0, self.pic)
        image = Image.open(self.pic)
        photo = ImageTk.PhotoImage(image)

    def submit(self):
        return


root = Tk()

button = MainScreen(root)





