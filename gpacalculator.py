
unweighted_gpa_list = []
weighted_gpa_list = []
"""
GPA Calculator. Options for...
- Calculating Quarter GPA off of summative and formative grades.
- Calculating Semester GPA off of Semester Grade
- Can calculate both unweighted and weighted GPA. - Currently Unfinished. 
"""
from rich import print
from rich.prompt import Prompt
from rich.console import Console
import time
print("Welcome to the GPA Calculator!(North Hills Values)")
q1 = input("Do you want to calcuate unweighted or weighted GPA? Answer w for Weighted and u for Unweighted.\n").lower()
while q1 != "w" and q1 != "u":
    print("[red]That is not a valid answer![/red]")
    q1 = input("Please type U or W for unweighted or weighted GPA.\n")

def unweighted():
    #Calculates unweighted GPA 
    q2 = input("Are there summatives in the grade book. Type Y for Yes and N for No.\n").lower()
    while q2 != "y" and q2 != "n":
        print("This is not a valid answer!")
        q2 = input("Type Y if there are summatives and N if there aren't.").lower()
    if q2 == "y":
        summative = []
        while True:
            try:
                q3 = int(input("Type a summative grade.\n"))
                if 0 <= q3 <= 100:
                    summative.append(q3)
                    break 
                else:
                    print("That is not a valid answer! Must be between 0 and 100.")
            except ValueError:
                print("That is not a valid answer! Please enter a number.")
        while True:
            q3 = input("Type another summative grade or click enter to end.\n")
            if q3 == "":
                print("All summatives have been entered...")
                break
            try:
                q3 = int(q3)
                if 0 <= q3 <= 100:
                    summative.append(q3)
                else:
                    print("That is not a valid answer! Must be between 0 and 100.")
            except ValueError:
                print("That is not a valid answer! Please enter a number.")
        count = len(summative)
        sumaverage =((sum(summative))/count)
        if sumaverage.is_integer():
            sumaverage = int(sumaverage)
        sumaverage = round(sumaverage, 2)
        print(f"Your summative average is {sumaverage}.")
        #end of summative, starting formative
        formative = []
        while True:
            try:
                q4 = int(input("Type a formative grade.\n"))
                if 0 <= q4 <= 100:
                    formative.append(q4)
                    break 
                else:
                    print("That is not a valid answer! Must be between 0 and 100.")
            except ValueError:
                print("That is not a valid answer! Please enter a number.")
        while True:
            q4 = input("Type another formative grade or click enter to end.\n")
            if q4 == "":
                print("All formatives have been entered...")
                break
            try:
                q4 = int(q4)
                if 0 <= q4 <= 100:
                    formative.append(q4)
                else:
                    print("That is not a valid answer! Must be between 0 and 100.")
            except ValueError:
                print("That is not a valid answer! Please enter a number.")
        count = len(formative)
        formaverage =((sum(formative))/count)
        formaverage = round(formaverage, 2)
        print(f"Your formative average is {formaverage}.")
        print("Combining average...")
        time.sleep(1)
        average = (formaverage*0.4)+(sumaverage*0.6)
        print(f"Your average is a {average}.")
        return average
    else:
        formative = []
        while True:
            try:
                q4 = int(input("Type a formative grade.\n"))
                if 0 <= q4 <= 100:
                    formative.append(q4)
                    break 
                else:
                    print("That is not a valid answer! Must be between 0 and 100.")
            except ValueError:
                print("That is not a valid answer! Please enter a number.")
        while True:
            q4 = input("Type another formative grade or click enter to end.\n")
            if q4 == "":
                print("All formatives have been entered...")
                break
            try:
                q4 = int(q4)
                if 0 <= q4 <= 100:
                    formative.append(q4)
                else:
                    print("That is not a valid answer! Must be between 0 and 100.")
            except ValueError:
                print("That is not a valid answer! Please enter a number.")
        count = len(formative)
        formaverage =((sum(formative))/count)
        if formaverage.is_integer():
            formaverage = int(formaverage)
        print(f"Your formative average is {formaverage}.")
        average = formaverage
        return average
def unweightedgpa(average):
    global unweighted_gpa_list
    if 93 < average <= 100:
        print("Your GPA is a 4.0!")
        Unweighted_GPA = 4.0
    elif 90 <= average < 93:
        print("Your GPA is a 3.7!")
        Unweighted_GPA = 3.7
    elif 87 <= average < 90:
        print("Your GPA is 3.3!")
        Unweighted_GPA = 3.3
    elif 83 <= average < 87:
        print("Your GPA is a 3.0!")
        Unweighted_GPA = 3.0
    elif 80 <= average < 83:
        print("Your GPA is a 2.7.")
        Unweighted_GPA = 2.7
    elif 77 <= average < 80:
        print("Your GPA is a 2.3.")
        Unweighted_GPA = 2.3
    elif 73 <= average < 77:
        print("Your GPA is a 2.0.")
        Unweighted_GPA = 2.0
    elif 70 <= average < 73:
        print("Your GPA is a 1.7.")
        Unweighted_GPA = 1.7
    else:
        print("Your GPA is a 0.")
        Unweighted_GPA = 0.0
    unweighted_gpa_list.append(Unweighted_GPA)
    while True:
        print('Would you like to run this code again with other classes to find your average unweighted GPA across classes?')
        q6 = input("Enter 'y' for yes and 'n' for no.\n").lower()
        if q6 == 'y':
            print("Rerunning program...")
            print("")
            semester_unweighted_gpa()
        else:
            number_unweighted_GPA = len(unweighted_gpa_list)
            GPA_Average_Unweighted = ((sum(unweighted_gpa_list))/number_unweighted_GPA)
            print(f"Your overall semester unweighted GPA is a {GPA_Average_Unweighted}.")
            break
