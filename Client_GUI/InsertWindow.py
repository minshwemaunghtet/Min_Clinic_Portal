# Importing modules and class
from Client_GUI.SearchDeleteWindow import *
import tkinter.messagebox as tmsg
import tkinter.ttk
import tkinter.messagebox
import sqlite3

# It is an insert class to get all information from the beginning
class InsertWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.wm_title("Insert data")

        # Initializing all the variables
        self.id = tkinter.StringVar()
        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.phone = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.history = tkinter.StringVar()
        self.doctor = tkinter.StringVar()
        self.genderButton = tkinter.IntVar()
        self.dateList = list(range(1, 32))
        self.monthList = ["January", "February", "March", "April", "May", "June", "July",
                          "August", "September", "October", "November", "December"]
        self.yearList = list(range(1900, 2020))
        self.bloodGroupList = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

        # Labels of the data
        tkinter.Label(self.window, text = "Patient ID",  width = 25).grid(pady = 5, column = 1, row = 1)
        tkinter.Label(self.window, text = "First Name",  width = 25).grid(pady = 5, column = 1, row = 2)
        tkinter.Label(self.window, text = "Last Name",  width = 25).grid(pady = 5, column = 1, row = 3)
        tkinter.Label(self.window, text = "D.O.B",  width = 25).grid(pady = 5, column = 1, row = 4)
        tkinter.Label(self.window, text = "M.O.B",  width = 25).grid(pady = 5, column = 1, row = 5)
        tkinter.Label(self.window, text = "Y.O.B",  width = 25).grid(pady = 5, column = 1, row = 6)
        tkinter.Label(self.window, text = "Gender",  width = 25).grid(pady = 5, column = 1, row = 7)
        tkinter.Label(self.window, text = "Home Address",  width = 25).grid(pady = 5, column = 1, row = 8)
        tkinter.Label(self.window, text = "Phone Number",  width = 25).grid(pady = 5, column = 1, row = 9)
        tkinter.Label(self.window, text = "Email ID",  width = 25).grid(pady = 5, column = 1, row = 10)
        tkinter.Label(self.window, text = "Blood Group",  width = 25).grid(pady = 5, column = 1, row = 11)
        tkinter.Label(self.window, text = "Patient History",  width = 25).grid(pady = 5, column = 1, row = 12)
        tkinter.Label(self.window, text = "Doctor",  width = 25).grid(pady = 5, column = 1, row = 13)

        # Fields
        # Entry widgets
        self.idEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.id)
        self.fNameEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.fName)
        self.lNameEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.lName)
        self.addressEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.address)
        self.phoneEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.phone)
        self.emailEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.email)
        self.historyEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.history)
        self.doctorEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.doctor)

        self.idEntry.grid(pady = 5, column = 3, row = 1)
        self.fNameEntry.grid(pady = 5, column = 3, row = 2)
        self.lNameEntry.grid(pady = 5, column = 3, row = 3)
        self.addressEntry.grid(pady = 5, column = 3, row = 8)
        self.phoneEntry.grid(pady = 5, column = 3, row = 9)
        self.emailEntry.grid(pady = 5, column = 3, row = 10)
        self.historyEntry.grid(pady = 5, column = 3, row = 12)
        self.doctorEntry.grid(pady = 5, column = 3, row = 13)

        # Combobox widgets
        self.dobBox = tkinter.ttk.Combobox(self.window, values = self.dateList, width = 20)
        self.mobBox = tkinter.ttk.Combobox(self.window, values = self.monthList, width = 20)
        self.yobBox = tkinter.ttk.Combobox(self.window, values = self.yearList, width = 20)

        # Radio button for male and female button
        self.genderButton.set(1)
        self.male_button = tkinter.ttk.Radiobutton(self.window, text="Male", variable=self.genderButton,
                                                 value = 1, width = 20)
        self.female_button = tkinter.ttk.Radiobutton(self.window, text="Female", variable=self.genderButton,
                                                 value = 2, width=20)
        self.bloodGroupBox = tkinter.ttk.Combobox(self.window, values = self.bloodGroupList, width = 20)


        # Putting all combobox and radiobutton in grid format
        self.dobBox.grid(pady = 5, column = 3, row = 4)
        self.mobBox.grid(pady = 5, column = 3, row = 5)
        self.yobBox.grid(pady = 5, column = 3, row = 6)
        self.male_button.grid(padx = 5, column = 3, row = 7)
        self.female_button.grid(padx=5, column=4, row=7)
        self.bloodGroupBox.grid(pady = 5, column = 3, row = 11)


        # Button widgets in the very bottom of the window
        tkinter.Button(self.window, width = 20, text = "Insert", command = self.Insert)\
            .grid(pady = 15, padx = 5, column = 1, row = 14)
        tkinter.Button(self.window, width = 20, text = "Reset", command = self.Reset)\
            .grid(pady = 15, padx = 5, column = 2, row = 14)
        tkinter.Button(self.window, width = 20, text = "Close", command = self.window.destroy)\
            .grid(pady = 15, padx = 5, column = 3, row = 14)

        # Creating mainloop
        self.window.mainloop()

    # This insert function interacts with the class to get input valid data
    def Insert(self):
        self.values = Values()
        self.database = Database()
        self.test = self.values.Validate(self.idEntry.get(), self.fNameEntry.get(), self.lNameEntry.get(),
                                         self.phoneEntry.get(), self.emailEntry.get(), self.historyEntry.get(),
                                         self.doctorEntry.get())
        if (self.test == "SUCCESS"):
            self.database.Insert(self.idEntry.get(), self.fNameEntry.get(), self.lNameEntry.get(),
                                 self.dobBox.get(), self.mobBox.get(), self.yobBox.get(),
                                 self.genderButton.get(), self.addressEntry.get(), self.phoneEntry.get(),
                                 self.emailEntry.get(), self.bloodGroupBox.get(), self.historyEntry.get(),
                                 self.doctorEntry.get())
            tkinter.messagebox.showinfo("Inserted data", "Successfully inserted the above data in the database")
        else:
            self.valueErrorMessage = "Invalid input in field " + self.test
            tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)

    # This function clear out all the input data in insert field
    def Reset(self):
        self.idEntry.delete(0, tkinter.END)
        self.fNameEntry.delete(0, tkinter.END)
        self.lNameEntry.delete(0, tkinter.END)
        self.dobBox.set("")
        self.mobBox.set("")
        self.yobBox.set("")
        self.genderButton.set("")
        self.addressEntry.delete(0, tkinter.END)
        self.phoneEntry.delete(0, tkinter.END)
        self.emailEntry.delete(0, tkinter.END)
        self.bloodGroupBox.set("")
        self.historyEntry.delete(0, tkinter.END)
        self.doctorEntry.delete(0, tkinter.END)


