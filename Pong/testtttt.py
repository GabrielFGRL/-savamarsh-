from tkinter import *

root = Tk() 
root.geometry('500x500') 
root.title('Good morning :)') 

frame1 = Frame(root, bg='green') 
frame1.pack(expand=True, fill=BOTH) 

button1 = Button(frame1, text='Hello') 
button1.place(relx=0.5,rely=0.5) 

root.mainloop()