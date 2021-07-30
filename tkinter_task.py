import tkinter as tk
screen = tk.Tk()
screen.title("Form")
screen.configure(background = "red")
# ==================================================== First Name ============================================= #
First = tk.Label(screen ,text = "First Name")
First.pack()
First1=tk.Entry(screen)
First1.pack()
# ==================================================== Last Name ============================================= #
Last = tk.Label(screen ,text = "Last Name")
Last.pack()
Last1=tk.Entry(screen)
Last1.pack()

# ==================================================== Gender ============================================= #
gender = tk.Label(screen ,text = "Last Name")
gender.pack()
var = tk.IntVar()
gender1=tk.Radiobutton(screen, text="Male", variable=var, value=1)
gender1.pack()
gender2=tk.Radiobutton(screen, text="Female", variable=var, value=2)
gender2.pack()

# ==================================================== Email-id ============================================= #
EmailId = tk.Label(screen ,text = "Email Id")
EmailId1=tk.Entry(screen)
EmailId.pack()
EmailId1.pack()
# ==================================================== Phone Number ============================================= #
Number = tk.Label(screen ,text = "Contact Number")
Number.pack()
Number1=tk.Entry(screen)
# Number1=tk.IntVar(Number1)
Number1=int(Number1)
Number1.pack()
# ==================================================== Date Of Birth ============================================= #
DOB = tk.Label(screen ,text = "Date-of-birth")
# import wckCalendar
import tkcalendar as tkc 
def cal():
    print (DOB.getselection())

DOB.pack()
DOB1 = tkc.Calendar(screen, command=cal)
DOB1.pack()

# ======================================================== Age =================================================== #
Age = tk.Label(screen ,text = "age")
Age.pack()
Age1=tk.Entry(screen)
# Age1=int(Age1)
Age1.pack()

# ======================================================== Save-Button =================================================== #

save=tk.Button(screen,text='Save')
save.pack()

screen.mainloop()