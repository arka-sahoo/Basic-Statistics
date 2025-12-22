import statistics

def find_mean(data):
    return statistics.mean(data)

def find_median(data):
    return statistics.median(data)

def find_mode(data):
    try:
        return statistics.mode(data)
    except statistics.StatisticsError:
        return "No unique mode found"

def find_variance(data):
    return statistics.variance(data)

def find_standard_deviation(data):
    return statistics.stdev(data)

def main():
    print("Welcome to the basic Statistics Calculator program!")
    print("Please enter a list of numbers separated by commas: ")

    while True:
        try:
            user_input = input("Enter numbers: ")
            data = [float(item.strip()) for item in user_input.split(',')]
            if not data:
                print("No data entered. please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas: ")

    while True:
        print("\nChoose a statistic to calculate: ")
        print("1. Mean")
        print("2. Median")
        print("3. Mode")
        print("4. Variance")
        print("5. Standard Deviation")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            result = find_mean(data)
            print(f"The mean is: {result}")
        elif choice == '2':
            result = find_median(data)
            print(f"The median is: {result}")
        elif choice == '3':
            result = find_mode(data)
            print(f"The mode is: {result}")
        elif choice == '4':
            result = find_variance(data)
            print(f"The variance is: {result}")
        elif choice == '5':
            result = find_standard_deviation(data)
            print(f"The standard deviation is: {result}")
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 6.")

if __name__ == "__main__":
    main()