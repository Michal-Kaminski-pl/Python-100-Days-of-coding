import tkinter
def button_click():
    value_in_miles = input.get()
    value_in_km = round(float(value_in_miles) * 1.61, 2)
    value_in_km_label.config(text=value_in_km)
window = tkinter.Tk()
window.minsize(width=200, height=100)
window.config(padx= 30, pady= 50)
## napisy
is_equal_label = tkinter.Label(text="is equal to", font = ("Arial", 12, "bold"))
is_equal_label.grid(row=1, column=0)

miles_label = tkinter.Label(text="Miles", font = ("Arial", 12, "bold"))
miles_label.grid(row=0, column=2)

km_label = tkinter.Label(text="Kilometers", font = ("Arial", 12, "bold"))
km_label.grid(row=1, column=2)

value_in_km_label = tkinter.Label(text="0", font = ("Arial", 12, "bold"))
value_in_km_label.config(padx= 20, pady=20)
value_in_km_label.grid(row = 1, column = 1)

## entry
input = tkinter.Entry(width=10)
input.insert(string="0", index=0)
input.grid(row=0, column=1)
## button

button = tkinter.Button(text="Calculate", command=button_click)
button.grid(row = 2, column= 1)
window.mainloop()