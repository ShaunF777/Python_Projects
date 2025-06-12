#!/usr/bin/env python3
"""
Interactive Python Learning Program
Based on CS50's Introduction to Programming with Python - Lecture 0 Functions & Variables
Teaches Python concepts with comparisons to C programming language, including concepts like:
Hello World programs and functions,
Debugging and error handling, 
Variables and user input,
Strings and formatting,
Integers and mathematical operations,
Floating point numbers,
Creating custom functions,
Code organization with main()
"""

import random
import time
import sys

def clear_screen():
    """Clear the terminal screen for better readability"""
    print("\n" * 2)

def pause_for_effect():
    """Add a small pause for dramatic effect"""
    time.sleep(1.5)

def get_input_with_validation(prompt, valid_responses=None):
    """Get user input with optional validation"""
    while True:
        response = input(prompt).strip().lower()
        if valid_responses is None or response in valid_responses:
            return response
        print(f"Please enter one of: {', '.join(valid_responses)}")

def welcome_user():
    """Personalized welcome and introduction"""
    print("=" * 60)
    print("🐍 WELCOME TO INTERACTIVE PYTHON LEARNING! 🐍")
    print("=" * 60)
    print("\nHello! I'm your personal Python tutor.")
    
    name = input("What's your name? ").strip().title()
    print(f"\nNice to meet you, {name}! 🎉")
    
    print(f"\n{name}, I'm excited to help you learn Python!")
    print("This program will teach you Python fundamentals with comparisons to C.")
    
    experience = get_input_with_validation(
        "\nHave you programmed in C before? (yes/no): ", 
        ["yes", "no", "y", "n"]
    )
    
    has_c_experience = experience.startswith('y')
    
    print(f"\n{'Great!' if has_c_experience else 'No worries!'} Let's start our Python journey together!")
    pause_for_effect()
    
    return name, has_c_experience

def lesson_hello_world(name, has_c_experience):
    """Lesson 1: Hello World and Basic Functions"""
    clear_screen()
    print("=" * 60)
    print("📝 LESSON 1: HELLO WORLD & FUNCTIONS")
    print("=" * 60)
    
    print(f"\n{name}, let's start with the most famous program in programming!")
    
    if has_c_experience:
        print("\n🔄 COMPARISON TO C:")
        print("In C, you might write:")
        print('    #include <stdio.h>')
        print('    int main() {')
        print('        printf("hello, world\\n");')
        print('        return 0;')
        print('    }')
        print("\nIn Python, it's much simpler:")
    else:
        print("\nIn Python, printing text is incredibly simple:")
    
    print('    print("hello, world")')
    
    print(f"\n🤔 {name}, what do you notice about Python vs C?" if has_c_experience else f"\n🤔 {name}, what do you think this code does?")
    input("Press Enter to continue...")
    
    print("\n✨ Key Points:")
    print("• Python's print() is a built-in FUNCTION")
    print("• Functions are like verbs - they perform actions")
    print("• print() takes ARGUMENTS (the text to display)")
    print("• No need for #include, main(), or return statements!")
    
    # Interactive question
    response = get_input_with_validation(
        f"\n❓ {name}, what do we call the text inside the parentheses? (hint: starts with 'a'): ",
        ["argument", "arguments", "arg", "args"]
    )
    
    print("🎯 Correct! The text inside parentheses are called ARGUMENTS!")
    pause_for_effect()

def lesson_bugs_and_errors(name):
    """Lesson 2: Understanding Bugs and Error Messages"""
    clear_screen()
    print("=" * 60)
    print("🐛 LESSON 2: BUGS & ERROR MESSAGES")
    print("=" * 60)
    
    print(f"\n{name}, bugs are a natural part of programming!")
    print("Don't get discouraged - even experienced programmers make mistakes!")
    
    print("\n🚫 Common Bug Example:")
    print('    print("hello, world"  # Missing closing parenthesis!')
    
    print("\n📋 When you run this, Python gives you an error message:")
    print("    SyntaxError: unexpected EOF while parsing")
    
    print(f"\n💡 {name}, error messages are your friends! They help you find and fix problems.")
    
    # Interactive debugging
    print("\n🔍 DEBUGGING CHALLENGE:")
    print("Which of these lines has a bug?")
    print("A) print('Hello, world!')")
    print('B) print("Hello, world"')
    print('C) print("Hello, world!")')
    
    answer = get_input_with_validation(
        "Your answer (A, B, or C): ", 
        ["a", "b", "c"]
    )
    
    if answer == "b":
        print("🎯 Excellent! Line B is missing the closing parenthesis!")
    else:
        print("🤔 Not quite. Line B is missing the closing parenthesis: )")
    
    print("\n✨ Remember: Python is very picky about syntax!")
    pause_for_effect()

