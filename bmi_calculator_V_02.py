# ToDo: Build the gui for the BMI-calculator

import tkinter as tk

"""
input_weight = int(input("Was ist Ihr Körpergewicht in Kilogramm?: "))
input_height = float(input("Was ist Ihre Körpergröße in Meter?: "))

print("Körpergewicht: ", input_weight)
print("Körpergröße: ", input_height)

bmi_result = input_weight / input_height ** 2

if bmi_result < 18.5:
    print("Untergewicht")
elif bmi_result >= 18.5 and bmi_result <= 24.9:
    print("Normalgewicht")
elif bmi_result >= 25 and bmi_result <= 34.9:
    print("Übergewicht")
else:
    print("Starkes oder extremes Übergewicht")

print("Hinweis: Der BMI dient lediglich einer Einschätzung, hat aber keinen Anspruch auf Richtigkeit.\n"
      "Sind Sie beispielsweise sehr muskolös, kann eine Einschätzung in die Kategorie 'Übergewicht' erfolgen.")
      
"""

window = tk.Tk()

title = tk.Label(text = "Wilkommen in meinem BMI-Rechner.",
                 bg = "#c2c2c2",
                 font = ("Calibri", 14),
                 height = 4,
                 width = 50
                 )

# spacers to make gui look less crowded

spacer = tk.Label(bg = "#dedede",
                   height = 1,
                   width = 72)

spacer_1 = tk.Label(bg = "#dedede",
                   height = 1,
                   width = 72)

spacer_2 = tk.Label(bg = "#dedede",
                    height = 1,
                    width = 72)

# title and input fields

weight_title = tk.Label(text = "Ihr Körpergewicht in Kilogramm: ",
                        bg = "#dedede",
                        font = ("Calibri", 14),
                        width = 25
                        )

weight_entry = tk.Entry(font = ("Calibri",14),
                        width = 25
                        )

height_title = tk.Label(text = "Ihre Körpergröße in Metern: ",
                        bg = "#dedede",
                        font = ("Calibri", 14),
                        width = 25
                        )

height_entry = tk.Entry(font = ("Calibri", 14),
                        width = 25
                        )
# function to calculate
def output_calc():
    input_weight = float(weight_entry.get())
    input_height = float(height_entry.get())
    middle = input_weight / input_height ** 2
    output_number = round(middle, 2)

    if output_number < 18.5:
        output = "Untergewicht"
        output_field.config(text= output)
    elif output_number >= 18.5 and output_number <= 24.9:
        output ="Normalgewicht"
        output_field.config(text= output)
    elif output_number >= 25 and output_number <= 34.9:
        output = "Übergewicht"
        output_field.config(text= output)
    else:
        output = "Starkes oder extremes Übergewicht"
        output_field.config(text= output)


converter_button = tk.Button(text = "BMI errechnen",
                             font = ("Calibri", 14),
                             command = output_calc
                             )

output = ""
output_number = ""

output_field = tk.Label(text = output,
                        font = ("Calibri", 14),
                        height = 2,
                        width = 50,
                        bd = 2,
                        relief = "solid",
                        bg = "#dedede"
                        )

hinweis_field = tk.Label(text="Hinweis: Der BMI dient lediglich einer Einschätzung,\n"
                              "hat aber keinen Anspruch auf Richtigkeit.\n"
                              "Sind Sie beispielsweise sehr muskolös, kann fälsch- \n"
                              "lich eine Einschätzung in die Kategorie 'Übergewicht' erfolgen.",
                         bg = "#c2c2c2",
                         font = ("Calibri", 14),
                         height = 4,
                         width = 50)

title.grid(row=0, column=0, columnspan=4)
spacer.grid(row=1, column=0, columnspan=4)
weight_title.grid(row=2, column=0, columnspan=2)
weight_entry.grid(row=2, column=2, columnspan=2)
height_title.grid(row=3, column=0, columnspan=2)
height_entry.grid(row=3, column=2, columnspan=2)
spacer_1.grid(row=4, column=0, columnspan=4)
converter_button.grid(row=5, column =1, columnspan=2)
spacer_2.grid(row=6, column=0, columnspan=4)
output_field.grid(row=7, column=0, columnspan=4)
hinweis_field.grid(row=8, column=0, columnspan=4)

window.mainloop()