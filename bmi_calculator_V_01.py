# ToDo: Basic functions of a BMI-calculator here in the terminal

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