import signal
import sys

def signal_handler(sig, frame):
    print("\nProgram interrupted by user. Exiting...")
    sys.exit(0)

def is_divisible_by_numbers(number, divisors):
    """
    Checks if a number is divisible by any of the given divisors.

    Args:
        number (int): The number to check.
        divisors (list): List of divisors to check against.

    Returns:
        bool: True if the number is divisible by any of the divisors, False otherwise.
    """
    return any(number % divisor == 0 for divisor in divisors)


def find_divisible_numbers_and_sum(start, end, divisors):
    """
    Finds all numbers in the range [start, end] that are divisible by any of the given divisors
    and calculates their sum.

    Args:
        start (int): Start of the range.
        end (int): End of the range.
        divisors (list): List of divisors to check against.

    Returns:
        tuple: (divisible_numbers (list), total_sum (int))
    """
    divisible_numbers = []
    total_sum = 0

    for num in range(start, end + 1):
        if is_divisible_by_numbers(num, divisors):
            divisible_numbers.append(num)
            total_sum += num

    return divisible_numbers, total_sum


def get_last_n_elements(numbers, n):
    """
    Returns the last n elements of a list.

    Args:
        numbers (list): List of numbers.
        n (int): Number of elements to return.

    Returns:
        list: Last n elements of the list.
    """
    return numbers[-n:]


def get_valid_input(prompt):
    """
    Continuously prompts the user for input until a valid integer is entered.

    Args:
        prompt (str): The prompt message for input.

    Returns:
        int: The validated integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_input_range():
    """
    Prompts the user for the start and end of a range and validates the input.

    Returns:
        tuple: A tuple containing the start and end of the range (start, end).
    """
    while True:
        start = get_valid_input("Please enter the start of the range: ")
        end = get_valid_input("Please enter the end of the range: ")
        if start > end:
            print("The start of the range must be less than or equal to the end. Please try again.")
        else:
            return start, end


def get_divisors():
    """
    Prompts the user for a list of divisors and validates the input.

    Returns:
        list: List of divisors.
    """
    divisors = []
    print("Enter the divisors (enter 'done' to finish):")
    while True:
        user_input = input("Enter a divisor: ")
        if user_input.lower() == 'done':
            if not divisors:
                print("You must enter at least one divisor.")
            else:
                return divisors
        else:
            try:
                divisor = int(user_input)
                if divisor <= 0:
                    print("Divisor must be a positive integer. Try again.")
                elif divisor in divisors:
                    print("This divisor has already been entered. Try again.")
                else:
                    divisors.append(divisor)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")


def display_results(start, end, divisors, divisible_numbers, last_n_numbers, total_sum):
    """
    Displays the results of the calculation.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.
        divisors (list): List of divisors.
        divisible_numbers (list): List of numbers divisible by the divisors.
        last_n_numbers (list): The last n numbers divisible by the divisors.
        total_sum (int): The sum of numbers divisible by the divisors.
    """
    count = len(divisible_numbers)
    print(f"\nIn the range [{start}, {end}], there are {count} numbers divisible by {', '.join(map(str, divisors))}.")

    if divisible_numbers:
        print("These numbers are:")
        print(", ".join(map(str, divisible_numbers)))
        print(f"\nThe last three numbers divisible by {', '.join(map(str, divisors))} are: {', '.join(map(str, last_n_numbers))}")
        print(f"The sum of all numbers divisible by {', '.join(map(str, divisors))} in this range is: {total_sum}")


def main():
    """Main function to execute the program."""
    # Register the signal handler
    signal.signal(signal.SIGINT, signal_handler)

    # Get the input range from the user
    start, end = get_input_range()

    # Get the divisors from the user
    divisors = get_divisors()

    # Find all numbers divisible by the given divisors in the range and calculate the sum
    divisible_numbers, total_sum = find_divisible_numbers_and_sum(start, end, divisors)

    # Get the last three numbers from the list
    last_n_numbers = get_last_n_elements(divisible_numbers, 3)

    # Display the results
    display_results(start, end, divisors, divisible_numbers, last_n_numbers, total_sum)


# Run the program
if __name__ == "__main__":
    main()
