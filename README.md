# Modulo-Magic
The Divisibility Range Tool is a Python program that identifies numbers divisible by 3 or 5 within a given range, calculates their sum, and retrieves the last few elements from the list. It ensures valid input and provides a clear, efficient way to analyze numerical divisibility.
# Modulo Magic

**Modulo Magic** is a Python application that finds numbers within a specified range that are divisible by any of a list of user-defined divisors. It also calculates the sum of these numbers and provides additional insights such as the last three numbers divisible by the given divisors.

## Features

- **Find Divisible Numbers**: Identifies numbers in a given range that are divisible by any of the user-specified divisors.
- **Sum Calculation**: Computes the sum of all numbers that meet the divisibility criteria.
- **Last N Numbers**: Returns the last few numbers that are divisible by the specified divisors.
- **Interrupt Handling**: Gracefully handles program interruption (e.g., via `Ctrl+C`).

## Installation

Ensure you have Python installed on your system. This project requires Python 3.6 or higher.

No additional packages are required.

## Usage

### Input Range

You will be prompted to enter the start and end of the range. Enter valid integers to specify the range.

### Input Divisors

Enter the divisors one by one. Type `done` when you have finished entering all divisors.

### View Results

The program will display:

- The count of numbers divisible by the specified divisors.
- The list of these numbers.
- The last three numbers divisible by the divisors.
- The sum of these numbers.

### Exit the Program

You can exit the program anytime by pressing `Ctrl+C`.

## Example

```plaintext
Please enter the start of the range: 10
Please enter the end of the range: 50
Enter the divisors (enter 'done' to finish):
Enter a divisor: 3
Enter a divisor: 5
Enter a divisor: done

In the range [10, 50], there are 18 numbers divisible by 3, 5.

These numbers are:
15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50

The last three numbers divisible by 3, 5 are: 36, 39, 40
The sum of all numbers divisible by 3, 5 in this range is: 663
```
## Contributing
Contributions are welcome! If you have suggestions or improvements, please feel free to submit a pull request.

## Contact
For any questions or support, please contact mahnaznamani007@gmail.com .
