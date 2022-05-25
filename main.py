from tkinter import *


def buttoned_clicked():
    conversion = round(1.60934 * float(user_input.get()), 2)
    value_label.config(text=f"{conversion}")


window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=350, height=200)

# Label
first_label = Label(text="is equal to", font=("Ariel", 12, "bold"))
first_label.place(x=50, y=100)
first_label.config(padx=10, pady=10)
# miles label
miles_label = Label(text="Miles", font=("Ariel", 12, "bold"))
miles_label.place(x=225, y=55)
miles_label.config(padx=10, pady=10)
# value label
value_label = Label(text="0", font=("Ariel", 12, "bold"))
value_label.place(x=150, y=100)
value_label.config(padx=10, pady=10)
# kilometer label
km_label = Label(text="Km", font=("Ariel", 12, "bold"))
km_label.place(x=225, y=100)
km_label.config(padx=10, pady=10)
# Button
button = Button(text="Calculate", command=buttoned_clicked)
button.place(x=150, y=140)
button.config(padx=10, pady=10)

# Entry
user_input = Entry(width=10)
user_input.place(x=150, y=70)
print(user_input.get())

window.mainloop()
