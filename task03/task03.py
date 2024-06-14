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

# Function to ask for data
def ask_for(datafield, value_type, min_value, max_value):
    reading_done = False
    error_count = 0
    while not reading_done:
        try:
            myRead = input(f"Please let me know your {datafield}: ")
            myRead = myRead.replace(",", ".")
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

        if error_count >= 5:   # Exit program after x continues wrong inputs
            print("Too many invalid attempts. Program will terminate.")
            exit()

# Function for BMI classification
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

filename = "bmi.csv"

# check if file exists
file_exists = False
try:
    with open(filename, "r") as csvfile:  # open file in read mode
        reader = csv.reader(csvfile)  
        file_exists = any(reader)
except FileNotFoundError:
    pass  # continues program w/o any action

# write data in csv file
with open(filename, "a") as csvfile:  # open file in attach mode, adds data w/o deleting previous data
    writer = csv.writer(csvfile)
    if not file_exists:
        writer.writerow(["Name", "Age", "Height", "Weight", "BMI", "Category"])  # writes headers
    writer.writerow([name, age, height, weight, bmi_category(bmi)])  # writes data in a line

print(f"{name} wurde in {filename} gespeichert.")