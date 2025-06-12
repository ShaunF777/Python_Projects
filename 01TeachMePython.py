"""
Python Conditionals Interactive Tutorial
========================================

This program interactively teaches Python conditionals based on the Harvard CS50 Python course.
It covers: if statements, elif/else, logical operators (and/or), comparison operators,
modulo operator, match statements, and Pythonic coding practices.

Dependencies: Python 3.6+ (no external libraries required)

Topics covered:
- Basic if statements and comparison operators
- Control flow with elif and else
- Logical operators: and, or
- Modulo operator for parity checking
- Creating custom functions with boolean returns
- Pythonic coding style
- Match statements (Python 3.10+)

Characters used: Peter Rabbit stories and The Famous Five
"""

import sys
import random

def clear_screen():
    """Clear the screen for better presentation"""
    print("\n" * 3)

def wait_for_enter():
    """Wait for user to press Enter to continue"""
    input("\nPress Enter to continue...")

def section_header(title):
    """Print a formatted section header"""
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)

def demonstrate_basic_conditionals():
    """Demonstrate basic if statements and comparison operators"""
    section_header("BASIC IF STATEMENTS & COMPARISON OPERATORS")
    
    print("""
In Python, we use conditionals to make decisions in our programs.
Let's start with the basic comparison operators:

>   greater than          <   less than
>=  greater than or equal <=  less than or equal
==  equals (comparison)   !=  not equal
=   assignment (single =)

Let's help Peter Rabbit decide which garden path to take!
""")
    
    wait_for_enter()
    
    print("\n--- Example 1: Basic Comparison ---")
    print("Code:")
    print("""
peter_carrots = int(input("How many carrots does Peter have? "))
required_carrots = 5

if peter_carrots >= required_carrots:
    print("Peter has enough carrots to share with his sisters!")
""")
    
    # Interactive demonstration
    print("\nLet's try it:")
    try:
        peter_carrots = int(input("How many carrots does Peter have? "))
        required_carrots = 5
        
        if peter_carrots >= required_carrots:
            print("Peter has enough carrots to share with his sisters!")
        else:
            print("Peter needs more carrots!")
    except ValueError:
        print("Please enter a valid number!")
    
    wait_for_enter()

def demonstrate_elif_else():
    """Demonstrate elif and else statements"""
    section_header("ELIF AND ELSE STATEMENTS")
    
    print("""
Instead of multiple separate if statements, we use elif (else if) and else
for more efficient control flow.

Let's help Julian from The Famous Five decide what to do based on the weather!
""")
    
    wait_for_enter()
    
    print("\n--- Inefficient Way (Multiple if statements) ---")
    print("""
weather = input("What's the weather like? ")

if weather == "sunny":
    print("Julian suggests going to the beach!")
    
if weather == "rainy":
    print("Julian suggests staying inside and reading!")
    
if weather == "cloudy":
    print("Julian suggests exploring the old castle!")
""")
    
    print("\n--- Efficient Way (if/elif/else) ---")
    print("""
weather = input("What's the weather like? ").lower()

if weather == "sunny":
    print("Julian suggests going to the beach!")
elif weather == "rainy":
    print("Julian suggests staying inside and reading!")
elif weather == "cloudy":
    print("Julian suggests exploring the old castle!")
else:
    print("Julian says: 'Whatever the weather, adventure awaits!'")
""")
    
    # Interactive demonstration
    print("\nLet's try the efficient version:")
    weather = input("What's the weather like? ").lower()
    
    if weather == "sunny":
        print("Julian suggests going to the beach!")
    elif weather == "rainy":
        print("Julian suggests staying inside and reading!")
    elif weather == "cloudy":
        print("Julian suggests exploring the old castle!")
    else:
        print("Julian says: 'Whatever the weather, adventure awaits!'")
    
    wait_for_enter()

