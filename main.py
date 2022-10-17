import tkinter as tk 

root = tk.Tk()

svarVindu = tk.Entry(root, font = ("Arial", 20))
svarVindu.grid(row = 0, column = 0)

ceButton = tk.Button(root, text = "CE", font = ("Arial, 20"))
ceButton.grid(row = 1, column = 0 )

CButton = tk.Button(root, text = "C", font = ("Arial, 20"))
CButton.grid(row = 1, column = 1 )

delButton = tk.Button(root, text = "del", font = ("Arial, 20"))
delButton.grid(row = 1, column = 2,  sticky = "we")

pwrButton = tk.Button(root, text = "pwr", font = ("Arial, 20"))
pwrButton.grid(row = 1, column = 3, sticky = "we")


syvButton = tk.Button(root, text = "7", font = ("Arial, 20"))
syvButton.grid(row = 2, column = 0, sticky = "we")

åtteButton = tk.Button(root, text = "8", font = ("Arial, 20"))
åtteButton.grid(row = 1, column = 1, sticky = "we")


niButton = tk.Button(root, text = "9", font = ("Arial, 20"))
niButton.grid(row = 3, column = 2, sticky = "we")

gangeButton = tk.Button(root, text = "*", font = ("Arial, 20"))
gangeButton.grid(row = 2, column = 3, sticky = "we")

Button = tk.Button(root, text = "7", font = ("Arial, 20"))
Button.grid(row = 2, column = 0, sticky = "we")











root.mainloop()