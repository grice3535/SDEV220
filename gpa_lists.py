"""
Auther: Gillian Rice
File Name: gpa_lists.py
Description: This program will determine if a student has made the Dean's List or Honor's List based on their GPA.
"""

while True:
    studLName = str(input("Please enter your last name:"))
    if studLName == "ZZZ":
        break

    studName = str(input("Please enter your first name:"))
    studGPA = float(input("Please enter your GPA:"))

    if studGPA >= 3.5:
        print(studName, studLName, "has made the Dean's List.")
    elif studGPA >= 3.25:
        print(studName, studLName, "has made the Honor's List.")
    else:
        print(studName, studLName, "has not made either list.")