def lesson_variables_and_input(name, has_c_experience):
    """Lesson 3: Variables and User Input"""
    clear_screen()
    print("=" * 60)
    print("📦 LESSON 3: VARIABLES & USER INPUT")
    print("=" * 60)
    
    print(f"\n{name}, variables are like containers that store values!")
    
    if has_c_experience:
        print("\n🔄 COMPARISON TO C:")
        print("In C:")
        print("    char name[50];")
        print('    printf("What\'s your name? ");')
        print("    scanf('%s', name);")
        print('    printf("Hello, %s\\n", name);')
        print("\nIn Python:")
    
    print('    name = input("What\'s your name? ")')
    print('    print("Hello,", name)')
    
    print("\n✨ Key Differences:")
    print("• No need to declare variable types!")
    print("• No memory management needed")
    print("• input() function handles user input easily")
    print("• = assigns values to variables")
    
    # Interactive example
    print(f"\n🎮 Let's try it! I'll ask you some questions, {name}:")
    
    favorite_color = input("What's your favorite color? ").strip().title()
    favorite_number = input("What's your favorite number? ").strip()
    
    print(f"\n🎨 So {name}, your favorite color is {favorite_color}")
    print(f"🔢 And your favorite number is {favorite_number}")
    
    # Demonstrate string concatenation
    print("\n🔗 COMBINING STRINGS:")
    print("We can combine (concatenate) strings with +:")
    combined = "Your favorite color is " + favorite_color + "!"
    print(f"Result: {combined}")
    
    quiz_answer = get_input_with_validation(
        f"\n❓ {name}, what operator do we use to assign values to variables? ",
        ["=", "equals", "equal"]
    )
    
    print("🎯 Perfect! The = operator assigns values to variables!")
    pause_for_effect()

def lesson_strings_and_formatting(name, has_c_experience):
    """Lesson 4: Strings and String Formatting"""
    clear_screen()
    print("=" * 60)
    print("🔤 LESSON 4: STRINGS & FORMATTING")
    print("=" * 60)
    
    print(f"\n{name}, strings are sequences of text in Python!")
    
    if has_c_experience:
        print("\n🔄 COMPARISON TO C:")
        print("C strings are arrays of characters:")
        print("    char greeting[] = \"Hello\";")
        print("    printf(\"Hello, %s!\\n\", name);")
        print("\nPython strings are much more flexible:")
    
    print('    greeting = "Hello"')
    print('    print(f"Hello, {name}!")')
    
    # Demonstrate string methods
    print(f"\n🛠️ STRING METHODS - Let's use your name: '{name}'")
    
    print(f"• name.upper() → '{name.upper()}'")
    print(f"• name.lower() → '{name.lower()}'")
    print(f"• name.title() → '{name.title()}'")
    
    messy_input = "  " + name + "  "
    print(f"• '  {name}  '.strip() → '{messy_input.strip()}'")
    
    # F-strings demonstration
    print("\n🎯 F-STRINGS (Formatted String Literals):")
    print("The most elegant way to format strings!")
    
    age = input(f"\n{name}, how old are you? ").strip()
    
    print(f"\n📝 Different ways to create the same output:")
    print(f'1. print("Hello, {name}! You are {age} years old.")')
    print(f'2. print("Hello,", name, "! You are", age, "years old.")')
    print(f'3. print("Hello, " + name + "! You are " + age + " years old.")')
    print(f'4. print(f"Hello, {{name}}! You are {{age}} years old.")')
    
    best_method = get_input_with_validation(
        "\nWhich method looks cleanest to you? (1, 2, 3, or 4): ",
        ["1", "2", "3", "4"]
    )
    
    if best_method == "4":
        print("🎯 Excellent choice! F-strings are the most readable!")
    else:
        print("👍 That works too, but f-strings (option 4) are usually preferred!")
    
    pause_for_effect()

