from tkinter import *

window = Tk()
window.title("Miles to Km")
window.minsize(width=250, height=100)


def miles_to_km():
    kilometer = (int(entry.get())) * 8 / 5
    label_km.config(text=int(kilometer))


entry = Entry()
entry.grid(row=0, column=1)
user_input = entry.get()

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label_km = Label(text="0")
label_km.grid(row=1, column=1)

label3 = Label(text="Km")
label3.grid(row=1, column=2)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(row=2, column=1)

window.mainloop()
