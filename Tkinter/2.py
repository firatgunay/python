from tkinter import *

# window
window = Tk()
window.title("tkinter")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

label = Label(text= "my label")
label.config(bg="black")
label.config(fg="white")
label.config(padx=10, pady=10)
label.pack()

def click():
    print("clicked")
    my_text = text.get("1.0", END)
    print(my_text)
    
button = Button(text="button", command=click)
button.config(padx=10, pady=10)
button.pack()

text = Text(width=20, height=10)
text.pack()

window.mainloop()