def semester_unweighted_gpa():#error here, line 168, need while true to stop incorrect answers
    global q1
    if q1 == "u":
        q5 = input("Do you want to calculate your unweighted GPA with your current semester average? Type Y for Yes and N for No.\n").lower()
        while q5 != "y" and q5 != "n":
            print("[red]That is not a valid answer![/red]")
            q5 = input("Enter Y or N.\n").lower()
        if q5 == 'y':
            while True:
                semestergrade = input("Enter the semester average (0–100): ")
                try:
                    semestergrade = int(semestergrade)
                    if 0 <= semestergrade <= 100:
                        break 
                    else:
                        print("[red]Please enter a number between 0 and 100.[/red]")
                except ValueError:
                    print("[red]That is not a valid number! Please enter an integer.[/red]")
            unweightedgpa(semestergrade)
            quit()
        else:
            print("[bold green]Moving on through program...[/bold green]")
    if q1 == 'u':
        average = unweighted() #calculates unweighted GPA based off average in unweighted GPA section.
        unweightedgpa(average)
def weighted():
    #Calculates Weighted GPA 
    q2 = input("Are there summatives in the grade book. Type Y for Yes and N for No.\n").lower()
    while q2 != "y" and q2 != "n":
        print("This is not a valid answer!")
        q2 = input("Type Y if there are summatives and N if there aren't.").lower()
    if q2 == "y":
        summative = []
        while True:
            try:
                q3 = int(input("Type a summative grade.\n"))
                if 0 <= q3 <= 100:
                    summative.append(q3)
                    break 
                else:
                    print("That is not a valid answer! Must be between 0 and 100.")
            except ValueError:
                print("That is not a valid answer! Please enter a number.")
        while True:
            q3 = input("Type another summative grade or click enter to end.\n")
            if q3 == "":
                print("All summatives have been entered...")
                break
            try:
                q3 = int(q3)
                if 0 <= q3 <= 100:
                    summative.append(q3)
                else:
                    print("That is not a valid answer! Must be between 0 and 100.")
            except ValueError:
                print("That is not a valid answer! Please enter a number.")
        count = len(summative)
        sumaverage =((sum(summative))/count)
        if sumaverage.is_integer():
            sumaverage = int(sumaverage)
        sumaverage = round(sumaverage, 2)
        print(f"Your summative average is {sumaverage}.")
        #end of summative, starting formative
        formative = []
        while True:
            try:
                q4 = int(input("Type a formative grade.\n"))
                if 0 <= q4 <= 100:
                    formative.append(q4)
                    break 
                else:
                    print("That is not a valid answer! Must be between 0 and 100.")
            except ValueError:
                print("That is not a valid answer! Please enter a number.")
        while True:
            q4 = input("Type another formative grade or click enter to end.\n")
            if q4 == "":
                print("All formatives have been entered...")
                break
            try:
                q4 = int(q4)
                if 0 <= q4 <= 100:
                    formative.append(q4)
                else:
                    print("That is not a valid answer! Must be between 0 and 100.")
            except ValueError:
                print("That is not a valid answer! Please enter a number.")
        count = len(formative)
        formaverage =((sum(formative))/count)
        formaverage = round(formaverage, 2)
        print(f"Your formative average is {formaverage}.")
        print("Combining average...")
        time.sleep(1)
        average = (formaverage*0.4)+(sumaverage*0.6)
        print(f"Your average is a {average}.")
        return average
    else:
        formative = []
        while True:
            try:
                q4 = int(input("Type a formative grade.\n"))
                if 0 <= q4 <= 100:
                    formative.append(q4)
                    break 
                else:
                    print("That is not a valid answer! Must be between 0 and 100.")
            except ValueError:
                print("That is not a valid answer! Please enter a number.")
        while True:
            q4 = input("Type another formative grade or click enter to end.\n")
            if q4 == "":
                print("All formatives have been entered...")
                break
            try:
                q4 = int(q4)
                if 0 <= q4 <= 100:
                    formative.append(q4)
                else:
                    print("That is not a valid answer! Must be between 0 and 100.")
            except ValueError:
                print("That is not a valid answer! Please enter a number.")
        count = len(formative)
        formaverage =((sum(formative))/count)
        if formaverage.is_integer():
            formaverage = int(formaverage)
        print(f"Your formative average is {formaverage}.")
        average = formaverage
        return average
