
"""
This program allows the user to create a register of students for an exam venue.

It asks the user for:
- venue name
- number of registered students
- student ID numbers

A .txt file is created to register the students sitting their exam at the specified venue.
This file can then be used as an attendance sheet for the exam.

"""


# Define function for asking the user if they want to continue using the program or to exit.
def continue_or_exit():

    user_choice = input("\nWould you like to create a new register? Enter 'y' or 'n':\t")
    user_choice = user_choice.lower()

    while user_choice != 'y':
        # If user chooses no, print exit message and return True (to done variable).
        if user_choice == 'n':
            print("\nOk, goodbye.\n")
            return True
        
        # Input validation - prompt the user to enter only 'y' or 'n' in answer to the question.
        else:
            user_choice = input("\n**** Invalid Entry ****\tPlease enter 'y' or 'n':\t")
            user_choice = user_choice.lower()
    
    # If user chooses yes, return False (to done variable).
    return False


# Define function for asking the user if the input they have entered is correct.
def input_validation(user_entry, entry_descriptor):

    # Ask if the user_entry is correct, give "yes" or "no" options.
    entry_check = input(f"\nYou entered \"{user_entry}\". Please confirm, 'y' or 'n':\t")
    entry_check = entry_check.lower()

    # If the correct value is confirmed by the user, this loop is not entered.
    while entry_check != 'y':

        # If the entry is incorrect, allow the user to enter a new value.
        if entry_check == 'n':
            user_entry = input(f"\nPlease enter the correct {entry_descriptor}:\t")

            # Check again if the new value the user has entered is correct.
            entry_check = input(f"\nYou entered \"{user_entry}\". Please confirm, 'y' or 'n':\t")

        # Input validation - prompt the user to choose either 'y' or 'n' only to answer the question.
        else:
            entry_check = input("\n**** Invalid Entry ****\tPlease enter 'y' or 'n':\t")
        
        entry_check = entry_check.lower()

    # When the user is satisfied with the user_entry, return user_entry.
    return user_entry


# Define function to validate numeric inputs. (Descriptor = "no. of students", "position in list" etc.)
def numeric_input_checker(num_input, num_descriptor):

    # Ask the user if they have entered the desired value, and allow them to change it as needed.
    num_input = input_validation(num_input, "number")

    # If the num_input is not numeric or not a number above 0, show an error message.
    while not num_input.isnumeric() or int(num_input) < 0:
        print("\n**** Invalid Entry ****\n")

        # Ask the user to enter a number in the correct range.
        num_input = input(f"Please enter the correct {num_descriptor}:\t")

        # Ask the user if they have entered the desired value, and allow them to change it as needed.
        num_input = input_validation(num_input, "number")

    # Once the num_input is correct and has been validated, return it as an int.
    return int(num_input)
    

# Define a function to check if an index is within the range of a list.
def list_range_checker(user_list, index_input):

    # If the index_input is not numeric or not within the list range, show an error message.
    while (not index_input.isnumeric()) or (int(index_input) < 0) or (int(index_input) > len(user_list)):

        print("\n**** Invalid Entry - not within the specified range ****\n")
        # Ask for another number.
        index_input = input("Please enter a number within the list:\t")
        # Ask if the user if the new input is correct, allow them to change it if needed.
        index_input = input_validation(index_input, "position in the list")

    return int(index_input)





# Greet the user and explain the purpose of the program.
print("Welcome to the Exam Venue Register Creator")
print("-"*90)
print("For each exam venue, this program will allow you to create a register of allocated students.")



# Declare divider and signature line, for later use in writing to reg_form.txt to aid readability.
divider = "_"*40
signature_line = "."*30



# Set done variable to False, to be used to control continuing/exiting the program.
done = False

# Ask the user if they wish to create a new venue register, and give the option to exit.
done = continue_or_exit()

# If the user chooses to continue, create a new register for an exam venue.
while not done:


    # Ask the user to input the name of the exam venue, then validate the input.
    exam_venue = input("\nPlease enter the name of the exam venue:\t")
    exam_venue = input_validation(exam_venue, "exam venue")


    # Ask the user to input the number of students who will sit their exam at the venue.
    num_input = input("\nPlease enter the total number of students "
                      f"who will be registered to the {exam_venue.title()} venue:\t")
    # Validate the number entered prior to storing the result in a variable.
    no_of_students = numeric_input_checker(num_input, "number of students")


    # Create a .txt file to store the list of students, and add a title for readability.
    with open(f"{exam_venue}_reg_form.txt", 'w', encoding="utf-8") as register:
        register.write(f"Exam Register for {exam_venue.title()}\n")
        register.write(f"{divider}\n")


    # Declare a student_list, to store the student ID numbers for later use.
    student_list = []

    # For each student: request the ID number and store it in student_list.
    print(f"\nPlease enter the student ID numbers for the {exam_venue.title()} register: ")
    print("-"*65)
    for student in range(no_of_students):
        student_id = input(f"Student {student+1} -\t")
        student_list.append(student_id)

    # Ask the user if the student_list is correct, prior to writing the values to reg_form.txt
    check_students = input("\nAre these student ID numbers correct? Please enter 'y' or 'n':\t")
    check_students = check_students.lower()


    # If the student_list is confirmed to be correct, this loop is not entered.
    while check_students != 'y':

        # If there are incorrect values, allow the user to change them.
        if check_students == 'n':

            print("\nWhich student ID number do you wish to change?")
            # Ask the user which number (list index) they wish to change.
            to_be_changed = input("Enter the position in the list, (e.g. for Student 4, enter '4'):\t")
            # Check that the number the user enters is within the range of the student_list.
            to_be_changed = list_range_checker(student_list, to_be_changed)

            # Ask the user to enter the correct student ID number.
            correct_id = input(f"\nEnter the correct student ID number for Student {to_be_changed}:\t")
            # Replace the incorrect value in student_list.
            student_list[to_be_changed-1] = correct_id

            # Print the updated student_list values for the user to review, and ask if they are correct.
            print("\nYou have entered:")
            print("-"*20)
            for pos, student in enumerate(student_list, 1):
                print(f"Student {pos} -\t{student}")
            check_students = input("\nAre these student ID numbers correct? Please enter 'y' or 'n':\t")

        # Input validation - prompt the user to choose either 'y' or 'n' only in response to the question.
        else:
            check_students = input("\n**** Invalid Entry ****\tPlease enter 'y' or 'n':\t")

        check_students = check_students.lower()


    # When student_list is correct, write the student IDs to reg_form.txt and add a signature line for each.
    for student in student_list:
        with open(f"{exam_venue}_reg_form.txt", 'a', encoding="utf-8") as register:
            register.write(f"\n{student}\t")
            register.write(f"{signature_line}\n")

    print("\nProcessing complete. The register has been created.")
    print(f"Please check your folder for the file: \"{exam_venue}_reg_form.txt\"")


    # Ask the user if they wish to create another register or exit the program.
    done = continue_or_exit()

