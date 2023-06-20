from tkinter import *

# window
window = Tk()
window.title("tkinter")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

#scale
def select_scale(value):
    print(value)
scale = Scale(from_=0, to=50, command=select_scale)
scale.pack()

#spinbox
def spinbox():
    print(my_spinbox.get())
my_spinbox = Spinbox(from_=0, to=50, command=spinbox)
my_spinbox.pack()

#check butoon
def checkbutton_control():
    print(check_state.get())    
check_state = IntVar()
my_chechk_button = Checkbutton(text="check", variable=check_state, command=checkbutton_control)
my_chechk_button.pack()

# radio-button
def radio_selected():
    print(radio_check_state.get())

radio_check_state = IntVar()
my_radiobutton = Radiobutton(text="1.option", value=10, variable=radio_check_state, command=radio_selected)
my_radiobutton2 = Radiobutton(text="1.option", value=20, variable=radio_check_state, command=radio_selected)
my_radiobutton.pack()
my_radiobutton2.pack()

# listbox
def select_listbox(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ["atil", "firat", "jkdsnk", "dkl"]
for i in range(len(name_list)):
    my_listbox.insert(i, name_list[i])

my_listbox.bind('<<ListboxSelect>>', select_listbox)
my_listbox.pack()

window.mainloop()