def demonstrate_logical_operators():
    """Demonstrate and/or operators"""
    section_header("LOGICAL OPERATORS: AND & OR")
    
    print("""
Logical operators allow us to combine multiple conditions:

AND - Both conditions must be True
OR  - At least one condition must be True

Let's help Anne from The Famous Five pack for their adventure!
""")
    
    wait_for_enter()
    
    print("\n--- Using AND ---")
    print("Anne needs BOTH a map AND a compass for the treasure hunt:")
    print("""
has_map = input("Does Anne have a map? (yes/no): ").lower() == "yes"
has_compass = input("Does Anne have a compass? (yes/no): ").lower() == "yes"

if has_map and has_compass:
    print("Anne is ready for the treasure hunt!")
else:
    print("Anne needs to find the missing item first!")
""")
    
    # Interactive demonstration
    has_map = input("Does Anne have a map? (yes/no): ").lower() == "yes"
    has_compass = input("Does Anne have a compass? (yes/no): ").lower() == "yes"
    
    if has_map and has_compass:
        print("Anne is ready for the treasure hunt!")
    else:
        print("Anne needs to find the missing item first!")
    
    wait_for_enter()
    
    print("\n--- Using OR ---")
    print("George can bring EITHER Timmy the dog OR her boat (or both):")
    print("""
has_timmy = input("Is Timmy with George? (yes/no): ").lower() == "yes"
has_boat = input("Does George have her boat? (yes/no): ").lower() == "yes"

if has_timmy or has_boat:
    print("George is ready for adventure!")
else:
    print("George needs either Timmy or her boat!")
""")
    
    # Interactive demonstration
    has_timmy = input("Is Timmy with George? (yes/no): ").lower() == "yes"
    has_boat = input("Does George have her boat? (yes/no): ").lower() == "yes"
    
    if has_timmy or has_boat:
        print("George is ready for adventure!")
    else:
        print("George needs either Timmy or her boat!")
    
    wait_for_enter()

def demonstrate_chained_comparison():
    """Demonstrate Python's chained comparisons"""
    section_header("PYTHON'S CHAINED COMPARISONS")
    
    print("""
Python allows you to chain comparisons in a natural way!
This is more readable than using multiple 'and' operators.

Let's help Dick from The Famous Five grade their school test:
""")
    
    wait_for_enter()
    
    print("--- Traditional way (using 'and') ---")
    print("""
score = int(input("What's Dick's test score? "))

if score >= 90 and score <= 100:
    print("Grade: A - Excellent work, Dick!")
elif score >= 80 and score < 90:
    print("Grade: B - Well done, Dick!")
elif score >= 70 and score < 80:
    print("Grade: C - Good effort, Dick!")
elif score >= 60 and score < 70:
    print("Grade: D - Keep trying, Dick!")
else:
    print("Grade: F - Don't give up, Dick!")
""")
    
    print("\n--- Pythonic way (chained comparisons) ---")
    print("""
score = int(input("What's Dick's test score? "))

if 90 <= score <= 100:
    print("Grade: A - Excellent work, Dick!")
elif 80 <= score < 90:
    print("Grade: B - Well done, Dick!")
elif 70 <= score < 80:
    print("Grade: C - Good effort, Dick!")
elif 60 <= score < 70:
    print("Grade: D - Keep trying, Dick!")
else:
    print("Grade: F - Don't give up, Dick!")
""")
    
    # Interactive demonstration
    print("\nLet's try it:")
    try:
        score = int(input("What's Dick's test score? "))
        
        if 90 <= score <= 100:
            print("Grade: A - Excellent work, Dick!")
        elif 80 <= score < 90:
            print("Grade: B - Well done, Dick!")
        elif 70 <= score < 80:
            print("Grade: C - Good effort, Dick!")
        elif 60 <= score < 70:
            print("Grade: D - Keep trying, Dick!")
        else:
            print("Grade: F - Don't give up, Dick!")
    except ValueError:
        print("Please enter a valid number!")
    
    wait_for_enter()