def lesson_integers_and_math(name, has_c_experience):
    """Lesson 5: Integers and Mathematical Operations"""
    clear_screen()
    print("=" * 60)
    print("🔢 LESSON 5: INTEGERS & MATH OPERATIONS")
    print("=" * 60)
    
    print(f"\n{name}, let's work with numbers in Python!")
    
    if has_c_experience:
        print("\n🔄 COMPARISON TO C:")
        print("In C:")
        print("    int x, y, result;")
        print('    printf("Enter x: ");')
        print("    scanf(\"%d\", &x);")
        print('    printf("Enter y: ");')
        print("    scanf(\"%d\", &y);")
        print("    result = x + y;")
        print('    printf("Result: %d\\n", result);')
        print("\nIn Python:")
    
    print('    x = int(input("Enter x: "))')
    print('    y = int(input("Enter y: "))')
    print('    result = x + y')
    print('    print(f"Result: {result}")')
    
    print("\n🎮 Let's build a calculator together!")
    
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        
        print(f"\n🧮 Math Operations with {x} and {y}:")
        print(f"• Addition: {x} + {y} = {x + y}")
        print(f"• Subtraction: {x} - {y} = {x - y}")
        print(f"• Multiplication: {x} * {y} = {x * y}")
        print(f"• Division: {x} / {y} = {x / y}")
        print(f"• Integer Division: {x} // {y} = {x // y}")
        print(f"• Modulo (remainder): {x} % {y} = {x % y}")
        print(f"• Exponentiation: {x} ** {y} = {x ** y}")
        
    except ValueError:
        print("🚫 Oops! You need to enter valid integers!")
        print("💡 This is why we use int() to convert strings to integers!")
    
    print("\n🔍 TYPE CONVERSION:")
    print("• input() always returns a STRING")
    print("• int() converts strings to integers")
    print("• This is called 'casting' or 'type conversion'")
    
    # Quiz
    quiz_answer = get_input_with_validation(
        f"\n❓ {name}, what happens if you don't use int() with input()? (add/concatenate): ",
        ["concatenate", "concat", "add strings", "string addition"]
    )
    
    print("🎯 Correct! Without int(), + would concatenate strings instead of adding numbers!")
    print("   Example: '5' + '3' = '53' (not 8!)")
    
    pause_for_effect()

def lesson_floats(name, has_c_experience):
    """Lesson 6: Floating Point Numbers"""
    clear_screen()
    print("=" * 60)
    print("🌊 LESSON 6: FLOATING POINT NUMBERS")
    print("=" * 60)
    
    print(f"\n{name}, floats are numbers with decimal points!")
    
    if has_c_experience:
        print("\n🔄 COMPARISON TO C:")
        print("In C:")
        print("    float x, y;")
        print('    printf("Enter x: ");')
        print("    scanf(\"%f\", &x);")
        print('    printf("Result: %.2f\\n", x);')
        print("\nIn Python:")
    
    print('    x = float(input("Enter x: "))')
    print('    print(f"Result: {x:.2f}")')
    
    print("\n🎮 Let's work with decimals!")
    
    try:
        x = float(input("Enter first decimal number: "))
        y = float(input("Enter second decimal number: "))
        
        result = x / y
        print(f"\n📊 Division Results:")
        print(f"• Exact result: {result}")
        print(f"• Rounded to 2 decimal places: {result:.2f}")
        print(f"• Rounded to nearest integer: {round(result)}")
        print(f"• With comma formatting: {result:,.2f}")
        
    except ValueError:
        print("🚫 Please enter valid decimal numbers!")
    except ZeroDivisionError:
        print("🚫 Cannot divide by zero!")
    
    print("\n✨ FORMATTING OPTIONS:")
    print("• {value:.2f} - 2 decimal places")
    print("• {value:,.2f} - with commas")
    print("• round(value, 2) - round to 2 decimal places")
    
    # Demonstrate precision issues
    print(f"\n🤔 Floating Point Precision Challenge:")
    print("Try this: 0.1 + 0.2")
    result = 0.1 + 0.2
    print(f"Result: {result}")
    print(f"Expected: 0.3")
    print(f"Why? Computer math with decimals isn't always exact!")
    
    format_choice = get_input_with_validation(
        f"\n❓ {name}, which format shows 2 decimal places: {{x:.2f}} or {{x:2f}}? ",
        ["{x:.2f}", ":.2f", ".2f", "first", "1"]
    )
    
    print("🎯 Correct! The colon and dot are important: {x:.2f}")
    
    pause_for_effect()

