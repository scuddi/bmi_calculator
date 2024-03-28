import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()

app.geometry("375x280")

app.title("Wilkommen in meinem BMI-Rechner.")

hinweis_label = customtkinter.CTkLabel(master = app, text = "Hinweis: Der BMI dient lediglich einer Einschätzung,\n"
                                                   "hat aber keinen Anspruch auf Richtigkeit.\n"
                                                   "Sind Sie beispielsweise sehr muskolös, kann fälsch- \n"
                                                   "lich eine Einschätzung in die Kategorie 'Übergewicht' erfolgen.")

weight_title = customtkinter.CTkLabel(app, text = "Ihr Körpergewicht in Kilogramm: ", )
weight_entry = customtkinter.CTkEntry(app, placeholder_text = "z.B.: 90.6")

height_title = customtkinter.CTkLabel(app, text = "Ihre Körpergröße in Metern: ")
height_entry = customtkinter.CTkEntry(app, placeholder_text = "z.B.: 1.85")

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

converter_button = customtkinter.CTkButton(app,
                                           text = "BMI berechnen",
                                           command = output_calc,
                                           hover_color = "#447ec9")

hinweis_label.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5, sticky="nsew")
weight_title.grid(row = 1, column = 0, padx = 10, pady = 10)
weight_entry.grid(row = 1, column = 1)
height_title.grid(row = 2, column = 0, padx = 10, pady = 10)
height_entry.grid(row = 2, column = 1)
converter_button.grid (row = 3, column = 0, columnspan = 2, padx = 10, pady = 10)
output_field.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 10)


app.mainloop()