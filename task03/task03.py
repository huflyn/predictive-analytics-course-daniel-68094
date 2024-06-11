# Task 01
# Write a script that asks for your age, height and weight
# Make sure, that data is input correctly by checking types
# Compute [body mass index](https://en.wikipedia.org/wiki/Body_mass_index) and ouput result
# program shall comment (politely) on results

# Task 03
# Enhance task 01 by:
# ask for a username
# appending every run to a CSV file
# adding a main function such that you can either view collected data so far or run a new data capturing
import csv

# Funktion um nach Daten zu fragen
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

# Funktion zur Klassifikation des BMI
def bmi_category(bmi):
    if bmi < 16.0:
        return "Underweight (Severe thinness)"
    elif 16.0 <= bmi < 17.0:
        return "Underweight (Moderate thinness)"
    elif 17.0 <= bmi < 18.5:
        return "Underweight (Mild thinness)"
    elif 18.5 <= bmi < 25.0:
        return "Normal weight"
    elif 25 <= bmi < 30.0:
        return "Overweight (Pre-obese)"
    elif 30.0 <= bmi < 35.0:
        return "Obese (Class I)"
    elif 35 <= bmi < 40.0:
        return "Obese (Class II)"
    elif bmi >= 40.0:
        return "Obese (Class III)"

name = input(str("Please let me know your username: "))
age = ask_for("age", int, 1, 150)
height = ask_for("height in centimeters", int, 1, 300)
weight = ask_for("weight in kg", float, 0.1, 500)

bmi = weight / ((height / 100) ** 2)
print(f"BMI: {bmi:.2f} - {bmi_category(bmi)}")

filename = "bmi.csv"  # Dateiname der CSV Datei

# Überprüfen, ob die Datei existiert und ob sie den Header enthält
file_exists = False
try:
    with open(filename, "r") as csvfile:  # öffnet die Datei filename im Lesemodus und weist sie der Variablen csvfile zu. Der with-Kontextmanager stellt sicher, dass die Datei korrekt geschlossen wird, nachdem der Block beendet ist.
        reader = csv.reader(csvfile)  # Ein csv.reader-Objekt wird erstellt, das die Datei csvfile liest.
        file_exists = any(reader)  # any(reader) prüft, ob der reader Daten enthält. Falls Datei leer kommt False zurück, falls nicht True.
except FileNotFoundError:  # Falls die Datei nicht existiert, wird eine FileNotFoundError-Ausnahme ausgelöst.
    pass  # Programm wird einfach fortgesetzt, ohne eine Aktion auszuführen

# Daten in die CSV-Datei schreiben
with open(filename, "a", newline='') as csvfile:  # Anhängemodus ('a') bedeutet, dass neue Daten an das Ende der Datei angehängt werden, ohne bestehende Daten zu überschreiben
    writer = csv.writer(csvfile)  # newline='' stellt sicher, dass keine zusätzlichen Leerzeilen zwischen den geschriebenen Zeilen eingefügt werden
    if not file_exists:
        writer.writerow(["Name", "Age", "Height", "Weight", "BMI", "Category"])  # writer.writerow(['Name']) schreibt eine Zeile mit dem Header Name in die CSV-Datei. Header wird nur einmal geschrieben.
    writer.writerow([name, age, height, weight, bmi_category(bmi)])  # Schreibt eine Zeile mit dem eingegebenen Wert in die Datei.

print(f"{name} wurde in {filename} gespeichert.")