def lesson_functions_and_def(name, has_c_experience):
    """Lesson 7: Creating Custom Functions"""
    clear_screen()
    print("=" * 60)
    print("⚙️ LESSON 7: CREATING YOUR OWN FUNCTIONS")
    print("=" * 60)
    
    print(f"\n{name}, functions help organize and reuse code!")
    
    if has_c_experience:
        print("\n🔄 COMPARISON TO C:")
        print("In C:")
        print("    void greet(char* name) {")
        print('        printf("Hello, %s!\\n", name);')
        print("    }")
        print("    int main() {")
        print('        greet("World");')
        print("        return 0;")
        print("    }")
        print("\nIn Python:")
    
    print('    def greet(name):')
    print('        print(f"Hello, {name}!")')
    print('')
    print('    greet("World")')
    
    print("\n✨ Key Differences:")
    print("• def keyword instead of return type")
    print("• No semicolons or braces")
    print("• INDENTATION is crucial!")
    print("• No main() function required")
    
    # Interactive function creation
    print(f"\n🛠️ Let's create a function together, {name}!")
    
    function_name = input("What should we name our function? ").strip().lower()
    print(f"\n📝 Creating function '{function_name}':")
    
    print(f"def {function_name}():")
    print("    # Your code goes here")
    print("    pass  # placeholder")
    
    # Demonstrate function with parameters
    print("\n🎯 FUNCTIONS WITH PARAMETERS:")
    print("Functions can accept input values called parameters!")
    
    def demo_function(user_name, greeting="Hello"):
        return f"{greeting}, {user_name}! Welcome to Python!"
    
    result = demo_function(name)
    print(f"Result: {result}")
    
    # Function with return values
    print("\n🔄 RETURN VALUES:")
    print("Functions can send values back to the caller!")
    
    def calculate_square(number):
        return number ** 2
    
    test_number = 5
    squared = calculate_square(test_number)
    print(f"Square of {test_number} is {squared}")
    
    # Quiz
    indentation = get_input_with_validation(
        f"\n❓ {name}, what makes code part of a function in Python? ",
        ["indentation", "indent", "spaces", "tabs"]
    )
    
    print("🎯 Exactly! Indentation defines code blocks in Python!")
    print("   Everything indented under 'def' is part of the function!")
    
    pause_for_effect()

def lesson_main_function_pattern(name, has_c_experience):
    """Lesson 8: The main() Function Pattern"""
    clear_screen()
    print("=" * 60)
    print("🏗️ LESSON 8: THE MAIN() FUNCTION PATTERN")
    print("=" * 60)
    
    print(f"\n{name}, let's learn about organizing Python programs!")
    
    if has_c_experience:
        print("\n🔄 COMPARISON TO C:")
        print("In C, you always need main():")
        print("    int main() {")
        print("        // Your code here")
        print("        return 0;")
        print("    }")
        print("\nIn Python, main() is optional but recommended:")
    
    print('    def main():')
    print('        # Your main program code')
    print('        print("Hello, World!")')
    print('')
    print('    def helper_function():')
    print('        # Helper functions')
    print('        pass')
    print('')
    print('    main()  # Call main to start the program')
    
    print("\n✨ WHY USE main()?")
    print("• Better code organization")
    print("• Makes functions reusable")
    print("• Follows Python best practices")
    print("• Easier to test and debug")
    
    # Show common pattern
    print(f"\n📋 COMMON PYTHON PATTERN:")
    print("def main():")
    print("    name = input('What\\'s your name? ')")
    print("    greet(name)")
    print("")
    print("def greet(name):")
    print("    print(f'Hello, {name}!')")
    print("")
    print("main()")
    
    print(f"\n🤔 {name}, this might seem backwards at first!")
    print("We define main() but call it at the bottom.")
    print("This is because Python reads top-to-bottom!")
    
    # Advanced pattern
    print("\n🚀 ADVANCED PATTERN:")
    print("if __name__ == '__main__':")
    print("    main()")
    print("")
    print("This runs main() only when the script is run directly!")
    
    pattern_question = get_input_with_validation(
        f"\n❓ {name}, why might we put helper functions before main()? ",
        ["organization", "readable", "clarity", "structure", "order"]
    )
    
    print("🎯 Great thinking! It helps organize code and makes it more readable!")
    
    pause_for_effect()

