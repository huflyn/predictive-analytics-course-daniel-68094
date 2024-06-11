# Task 01
# Write a script that asks for your age, height and weight
# Make sure, that data is input correctly by checking types
# Compute [body mass index](https://en.wikipedia.org/wiki/Body_mass_index) and ouput result
# program shall comment (politely) on results



def ask_for(datafield, value_type, min_value, max_value):   # ask_for(wonach wird gefragt, Datentyp int oder float, Minimalwert, Maximalwert) 
    reading_done = False
    error_count = 0   # Fehlercounter für ungültige Eingaben
    while not reading_done:   # Schleife solange kein gültiger Wert eingegeben wurde
        try:
            myRead = input(f"Please let me know your {datafield}: ")
            myRead = myRead.replace(",", ".")   # "," in "." umwandeln, da Dezimalzahlen mit Punkt getrennt werden
            myRead = value_type(myRead)
            if (min_value is not None and myRead < min_value) or (max_value is not None and myRead > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
                error_count += 1
            else:
                reading_done = True
                return myRead
        except ValueError:
            print("This is not a number, please try again")
            error_count += 1

        if error_count >= 5:   # Abbruch nach x falschen Eingaben
            print("Too many invalid attempts. Program will terminate.")
            exit()

age = ask_for("age", int, 1, 150)
height = ask_for("height in centimeters", int, 1, 300)
weight = ask_for("weight in kg", float, 0.1, 500)

bmi = weight / ((height / 100) ** 2)
print(f"BMI: {bmi:.2f}")