def demonstrate_modulo():
    """Demonstrate the modulo operator"""
    section_header("THE MODULO OPERATOR (%)")
    
    print("""
The modulo operator (%) gives you the remainder after division.
It's very useful for checking if numbers are even or odd!

Examples:
4 % 2 = 0  (4 divided by 2 = 2 remainder 0)
5 % 2 = 1  (5 divided by 2 = 2 remainder 1)
6 % 3 = 0  (6 divided by 3 = 2 remainder 0)
7 % 3 = 1  (7 divided by 3 = 2 remainder 1)

Let's help Mr. McGregor count his vegetables:
""")
    
    wait_for_enter()
    
    print("""
vegetables = int(input("How many vegetables did Mr. McGregor harvest? "))

if vegetables % 2 == 0:
    print("Mr. McGregor has an even number of vegetables!")
    print("He can divide them equally between two baskets.")
else:
    print("Mr. McGregor has an odd number of vegetables!")
    print("One basket will have one more vegetable than the other.")
""")
    
    # Interactive demonstration
    try:
        vegetables = int(input("How many vegetables did Mr. McGregor harvest? "))
        
        if vegetables % 2 == 0:
            print("Mr. McGregor has an even number of vegetables!")
            print("He can divide them equally between two baskets.")
        else:
            print("Mr. McGregor has an odd number of vegetables!")
            print("One basket will have one more vegetable than the other.")
    except ValueError:
        print("Please enter a valid number!")
    
    wait_for_enter()

def demonstrate_functions_with_booleans():
    """Demonstrate creating functions that return boolean values"""
    section_header("FUNCTIONS RETURNING BOOLEAN VALUES")
    
    print("""
We can create our own functions that return True or False.
This makes our code more readable and reusable!

Let's create a function to help Peter Rabbit check if it's safe to enter the garden:
""")
    
    wait_for_enter()
    
    print("--- Function Definition ---")
    print("""
def is_garden_safe(mr_mcgregor_home, cat_nearby):
    '''Check if Peter can safely enter the garden'''
    if not mr_mcgregor_home and not cat_nearby:
        return True
    else:
        return False

def main():
    print("Let's check if Peter can safely enter Mr. McGregor's garden...")
    
    mcgregor_home = input("Is Mr. McGregor home? (yes/no): ").lower() == "yes"
    cat_present = input("Is there a cat nearby? (yes/no): ").lower() == "yes"
    
    if is_garden_safe(mcgregor_home, cat_present):
        print("It's safe! Peter can sneak into the garden!")
    else:
        print("Too dangerous! Peter should wait.")
""")
    
    # Interactive demonstration
    print("\nLet's try it:")
    
    def is_garden_safe(mr_mcgregor_home, cat_nearby):
        if not mr_mcgregor_home and not cat_nearby:
            return True
        else:
            return False
    
    mcgregor_home = input("Is Mr. McGregor home? (yes/no): ").lower() == "yes"
    cat_present = input("Is there a cat nearby? (yes/no): ").lower() == "yes"
    
    if is_garden_safe(mcgregor_home, cat_present):
        print("It's safe! Peter can sneak into the garden!")
    else:
        print("Too dangerous! Peter should wait.")
    
    wait_for_enter()

def demonstrate_pythonic_style():
    """Demonstrate Pythonic coding style"""
    section_header("PYTHONIC CODING STYLE")
    
    print("""
Python allows for very readable, English-like code.
Let's see how we can make our boolean functions more "Pythonic":
""")
    
    wait_for_enter()
    
    print("--- Less Pythonic ---")
    print("""
def is_adventure_day(weather_good, friends_available):
    if weather_good == True and friends_available == True:
        return True
    else:
        return False
""")
    
    print("\n--- More Pythonic ---")
    print("""
def is_adventure_day(weather_good, friends_available):
    return weather_good and friends_available
""")
    
    print("\n--- Even More Pythonic (ternary operator) ---")
    print("""
def get_adventure_message(is_adventure_day):
    return "Let's go exploring!" if is_adventure_day else "Maybe tomorrow!"
""")
    
    # Interactive demonstration
    print("\nLet's see the Pythonic version in action:")
    
    def is_adventure_day(weather_good, friends_available):
        return weather_good and friends_available
    
    def get_adventure_message(adventure_day):
        return "The Famous Five are ready to go exploring!" if adventure_day else "Maybe tomorrow will be better!"
    
    good_weather = input("Is the weather good? (yes/no): ").lower() == "yes"
    friends_ready = input("Are all the Famous Five available? (yes/no): ").lower() == "yes"
    
    adventure_possible = is_adventure_day(good_weather, friends_ready)
    message = get_adventure_message(adventure_possible)
    
    print(f"\nResult: {message}")
    
    wait_for_enter()