def final_challenge(name):
    """Final coding challenge combining all concepts"""
    clear_screen()
    print("=" * 60)
    print("🏆 FINAL CHALLENGE: PUT IT ALL TOGETHER!")
    print("=" * 60)
    
    print(f"\n{name}, let's combine everything you've learned!")
    print("I'll describe a program, and you tell me what it does step-by-step.")
    
    print("\n📝 MYSTERY PROGRAM:")
    print("def mystery_program():")
    print("    name = input('Enter your name: ').strip().title()")
    print("    age = int(input('Enter your age: '))")
    print("    next_year = age + 1")
    print("    print(f'Hello, {name}!')")
    print("    print(f'Next year you will be {next_year} years old.')")
    print("")
    print("mystery_program()")
    
    print(f"\n🤔 {name}, what does this program do?")
    explanation = input("Explain in your own words: ").strip()
    
    print(f"\n🎯 Great explanation! Here's what it does:")
    print("1. Gets user's name and formats it nicely")
    print("2. Gets user's age and converts to integer")
    print("3. Calculates next year's age")
    print("4. Prints a personalized greeting")
    print("5. Tells them their age next year")
    
    # Bonus challenge
    print(f"\n🌟 BONUS CHALLENGE:")
    print("Can you spot the potential bug in this program?")
    
    bug_answer = input("What could go wrong? ").strip().lower()
    
    print("\n💡 Potential issues:")
    print("• What if someone enters text instead of a number for age?")
    print("• This would cause a ValueError!")
    print("• We should use try/except to handle this!")
    
    print(f"\n🎊 Congratulations, {name}!")
    print("You've completed the Python basics course!")
    
    pause_for_effect()

def graduation_ceremony(name):
    """Celebrate the completion of the course"""
    clear_screen()
    print("=" * 60)
    print("🎓 GRADUATION CEREMONY!")
    print("=" * 60)
    
    print(f"\n🎉 Congratulations, {name}! 🎉")
    print("\nYou have successfully learned:")
    
    concepts = [
        "✅ Hello World programs and functions",
        "✅ Debugging and error handling", 
        "✅ Variables and user input",
        "✅ Strings and formatting",
        "✅ Integers and mathematical operations",
        "✅ Floating point numbers",
        "✅ Creating custom functions",
        "✅ Code organization with main()"
    ]
    
    for concept in concepts:
        print(concept)
        time.sleep(0.5)
    
    print(f"\n🌟 {name}, you're ready to:")
    print("• Write your own Python programs")
    print("• Debug common errors")
    print("• Use functions effectively")
    print("• Handle user input properly")
    print("• Format output beautifully")
    
    print(f"\n📚 NEXT STEPS:")
    print("• Practice writing small programs")
    print("• Learn about loops and conditionals")
    print("• Explore data structures (lists, dictionaries)")
    print("• Build projects that interest you!")
    
    print(f"\n💝 Thank you for learning with me, {name}!")
    print("Keep coding and have fun! 🐍✨")

def main():
    """Main program orchestrating the learning experience"""
    try:
        # Welcome and personalization
        name, has_c_experience = welcome_user()
        
        # Core lessons
        lesson_hello_world(name, has_c_experience)
        lesson_bugs_and_errors(name)
        lesson_variables_and_input(name, has_c_experience)
        lesson_strings_and_formatting(name, has_c_experience)
        lesson_integers_and_math(name, has_c_experience)
        lesson_floats(name, has_c_experience)
        lesson_functions_and_def(name, has_c_experience)
        lesson_main_function_pattern(name, has_c_experience)
        
        # Final assessment
        final_challenge(name)
        
        # Celebration
        graduation_ceremony(name)
        
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for learning with me! Come back anytime!")
    except Exception as e:
        print(f"\n🚫 An unexpected error occurred: {e}")
        print("Don't worry - errors are part of learning programming!")

if __name__ == "__main__":
    main()