def weighted_gpa(average):
    global weighted_gpa_list
    Additions = int(input("Enter 1 if your class is a Honors class and 2 if your class is an AP/IB Class. Enter 0 if your class is normal:\n"))
    while True:
        try:
            if Additions == 0 or Additions == 1 or Additions == 2:
                break
            else:
                print("That is not a valid answer!")
        except ValueError:
            print("Enter a number!")

    if 93 < average <= 100:
        if Additions == 2:
            GPA = 5.0
            print(f"Your Weighted GPA is a {GPA}.")
        elif Additions == 1:
            GPA = 4.5
            print(f"Your Weighted GPA is a {GPA}.")
        else:
            GPA = 4.0
            print(f"Your Weighted GPA is a {GPA}.")
    elif 90 <= average < 93:
        if Additions == 2:
            GPA = 4.7
            print(f"Your Weighted GPA is a {GPA}.")
        elif Additions == 1:
            GPA = 4.2
            print(f"Your Weighted GPA is a {GPA}.")
        else:
            GPA = 3.7
            print(f"Your Weighted GPA is a {GPA}.")
    elif 87 <= average < 90:
        if Additions == 2:
            GPA = 4.3
            print(f"Your Weighted GPA is a {GPA}.")
        elif Additions == 1:
            GPA = 3.8
            print(f"Your Weighted GPA is a {GPA}.")
        else:
            GPA = 3.3
            print(f"Your Weighted GPA is a {GPA}.")
    elif 83 <= average < 87:
        if Additions == 2:
            GPA = 4.0
            print(f"Your Weighted GPA is a {GPA}.")
        elif Additions == 1:
            GPA = 3.5
            print(f"Your Weighted GPA is a {GPA}.")
        else:
            GPA = 3.0
            print(f"Your Weighted GPA is a {GPA}.")
    elif 80 <= average < 83:
        if Additions == 2:
            GPA = 3.7
            print(f"Your Weighted GPA is a {GPA}.")
        elif Additions == 1:
            GPA = 3.2
            print(f"Your Weighted GPA is a {GPA}.")
        else:
            GPA = 2.7
            print(f"Your Weighted GPA is a {GPA}.")
    elif 77 <= average < 80:
        if Additions == 2:
            GPA = 3.3
            print(f"Your Weighted GPA is a {GPA}.")
        elif Additions == 1:
            GPA = 2.8
            print(f"Your Weighted GPA is a {GPA}.")
        else:
            GPA = 2.3
            print(f"Your Weighted GPA is a {GPA}.")
    elif 73 <= average < 77:
        if Additions == 2:
            GPA = 3.0
            print(f"Your Weighted GPA is a {GPA}.")
        elif Additions == 1:
            GPA = 2.5
            print(f"Your Weighted GPA is a {GPA}.")
        else:
            GPA = 2.0
            print(f"Your Weighted GPA is a {GPA}.")
    elif 70 <= average < 73:
        if Additions == 2:
            GPA = 2.7
            print(f"Your Weighted GPA is a {GPA}.")
        elif Additions == 1:
            GPA = 2.2
            print(f"Your Weighted GPA is a {GPA}.")
        else:
            GPA = 1.7
            print(f"Your Weighted GPA is a {GPA}.")
    else:
        if Additions == 2:
            GPA = 1.0
            print(f"Your Weighted GPA is a {GPA}.")
        elif Additions == 1:
            GPA = 0.5
            print(f"Your Weighted GPA is a {GPA}.")
        else:
            GPA = 0
            print(f"Your Weighted GPA is a {GPA}.")
    weighted_gpa_list.append(GPA)
    while True:
        print('Would you like to run this code again with other classes to find your average Weighted GPA across classes?')
        q6 = input("Enter 'y' for yes and 'n' for no.\n").lower()
        if q6 == 'y':
            print("Rerunning program...")
            print("")
            semester_weighted_gpa()
        else:
            number_weighted_GPA = len(weighted_gpa_list)
            GPA_Average_Weighted = ((sum(weighted_gpa_list))/number_weighted_GPA)
            print(f"Your overall semester Weighted GPA is a {GPA_Average_Weighted}.")
            break
def semester_weighted_gpa():
    global q1
    if q1 == "w":
        q5 = input("Do you want to calculate your weighted GPA with your current semester average? Type Y for Yes and N for No.\n").lower()
        while q5 != "y" and q5 != "n":
            print("[red]That is not a valid answer![/red]")
            q5 = input("Enter Y or N.\n").lower()
        if q5 == 'y':
            while True:
                semestergrade = input("Enter the semester average (0–100): ")
                try:
                    semestergrade = int(semestergrade)
                    if 0 <= semestergrade <= 100:
                        break 
                    else:
                        print("Please enter a number between 0 and 100.")
                except ValueError:
                    print("That is not a valid number! Please enter an integer.")
            weighted_gpa(semestergrade) #does GPA calculation using semestergrade instead of normal average
            quit()
        else:
            print("[blue]Moving on through program...[/blue]")
    if q1 == 'w':
        average = weighted() #calculates unweighted GPA based off average in unweighted GPA section.
        weighted_gpa(average)
semester_unweighted_gpa()
semester_weighted_gpa()
