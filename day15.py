import tkinter as ttk
app = ttk.Tk()
app.title('my app')
app.geometry('600x400')

ttk.Label(app, text = 'A simple Text Label').place(x=50,y=50)
ttk.Label(app, text = 'Aadarsh').place(x=100,y=100)
app.mainloop()