def demonstrate_match_statements():
    """Demonstrate match statements (Python 3.10+)"""
    section_header("MATCH STATEMENTS")
    
    print("""
Match statements (available in Python 3.10+) provide a clean way to
handle multiple specific values. They're like switch statements in other languages.

Let's help assign Famous Five members to their favorite activities:
""")
    
    wait_for_enter()
    
    # Check Python version
    if sys.version_info < (3, 10):
        print("NOTE: Match statements require Python 3.10+")
        print("Your Python version doesn't support match statements yet.")
        print("Here's how they would work:")
    
    print("\n--- Using if/elif (traditional way) ---")
    print("""
member = input("Which Famous Five member? ").title()

if member == "Julian":
    print("Julian loves leading expeditions!")
elif member == "Dick":
    print("Dick enjoys solving puzzles and mysteries!")
elif member == "Anne":
    print("Anne likes taking care of everyone!")
elif member == "George":
    print("George prefers adventures with Timmy!")
else:
    print("Who's that? Are they part of the Famous Five?")
""")
    
    wait_for_enter()
    print("\n--- Using match statements (Python 3.10+) ---")
    print("""
member = input("Which Famous Five member? ").title()

match member:
    case "Julian":
        print("Julian loves leading expeditions!")
    case "Dick":
        print("Dick enjoys solving puzzles and mysteries!")
    case "Anne":
        print("Anne likes taking care of everyone!")
    case "George":
        print("George prefers adventures with Timmy!")
    case _:  # Default case (like 'else')
        print("Who's that? Are they part of the Famous Five?")
""")
    
    wait_for_enter()
    print("\n--- Multiple values in one case ---")
    print("""
member = input("Which Famous Five member? ").title()

match member:
    case "Julian" | "Dick":  # Either Julian OR Dick
        print("One of the boys from the Famous Five!")
    case "Anne" | "George":  # Either Anne OR George
        print("One of the girls from the Famous Five!")
    case _:
        print("Not a Famous Five member!")
""")
    
    wait_for_enter()
    # Interactive demonstration
    print("\nLet's try the traditional if/elif version:")
    member = input("Which Famous Five member? ").title()
    
    if member == "Julian":
        print("Julian loves leading expeditions!")
    elif member == "Dick":
        print("Dick enjoys solving puzzles and mysteries!")
    elif member == "Anne":
        print("Anne likes taking care of everyone!")
    elif member == "George":
        print("George prefers adventures with Timmy!")
    else:
        print("Who's that? Are they part of the Famous Five?")
    
    wait_for_enter()
    # Interactive demonstration
    print("\nLet's try the \"Multiple values in one case\" version:")
    amember = input("Which Famous Five member? ").title()
    
    match amember:
        case "Julian" | "Dick":  # Either Julian OR Dick
            print("One of the boys from the Famous Five!")
        case "Anne" | "George":  # Either Anne OR George
            print("One of the girls from the Famous Five!")
        case _:
            print("Not a Famous Five member!")
    
    wait_for_enter()

def quiz_section():
    """Interactive quiz to test understanding"""
    section_header("QUIZ TIME!")
    
    print("""
Let's test your understanding of Python conditionals!
Answer the following questions:
""")
    
    score = 0
    total_questions = 4
    
    # Question 1
    print("\n--- Question 1 ---")
    print("What operator checks if two values are equal?")
    print("a) =")
    print("b) ==")
    print("c) !=")
    
    answer = input("Your answer (a/b/c): ").lower()
    if answer == "b":
        print("✓ Correct! == is used for comparison")
        score += 1
    else:
        print("✗ Incorrect. == is used for comparison, = is for assignment")
    
    wait_for_enter()
    
    # Question 2
    print("\n--- Question 2 ---")
    print("What will this code print if x = 7?")
    print("if x % 2 == 0:")
    print("    print('Even')")
    print("else:")
    print("    print('Odd')")
    
    answer = input("Your answer (Even/Odd): ").title()
    if answer == "Odd":
        print("✓ Correct! 7 % 2 = 1, which is not equal to 0")
        score += 1
    else:
        print("✗ Incorrect. 7 % 2 = 1, so the condition is False, printing 'Odd'")
    
    wait_for_enter()
    
    # Question 3
    print("\n--- Question 3 ---")
    print("Which is more efficient?")
    print("a) Multiple separate if statements")
    print("b) if/elif/else chain")
    
    answer = input("Your answer (a/b): ").lower()
    if answer == "b":
        print("✓ Correct! elif chains stop checking once a condition is met")
        score += 1
    else:
        print("✗ Incorrect. elif chains are more efficient as they stop checking once a condition is met")
    
    wait_for_enter()
    
    # Question 4
    print("\n--- Question 4 ---")
    print("What does this Pythonic expression return?")
    print("return x > 0 and x < 100")
    print("(when x = 50)")
    
    answer = input("Your answer (True/False): ").title()
    if answer == "True":
        print("✓ Correct! 50 is greater than 0 AND less than 100")
        score += 1
    else:
        print("✗ Incorrect. 50 > 0 is True AND 50 < 100 is True, so the result is True")
    
    wait_for_enter()
    
    # Final score
    print(f"\n--- QUIZ RESULTS ---")
    print(f"You scored {score}/{total_questions} ({score/total_questions*100:.0f}%)")
    
    if score == total_questions:
        print("🎉 Perfect! You've mastered Python conditionals!")
    elif score >= total_questions * 0.75:
        print("👍 Great job! You understand conditionals well!")
    elif score >= total_questions * 0.5:
        print("👌 Good work! Review the concepts and try again!")
    else:
        print("📚 Keep practicing! Review the examples above.")

