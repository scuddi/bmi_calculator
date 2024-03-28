import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()

app.geometry("600x400")

app.title("Wilkommen in meinem BMI-Rechner.")

weight_title = customtkinter.CTkLabel(app, text = "Ihr Körpergewicht in Kilogramm: ")
weight_entry = customtkinter.CTkEntry(app)

height_title = customtkinter.CTkLabel(app, text = "Ihre Körpergröße in Metern: ")
height_entry = customtkinter.CTkEntry(app)

def output_calc():
    input_weight = float(weight_entry.get())
    input_height = float(height_entry.get())
    middle = input_weight / input_height ** 2
    output_number = round(middle, 2)

    if output_number < 18.5:
        output = "Untergewicht"
        output_field.configure(text= output)
    elif output_number >= 18.5 and output_number <= 24.9:
        output ="Normalgewicht"
        output_field.configure(text= output)
    elif output_number >= 25 and output_number <= 34.9:
        output = "Übergewicht"
        output_field.configure(text= output)
    else:
        output = "Starkes oder extremes Übergewicht"
        output_field.configure(text= output)

output = ""
output_number = ""

output_field = customtkinter.CTkLabel(app, text = output)

converter_button = customtkinter.CTkButton(app, text = "BMI berechnen", command = output_calc)

weight_title.grid(row = 0, column = 0, padx = 10, pady = 10)
weight_entry.grid(row = 0, column = 1)
height_title.grid(row = 1, column = 0)
height_entry.grid(row = 1, column = 1)
converter_button.grid (row = 2, column = 0, columnspan = 2)
output_field.grid(row = 3, column = 1, columnspan = 2)


app.mainloop()


"""

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

"""