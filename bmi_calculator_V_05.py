import customtkinter

# general settings for appearance of gui

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()

app.geometry("430x350")

app.title("Wilkommen in meinem BMI-Rechner.")

frame1 = customtkinter.CTkFrame(master=app, fg_color="#ad3f37", border_color="#240d0c", border_width=2)

hinweis_label = customtkinter.CTkLabel(master = frame1, text = "Hinweis: Der BMI dient lediglich einer Einschätzung,\n"
                                                               "hat aber keinen Anspruch auf Richtigkeit.\n"
                                                               "Sind Sie beispielsweise sehr muskolös, kann fälsch- \n"
                                                               "lich eine Einschätzung in die Kategorie 'Übergewicht' erfolgen.")

frame2 = customtkinter.CTkFrame(master=app)
weight_title = customtkinter.CTkLabel(master=frame2, text = "Ihr Körpergewicht in Kilogramm: ", )
weight_entry = customtkinter.CTkEntry(master=frame2, placeholder_text = "z.B.: 90.6")

height_title = customtkinter.CTkLabel(master=frame2, text = "Ihre Körpergröße in Metern: ")
height_entry = customtkinter.CTkEntry(master=frame2, placeholder_text = "z.B.: 1.85")

# function behind button press to calculate bmi
def output_calc():

    # getting input from input fields

    input_weight_raw = weight_entry.get()
    input_height_raw = height_entry.get()

    # transforming commas to dots for german users

    input_weight_dot = input_weight_raw.replace(",", ".")
    input_height_dot = input_height_raw.replace(",", ".")

    # input getting transformed to float so they can be used in math operations

    input_weight = float(input_weight_dot)
    input_height = float(input_height_dot)

    # math logic of bmi

    middle = input_weight / input_height ** 2
    output_number = round(middle, 2)

    # determining result

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

# defining variables for the coming modules

output = "Hier erscheint Ihr Ergebnis"
output_number = ""

# output and button

frame3 = customtkinter.CTkFrame(app, fg_color = "#383838")
output_field = customtkinter.CTkLabel(frame3, text = output, width = 340, font = ("", 15))

converter_button = customtkinter.CTkButton(app,
                                           text = "BMI berechnen",
                                           command = output_calc,
                                           hover_color = "#447ec9",
                                           height = 40,
                                           width = 130,
                                           font = ("", 15))

# layout for all the modules

frame1.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 10)
hinweis_label.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 10)
frame2.grid(row = 1, column = 1, columnspan = 2, padx = 20, pady = 5)
weight_title.grid(row = 2, column = 0, padx = 10, pady = 10)
weight_entry.grid(row = 2, column = 1, padx = 20, pady = 10)
height_title.grid(row = 3, column = 0, padx = 10, pady = 10)
height_entry.grid(row = 3, column = 1, padx = 20, pady = 10)
converter_button.grid (row = 4, column = 0, columnspan = 2, padx = 10, pady = 10)
frame3.grid(row = 5, column = 0, columnspan = 2, padx = 20, pady = 10)
output_field.grid(row = 5, column = 1, padx = 20, pady = 10)

app.mainloop()