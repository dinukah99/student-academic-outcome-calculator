progress_count = 0  # variable to count number of progress outcomes
trailer_count = 0  # variable to count number of progress (module trailer) outcomes
retriever_count = 0  # variable to count number of do not progress (module retriever) outcomes
exclude_count = 0  # variable to count number of excluded outcomes
total_marks_count = 0  # variable to count total number of counts
marks_range = range(0, 121, 20)  # range of marks for all 4 progression outcomes
full_mark = 0  # variable for the total of all 3 types of credits (Pass, Defer & Fail)
selection = ""  # variable declared to select whether to run the program again or view the results
selected = 0  # variable to run another set or value to be updated to 1 if chosen to quit and view the results.
lst = []


def horizontalSeparator():
    print("_" * 77)


def get_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input not in marks_range:
                print("Out of range")
            else:
                return user_input
        except ValueError:
            print("Integer Required")


def horizontal_histogram(all_options, selections):
    print("Vertical Histogram")
    print()
    print("Progress   Trailing   Retriever   Exclude")

    for i in range(all_options):
        a = ['*' if i < star else ' ' for star in selections]
        print(f'{a[0]:>4}{a[1]:>11}{a[2]:>11}{a[3]:>11}')
    print()
    if total_marks_count == 1:
        print(total_marks_count, "outcome in total")
    elif total_marks_count > 1:
        print(total_marks_count, "outcomes in total")


def vertical_histogram():
    print("Vertical Histogram")
    print()
    print("Progress " + f'{progress_count:<3}' + ": " + "*" * progress_count)
    print("Trailer " + f'{trailer_count:<4}' + ": " + "*" * trailer_count)
    print("Retriever " + f'{retriever_count:<2}' + ": " + "*" * retriever_count)
    print("Excluded " + f'{exclude_count:<3}' + ": " + "*" * exclude_count + "\n")
    print()
    if total_marks_count == 1:
        print(total_marks_count, "outcome in total")
    elif total_marks_count > 1:
        print(total_marks_count, "outcomes in total")


def main():
    global progress_count, trailer_count, retriever_count, exclude_count, total_marks_count, full_mark, selected, lst, \
        selection

    isValid = False

    print("\nENTER YOUR MARKS")
    while True:  # main loop of the entire program
        while not isValid:  # variable to run the main program
            pass_mark = get_input("\nEnter your total PASS credits: ")
            defer_mark = get_input("Enter your total DEFER credits: ")
            fail_mark = get_input("Enter your total FAIL credits: ")

            full_mark = pass_mark + defer_mark + fail_mark

            if full_mark != 120:
                print("Total Incorrect\n")
                continue

            # if and else if statements to output the 4 progression outcomes
            if (pass_mark == 120) & (full_mark == 120):
                print("Progress")
                progress_count = progress_count + 1
                data = ("Progress-", pass_mark, ",", defer_mark, ",", fail_mark)
                lst.append(data)

            elif (pass_mark == 100) & (full_mark == 120):
                print("Progress (module trailer)")
                trailer_count = trailer_count + 1
                data = ("Progress- (module trailer)-", pass_mark, ",", defer_mark, ",", fail_mark)
                lst.append(data)

            elif (fail_mark >= 80) & (full_mark == 120):
                print("Exclude")
                exclude_count = exclude_count + 1
                data = ("Exclude-", pass_mark, ",", defer_mark, ",", fail_mark)
                lst.append(data)

            elif ((pass_mark in range(40, 81)) or (defer_mark in range(40, 121))) & (full_mark == 120):
                print("Do not progress-module retriever")
                retriever_count = retriever_count + 1
                data = ("Module retriever-", pass_mark, ",", defer_mark, ",", fail_mark)
                lst.append(data)

            # incrementing the total marks count to output the total number of outcomes
            total_marks_count = total_marks_count + 1

            isValid = True  # value updated to run the selection loop
            while isValid:
                selection = str(input("\nWould you like to enter another set of data ? \nEnter 'y' for yes or 'q' to "
                                      "quit and view results: "))
                if selection == "y":  # looping back to the main program
                    isValid = False

                elif selection == "q":  # breaking away from the loop to print the histograms and to print the stored
                    # data retrieved from the list
                    selections = [progress_count, trailer_count, retriever_count, exclude_count]
                    all_options = max(selections)

                    horizontalSeparator()
                    horizontal_histogram(all_options, selections)
                    horizontalSeparator()
                    vertical_histogram()
                    horizontalSeparator()

                    print("List\n")
                    for sub_list in lst:
                        for lst in sub_list:
                            print(lst, end=" ")
                        print()
                    break

                else:  # looping back to the selection loop if the user-input is incorrect
                    print("\ninvalid Input-Please enter valid input 'y' or 'q'\n")
                    isValid = True


if __name__ == "__main__":
    main()
