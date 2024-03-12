def sort_numbers():
    numbers = []
    while True:
        number = input("Please enter a number")
        if number == "":
            break
        numbers.append(int(number))
    
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)

sort_numbers()