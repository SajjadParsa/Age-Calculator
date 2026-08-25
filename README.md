# Age Calculator 🎂

A simple **Python Age Calculator** that calculates a person's age based on their birth year and the current year.

The program also provides additional information such as the approximate number of months, days, hours, and minutes the user has lived.

## Features

* Calculate the user's age
* Calculate approximate:

  * Months lived
  * Days lived
  * Hours lived
  * Minutes lived
* Identify the user's age category
* Calculate the number of years remaining until the user's 100th birthday
* Validate the user's name
* Validate year input
* Prevent a birth year greater than the current year
* Allow the user to calculate another age
* Interactive command-line interface

## Age Categories

The program identifies the user's age using the following categories:

| Age                       | Category    |
| ------------------------- | ----------- |
| 1–17                      | Under 18    |
| 18–30                     | Young Adult |
| 31–60                     | Adult       |
| 61–120                    | Senior      |
| 0 or below / 121 or above | Invalid Age |

## How It Works

The main calculation is handled by the `user_age()` function:

```python
def user_age(user_name, user_bt, user_cYear):
    age = user_cYear - user_bt
```

The program then uses the calculated age to determine other values.

### Months

```text
Months = Age × 12
```

### Days

```text
Days = Age × 365
```

### Hours

```text
Hours = Days × 24
```

### Minutes

```text
Minutes = Hours × 60
```

### Years Until 100

```text
Years Left = 100 − Age
```

## Input Validation

The program includes basic input validation.

### Name Validation

The user's name must contain only alphabetic characters:

```python
if user_name.isalpha():
    break
```

If the input contains numbers or other invalid characters, the program asks for the name again.

### Year Validation

The program uses `try/except` to make sure the user enters a valid integer for the years.

```python
try:
    user_bt = int(input("Enter Your Birthday year: "))
    user_cYear = int(input("Enter current year: "))
except ValueError:
    print("Enter valid Year!")
```

The program also checks that the birth year is not greater than the current year.

## Example

```text
Enter Your name: Sajad
Enter Your Birthday year: 2006
Enter current year: 2026

You are a young adult!

You have 80 years left until your 100th birthday.

Hello Sajad Now you are 20.
You have lived:
240 months
7300 days
175200 hours
10512000 minutes!

Do you want to calculate again? (Yes/No)
```

## Technologies

This project was created using:

* **Python 3**
* Functions
* Variables
* `while` loops
* `if / elif / else`
* Lists are not required
* String methods
* `try / except`
* User input
* Basic arithmetic operations
* Input validation

## Project Structure

```text
Age-Calculator/
│
├── age_calculator.py
└── README.md
```

## How to Run

Make sure **Python 3** is installed on your computer.

Run the program from the terminal:

```bash
python age_calculator.py
```

Then follow the instructions displayed in the terminal.

## Important Note

The calculations for months, days, hours, and minutes are **approximate** because the program assumes:

* 12 months per year
* 365 days per year
* 24 hours per day
* 60 minutes per hour

Leap years and the exact birth date are not considered.

## Future Improvements

Possible improvements for this project:

* Ask for the complete date of birth instead of only the birth year
* Calculate the exact age in years, months, and days
* Consider leap years
* Calculate remaining days until the 100th birthday
* Support names containing spaces
* Add a graphical user interface (GUI)
* Save calculation history to a file
* Add more age categories
* Use Python's `datetime` module for more accurate calculations

## Author

Created as a **Python practice project** to improve understanding of:

* Functions
* Loops
* Conditional statements
* Input validation
* Exception handling
* String methods
* Arithmetic operations
* Basic program structure
