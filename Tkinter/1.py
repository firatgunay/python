import tkinter

# window
window = tkinter.Tk()
window.title("tkinter")
window.minsize(width=450, height=450)

def click_button():
   user_input =  my_entry.get()
   print(user_input)

#label
my_label = tkinter.Label(text = "hello Tkinter", font=('Arial', 15, 'bold'))
my_label.config(bg="black", fg="white")
my_label.pack(side="top")

#button
my_button = tkinter.Button(text="this is a button", command=click_button)
my_button.pack(side="top")

#entry

my_entry = tkinter.Entry(width=20)
my_entry.pack(side="top")


window.mainloop()
