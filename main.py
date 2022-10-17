import tkinter as tk 

root = tk.Tk()

svarVindu = tk.Entry(root, font = ("Arial", 20))
svarVindu.grid(row = 0, column = 0,columnspan=4)

ceButton = tk.Button(root, text = "CE", font = ("Arial, 20"))
ceButton.grid(row = 1, column = 0, sticky= "we" )

CButton = tk.Button(root, text = "C", font = ("Arial, 20"))
CButton.grid(row = 1, column = 1, sticky= "we" )

delButton = tk.Button(root, text = "del", font = ("Arial, 20"))
delButton.grid(row = 1, column = 2,  sticky = "we")

pwrButton = tk.Button(root, text = "pwr", font = ("Arial, 20"))
pwrButton.grid(row = 1, column = 3, sticky = "we")


syvButton = tk.Button(root, text = "7", font = ("Arial, 20"))
syvButton.grid(row = 2, column = 0, sticky = "we")

åtteButton = tk.Button(root, text = "8", font = ("Arial, 20"))
åtteButton.grid(row = 2, column = 1, sticky = "we")




niButton = tk.Button(root, text = "9", font = ("Arial, 20"))
niButton.grid(row = 2, column = 2, sticky = "we")

gangeButton = tk.Button(root, text = "*", font = ("Arial, 20"))
gangeButton.grid(row = 2, column = 3, sticky = "we")

fireButton = tk.Button(root, text = "4", font = ("Arial, 20"))
fireButton.grid(row = 3, column = 0, sticky = "we")
femButton = tk.Button(root, text = "5", font = ("Arial, 20"))
femButton.grid(row = 3, column = 1, sticky = "we")

seksButton = tk.Button(root, text = "6", font = ("Arial, 20"))
seksButton.grid(row = 3, column = 2, sticky = "we")

plusButton = tk.Button(root, text = "+", font = ("Arial, 20"))
plusButton.grid(row = 3, column = 3, sticky = "we")

enButton = tk.Button(root, text = "1", font = ("Arial, 20"))
enButton.grid(row = 4, column = 0, sticky = "we")

toButton = tk.Button(root, text = "2", font = ("Arial, 20"))
toButton.grid(row = 4, column = 1, sticky = "we")

treButton = tk.Button(root, text = "3", font = ("Arial, 20"))
treButton.grid(row = 4, column = 2, sticky = "we")

plusButton = tk.Button(root, text = "-", font = ("Arial, 20"))
plusButton.grid(row = 4, column = 3, sticky = "we")

nullButton = tk.Button(root, text = "0", font = ("Arial, 20"))
nullButton.grid(row = 5, column = 0, sticky = "we")

kommaButton = tk.Button(root, text = ",", font = ("Arial, 20"))
kommaButton.grid(row = 5, column = 1, sticky = "we")
erlikButton = tk.Button(root, text = "=", font = ("Arial, 20"))
erlikButton.grid(row = 5, column = 2, sticky = "we")

delingButton = tk.Button(root, text = "/", font = ("Arial, 20"))
delingButton.grid(row = 5, column = 3, sticky = "we")









root.mainloop()
