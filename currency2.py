import requests
from tkinter import *

api_key = "3a60b2730b06fee2b625c0fc91997344"
url = "http://data.fixer.io/api/latest?access_key=" + api_key


def show_entry_fields():
    # print("First Currency: %s\nSecond Currency: %s" % (e1.get(), e2.get()))
    first_currency = e1.get()
    second_currency = e2.get()
    amount = e3.get()
    response = requests.get( url )
    infos = response.json()
    firstValue = infos["rates"][first_currency]
    secondValue = infos["rates"][second_currency]

    result = str( (secondValue / firstValue) * float( amount ) )

    lbl.configure( text="RESULT : " + result + " " + e2.get() )


master = Tk()
master.title( "HAKKI's Currency Calculator" )

Label( master, fg="blue", text="Currency 1", font=('Tahoma 12') ).grid( row=0 )
Label( master, fg="red", text="Currency 2", font=('Tahoma 12') ).grid( row=1 )
Label( master, fg="orange", bg="white", text="Amount", font=('Tahoma 13') ).grid( row=2 )

lbl = Label( master, bg="brown", fg="white", text="RESULT :      ", font=('Tahoma 13') )
lbl.grid( column=1, row=6 )

e1 = Entry( master )
e2 = Entry( master )


def e3_clearer():
    e3.delete( first=0, last=22 )


e3 = Entry( master, width=20 )

e1.grid( row=0, column=1 )
e2.grid( row=1, column=1 )
e3.grid( row=2, column=1 )

response = requests.get( url )
infos = response.json()

Button( master, text='Quit', command=master.destroy ).grid( row=5, column=2, sticky=W, pady=5, padx=15 )
Button( master, text='Clear', command=e3_clearer ).grid( row=5, column=1, sticky=W, pady=5, padx=35 )
Button( master, text='Convert', command=show_entry_fields ).grid( row=5, column=0, sticky=W, pady=5, padx=15 )

master.mainloop()