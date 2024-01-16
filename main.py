def horizontalSeparator():
    print("_" * 77)


def get_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input not in range(0, 121, 20):
                print("Out of range")
            else:
                return user_input
        except ValueError:
            print("Integer Required")


def horizontal_histogram(selections):
    print("Vertical Histogram")
    print()
    print("Progress   Trailing   Retriever   Exclude")

    for i in range(max(selections)):
        a = ['*' if i < star else ' ' for star in selections]
        print(f'{a[0]:>4}{a[1]:>11}{a[2]:>11}{a[3]:>11}')
    print()
    if sum(selections) == 1:
        print(sum(selections), "outcome in total")
    elif sum(selections) > 1:
        print(sum(selections), "outcomes in total")


def vertical_histogram(progress_count, trailer_count, retriever_count, exclude_count):
    print("Vertical Histogram")
    print()
    print("Progress " + f'{progress_count:<3}' + ": " + "*" * progress_count)
    print("Trailer " + f'{trailer_count:<4}' + ": " + "*" * trailer_count)
    print("Retriever " + f'{retriever_count:<2}' + ": " + "*" * retriever_count)
    print("Excluded " + f'{exclude_count:<3}' + ": " + "*" * exclude_count + "\n")
    print()
    if sum([progress_count, trailer_count, retriever_count, exclude_count]) == 1:
        print(sum([progress_count, trailer_count, retriever_count, exclude_count]), "outcome in total")
    elif sum([progress_count, trailer_count, retriever_count, exclude_count]) > 1:
        print(sum([progress_count, trailer_count, retriever_count, exclude_count]), "outcomes in total")


def main():
    progress_count = 0
    trailer_count = 0
    retriever_count = 0
    exclude_count = 0
    total_marks_count = 0
    lst = []

    print("\nENTER YOUR MARKS")
    while True:
        pass_mark = get_input("\nEnter your total PASS credits: ")
        defer_mark = get_input("Enter your total DEFER credits: ")
        fail_mark = get_input("Enter your total FAIL credits: ")

        full_mark = pass_mark + defer_mark + fail_mark

        if full_mark != 120:
            print("Total Incorrect\n")
            continue

        if (pass_mark == 120) and (full_mark == 120):
            print("Progress")
            progress_count += 1
            data = ("Progress-", pass_mark, ",", defer_mark, ",", fail_mark)
            lst.append(data)

        elif (pass_mark == 100) and (full_mark == 120):
            print("Progress (module trailer)")
            trailer_count += 1
            data = ("Progress- (module trailer)-", pass_mark, ",", defer_mark, ",", fail_mark)
            lst.append(data)

        elif (fail_mark >= 80) and (full_mark == 120):
            print("Exclude")
            exclude_count += 1
            data = ("Exclude-", pass_mark, ",", defer_mark, ",", fail_mark)
            lst.append(data)

        elif ((pass_mark in range(40, 81)) or (defer_mark in range(40, 121))) and (full_mark == 120):
            print("Do not progress-module retriever")
            retriever_count += 1
            data = ("Module retriever-", pass_mark, ",", defer_mark, ",", fail_mark)
            lst.append(data)

        total_marks_count += 1

        selection = input("\nWould you like to enter another set of data ? \nEnter 'y' for yes or 'q' to quit and "
                          "view results: ")
        if selection == "q":
            selections = [progress_count, trailer_count, retriever_count, exclude_count]

            horizontalSeparator()
            horizontal_histogram(selections)
            horizontalSeparator()
            vertical_histogram(progress_count, trailer_count, retriever_count, exclude_count)
            horizontalSeparator()

            print("List\n")
            for sub_list in lst:
                for lst_item in sub_list:
                    print(lst_item, end=" ")
                print()
            break


if __name__ == "__main__":
    main()