# This value class gets input data with valid information
class Values:
    def Validate(self, id, fName, lName, phone, email, history, doctor):
        if not (id.isdigit()):
            return "id"
        elif not (fName.isalpha()):
            return "fName"
        elif not (lName.isalpha()):
            return "lName"
        elif not (phone.isdigit() and (len(phone) == 10)):
            return "phone"
        elif not (email.count("@") == 1 and email.count(".") > 0):
            return "email"
        elif not (history.isalpha()):
            return "history"
        elif not (doctor.isalpha()):
            return "doctor"
        else:
            return "SUCCESS"

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("dbFile.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS patient_info (id PRIMARYKEY text, fName text, lName text, "
                              "dob text, mob text, yob text, gender text, address text, phone text, email text, "
                              "bloodGroup text, history text, doctor text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    # This insert function adds information to the database
    def Insert(self, id, fName, lName, dob, mob, yob, gender, address,
               phone, email, bloodGroup, history, doctor):
        self.dbCursor.execute("INSERT INTO patient_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                              (id, fName, lName, dob, mob, yob, gender, address,
                               phone, email, bloodGroup, history, doctor))
        self.dbConnection.commit()

    # This update function updates information to the database
    def Update(self, fName, lName, dob, mob, yob, gender, address,
               phone, email, bloodGroup, history, doctor, id):
        self.dbCursor.execute("UPDATE patient_info SET fName = ?, lName = ?, dob = ?, mob = ?, yob = ?, gender = ?, "
                              "address = ?, phone = ?, email = ?, bloodGroup = ?, history = ?, doctor = ? WHERE id = ?",
                              (fName, lName, dob, mob, yob, gender, address,
                               phone, email, bloodGroup, history, doctor, id))
        self.dbConnection.commit()

    # This function performs to get information with patient id key
    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM patient_info WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    # This function performs to delete information with patient id key
    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM patient_info WHERE id = ?", (id, ))
        self.dbConnection.commit()

    # This function shows all information of the patient data
    def Display(self):
        self.dbCursor.execute("SELECT * FROM patient_info")
        records = self.dbCursor.fetchall()
        return records
