# Importing modules
from Client_GUI.SearchDeleteWindow import *
from Client_GUI.InsertWindow import *
from tkinter import *
import tkinter.messagebox as tmsg
import tkinter.ttk
import tkinter.messagebox

# This is the first page to interact with the user
class HomePage:
    # Constructing homepage window class
    def __init__(self):
        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.wm_title("Project GUI")

        # The following functions perform when the user click the menu in menubar choice
        def exit():
            a = tmsg.askquestion("Exit?", "Are you sure sir?")
            if a == "yes":
                b = tmsg.askquestion("Again!", "Think again sir!")
                if b == "yes":
                    self.homePageWindow.destroy()

        def help():
            tmsg.showinfo("Help", "Contact Min for more information, Thank You :)")

        def feedback():
            l = tmsg.askquestion("Experience", "Was your experience good?")

            if l == "yes":
                tmsg.showinfo("Yes!", "Thanks for my using my application!")
            else:
                tmsg.showinfo("No!", "Sorry to hear that!")

        def update():
            msg = tmsg.askretrycancel("Sorry!", "Server is busy, so update is not available")
            if msg:
                tmsg.showinfo("Sorry", "Please try again later, update is not available!")

        # This will pop up another window when the user click the Rate Me button
        def RateWindow():
            root = Tk()
            root.geometry("400x100")
            root.minsize(400, 100)
            root.maxsize(400, 100)
            root.title("Please rate Min!")

            def rate():
                tmsg.showinfo("Feedback", "Thank You for Rating Me")
                with open("rate.txt", "a") as f:
                    f.write(f"Person rated = {Rate.get()}\n")
                root.destroy()
            Rate = Scale(root, from_=0, to=50, tickinterval=10, orient=HORIZONTAL)
            Rate.pack()
            b0 = Button(root, text="Rate", bg="yellow", command=rate)
            b0.pack()


        # Creating Menubar
        menubar = Menu(self.homePageWindow)
        # Adding three menus in menu bar and related commands to each menu
        menu1 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Available Service', menu=menu1)
        menu1.add_command(label='Help', command=help)
        menu1.add_command(label='Feedback', command=feedback)
        menu1.add_command(label='Update', command=update)
        menu1.add_separator()
        menu1.add_command(label='Exit', command=exit)

        menu2 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Rate', menu=menu2)
        menu2.add_command(label="Rate Me", command=RateWindow)

        menu3 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='View', menu=menu3)
        show_all = tkinter.BooleanVar()
        show_all.set(True)
        show_done = tkinter.BooleanVar()
        show_not_done = tkinter.BooleanVar()
        menu3.add_checkbutton(label="Show All", onvalue=1, offvalue=0, variable=show_all)
        menu3.add_checkbutton(label="Show Done", onvalue=1, offvalue=0, variable=show_done)
        menu3.add_checkbutton(label="Show Not Done", onvalue=1, offvalue=0, variable=show_not_done)

        # display Menu
        self.homePageWindow.config(menu=menubar)


        # Adding my personal information at the top of the project using Label and Frame
        tkinter.Label(self.homePageWindow, text="Name: Min Shwe Maung Htet\n"
                                                "Course: Python 3"
                                                "Topic: Min's Clinic Portal System Project",
                      width=100).grid(pady=20, column=1, row=1)
        instruction_frame = Frame(self.homePageWindow, width=150).grid(pady=20, column=1, row=2)
        Label(instruction_frame, text="You can do the following services "
                                      "in this application").grid(pady=20, column=1, row=3)


        # Creating five buttons in homepage for interaction with the program
        tkinter.Button(self.homePageWindow, width=20, text="Insert", command=self.Insert).grid(pady=15, column=1, row=5)
        tkinter.Button(self.homePageWindow, width=20, text="Search", command=self.Search).grid(pady=15, column=1, row=6)
        tkinter.Button(self.homePageWindow, width=20, text="Delete", command=self.Delete).grid(pady=15, column=1, row=7)
        tkinter.Button(self.homePageWindow, width=20, text="Display", command=self.Display).grid(pady=15, column=1,
                                                                                                 row=8)
        tkinter.Button(self.homePageWindow, width=20, text="Exit", command=self.homePageWindow.destroy).grid(pady=15,
                                                                                                             column=1,row=9)


        # Creating main loop
        self.homePageWindow.mainloop()


    # This each function performs differently specifically when the button clicks
    def Insert(self):
        self.insertWindow = InsertWindow()

    def Search(self):
        self.searchWindow = SearchDeleteWindow("Search")

    def Delete(self):
        self.deleteWindow = SearchDeleteWindow("Delete")

    def Display(self):
        self.database = Database()
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)


# Creating an instance of the HomePage class
homePage = HomePage()