def practice_exercises():
    """Provide practice exercises for students"""
    section_header("PRACTICE EXERCISES")
    
    print("""
Here are some exercises to practice what you've learned.
Try to solve them on your own!

EXERCISE 1: Peter's Carrot Counter
Write a program that:
- Asks how many carrots Peter found
- If he found more than 10, print "Plenty for the family!"
- If he found 5-10, print "Just enough for dinner"
- If he found less than 5, print "Better keep looking!"

EXERCISE 2: Famous Five Adventure Planner
Write a program that:
- Asks for the day of the week
- Uses match statements (or if/elif) to suggest activities:
  - Monday/Tuesday: "School day - plan for weekend adventure!"
  - Wednesday/Thursday: "Midweek - perfect for exploring nearby!"
  - Friday: "Weekend starts tomorrow - prepare your gear!"
  - Saturday/Sunday: "Adventure time!"

EXERCISE 3: Mr. McGregor's Garden Security
Write a function that takes three parameters:
- is_daytime (boolean)
- peter_nearby (boolean)  
- gate_locked (boolean)
Return True if the garden is secure, False otherwise.
Garden is secure if: it's nighttime OR the gate is locked OR Peter is not nearby.

EXERCISE 4: Create Your Own
Think of a scenario from Peter Rabbit or Famous Five stories and
create a program using conditionals to solve a problem!
""")
    
    wait_for_enter()

def main():
    """Main program function"""
    clear_screen()
    
    print("🐰 WELCOME TO PYTHON CONDITIONALS TUTORIAL 🐰")
    print("Featuring characters from Peter Rabbit and The Famous Five")
    
    while True:
        print("\n" + "=" * 60)
        print("MENU - Choose a topic to learn:")
        print("=" * 60)
        print("1. Basic If Statements & Comparison Operators")
        print("2. Elif and Else Statements")
        print("3. Logical Operators (and/or)")
        print("4. Python's Chained Comparisons")
        print("5. Modulo Operator (%)")
        print("6. Functions with Boolean Returns")
        print("7. Pythonic Coding Style")
        print("8. Match Statements")
        print("9. Quiz Time!")
        print("10. Practice Exercises")
        print("11. Exit")
        
        choice = input("\nEnter your choice (1-11): ").strip()
        
        if choice == "1":
            demonstrate_basic_conditionals()
        elif choice == "2":
            demonstrate_elif_else()
        elif choice == "3":
            demonstrate_logical_operators()
        elif choice == "4":
            demonstrate_chained_comparison()
        elif choice == "5":
            demonstrate_modulo()
        elif choice == "6":
            demonstrate_functions_with_booleans()
        elif choice == "7":
            demonstrate_pythonic_style()
        elif choice == "8":
            demonstrate_match_statements()
        elif choice == "9":
            quiz_section()
        elif choice == "10":
            practice_exercises()
        elif choice == "11":
            print("\n🎓 Thanks for learning Python conditionals!")
            print("Keep practicing and happy coding!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-11.")
        
        clear_screen()

if __name__ == "__main__":
    main()