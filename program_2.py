#Week 7, Program 2 - Larger than n
#Caiden Heinrichs
#03/06/26


def display_larger_than_n_list(n, n_list):
    #Sets up a list to collect numbers > n
    greaterThanN = []
    #Updates list for each number > n
    for number in n_list:
        if number > n:
            greaterThanN.append(number)
    #Displays all numbers > n
    print(greaterThanN)


def main():
    # Declare local variables
    number = 5
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Display the number.
    print('Number:', number)

    # Display the list of numbers.
    print('List of numbers:')
    print(f'{number_list}')

    # Display the list of numbers that are larger
    # than the number.
    print(f'List of numbers that are larger than {number}:')

    # Call the display_larger_than_n_list function,
    # passing a number and number list as arguments.
    display_larger_than_n_list(number, number_list)


if __name__ == '__main__':
    main()
