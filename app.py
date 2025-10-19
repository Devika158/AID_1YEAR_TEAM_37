import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("background colour changes")
root.geometry("400x200")
def change_color():
    selected_color=color_choice.get()
    root.config(bg=selected_color)
Label=tk.Label(root,text="pick a colour to change background")
font=("Arial",12)
Label.pack(pady=20)
colors=["red","blue","green","yellow","purple","pink","orange"]
color_choice=ttk.Combobox(root,values=colors,state="readoniy",font=("Arial",11))
color_choice.set("select a color")
color_choice.bind("<<Combobox selected>>",change_color)
color_choice.pack(pady=10)
change_button=tk.Button(root,text="select background color",command=change_color)
change_button.pack(pady=20)
root.mainloop()
