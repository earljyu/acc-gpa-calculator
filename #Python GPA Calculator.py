# Python GPA Calculator for Austin Community College.

def main():
    '''Prompts the user to input their class grades and respective credit hours for the semester; prints the user's semester total credit hours, average grade, and GPA.
    '''

    print("\nThis is a Python GPA Calculator for Austin Community College students.\n\n***WARNING***\n\nThe GPA calculated is based on Austin Community College's scale. If you do not attend Austin Community College, the GPA calculated may not be accurate!\n")

    # Stores the user's amount of classes into the variable course_total
    course_total = int(
        input("Enter the amount of courses you took this semester: "))

    # Establishes the grades and credit_hours lists; specifies their length
    grades = [0] * course_total

    credit_hours = [0] * course_total

    # Counter variable used in the following for loop. Represents the class number.
    class_number = 0

    # This for loop prompts the user to enter their grades and credit hours. They are assigned to indexes in the established lists.
    for index in range(course_total):
        class_number += 1
        grades[index] = float(
            input(f"Grade earned for class #{class_number}: "))
        credit_hours[index] = int(
            input(f"Credit hours attempted for class #{class_number}: "))

    # Establishes average_grade and assigns it the returned value from passing the list grades into average().
    average_grade = average(grades)

    # Establishes grade_points and assigns it the value returned from passing the list grades into grade_point_assigner().
    grade_points = grade_point_assigner(grades)

    # Establishes total_hours and assigns it the value returned from passing the list credit_hours into total_credit_hours().
    total_hours = total_credit_hours(credit_hours)

    # Establishes total_grade_points and assigns it the value returned from grade_point_calculator() with grade_points, credit_hours, and course_total as arguments.
    total_grade_points = grade_point_calculator(
        grade_points, credit_hours, course_total)

    # Establishes semester_gpa and assigns it the value returned from calculate_gpa() with total_grade_points and total_hours as arguments.
    semester_gpa = calculate_gpa(total_grade_points, total_hours)

    # Prints the user's total credit hours, average grade, and GPA; they are formatted to two decimal points.
    print(
        f"\n\n\nThanks for inputting your grades!\n\n\nThis semester, you've taken {total_hours:.2f} credit hours.\n\n\nYour average grade was {average_grade:.2f}.\n\n\nYour current semester GPA is: {semester_gpa:.2f}.\n\n\nHave a great day!")


def average(list):
    '''Calculates the average of a list by dividing it's sum by it's length.

    Parameters
    list : list
      any list object.

    Return
    average : float 
      average of the given list.
    '''
    total = sum(list)
    average = total / len(list)
    return average


def calculate_gpa(total_points, hours):
    '''Calculates the gpa by dividing the total grade points by total credit hours.

    Parameters
    total_points : float
      The total amount of grade points earned by the user.
    hours : int
      The total amount of credit hours taken by the user.

    Return
    gpa : float
      The user's Grade Point Average(GPA).
    '''
    gpa = total_points / hours
    return gpa


def total_credit_hours(credit_hours):
    '''Calculates the total amount of credit hours taken by calling the sum function on the credit hours list.

    Parameters
    credit_hours : list
      A list containing credit hours.

    Return
    total_hours : int
      The total amount of credit hours taken in the semester. The sum of the credit hours list.
    '''
    total_hours = sum(credit_hours)
    return total_hours


def grade_point_calculator(grades, hours, courses):
    '''Calculates the amount of total grade points. After establishing an accumulator variable, it loops through each course, multiplying the grade by credit hour earned, and adds the product to the accumulator; represents the total grade points.

    Parameters
    grades : list
      A list of the user's grades.
    hours : list
      A list of each course's credit hours.
    courses : int
      The amount of courses taken. 

    Return
    grade_points : float 
      The total amount of grade points earned.
    '''
    grade_points = 0
    for index in range(courses):
        single_class = grades[index] * hours[index]
        grade_points += single_class
    return grade_points


def grade_point_assigner(grades):
    '''Returns a list containing the grade point equivalent of each grade.

    Parameters
    grades : list
      The list of grades earned.

    Return
    grade_point_list : list
      List of grade point equivalents.
    '''
    grade_point_list = []
    grade_point_list += grades

    for index in range(len(grades)):
        if grade_point_list[index] >= 90.0:
            grade_point_list[index] = 4.0
        elif grade_point_list[index] >= 80.0:
            grade_point_list[index] = 3.0
        elif grade_point_list[index] >= 70.0:
            grade_point_list[index] = 2.0
        elif grade_point_list[index] >= 60.0:
            grade_point_list[index] = 1.0
        else:
            grade_point_list[index] = 0
    return grade_point_list


# Runs if module is a standalone script.
if __name__ == "__main__":
    main()
