# This program interactively teaches fundamental Python concepts
# including exceptions (ValueError, NameError), error handling with
# try, except, else, and the use of while loops, break, pass, functions,
# and parameters for robust user input. It's designed to be a
# memory refresher or an introductory guide.
#
# Dependencies:
# - Python 3 (standard library only, no external modules needed)

import sys
import time


def slow_print(text, delay=0.03):
    """Prints text character by character for a more engaging experience."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Add a newline at the end


def get_user_input(prompt):
    """Helper function to get user input with a slight delay."""
    slow_print(prompt)
    return input()


def main():
    """
    The main function that orchestrates the interactive Python lesson.
    """
    slow_print("Hello there, curious coder! �")
    user_name = get_user_input("What's your name, if you don't mind me asking? 🤔 ")
    slow_print(f"Ah, {user_name}! A wonderful name for a budding Python enthusiast!")
    slow_print(
        "I'm your friendly Python tutor, and we're about to embark on a little adventure,"
    )
    slow_print(
        "with some help from Peter Rabbit, The Famous Five, and friends from the Faraway Tree! 🐰🌳📚"
    )
    slow_print("-" * 60)
    slow_print("\nOur first stop on this coding journey: Syntax Errors! 🐛")
    slow_print(
        "Imagine Peter Rabbit trying to read a recipe but some words are missing punctuation."
    )
    slow_print(
        "He wouldn't understand it, right? That's what a syntax error is for Python! 📜❌"
    )
    time.sleep(1)
    slow_print(
        "Python needs you to type your code *just so*. Let's look at a classic mistake:"
    )
    slow_print("```python")
    slow_print('print("hello, world)')
    slow_print("```")
    slow_print("Can you spot the missing piece in that line, {user_name}? 🤔")
    slow_print("It's like a missing comma in Mrs. Tiggy-Winkle's laundry list! 🧺")
    get_user_input("Press Enter to reveal the answer... ")
    slow_print(
        "Yes! You're right, there's a missing closing quotation mark after 'world'."
    )
    slow_print("Python would get a 'SyntaxError: EOL while scanning string literal'.")
    slow_print(
        "These errors mean Python couldn't even understand *what* you wanted to say! 🤯"
    )
    slow_print("-" * 60)

    slow_print(
        "\nNow, sometimes Python understands your words, but then something unexpected happens *while the program is running*."
    )
    slow_print("These are called **Runtime Errors** or **Exceptions**! 💥")
    slow_print(
        "Think of it this way: what if Peter Rabbit asked for '10 carrots' 🥕 but you tried to give him a 'fluffy cloud'? ☁️"
    )
    slow_print("He wouldn't know what to do with a cloud when he expects a number! 🤷‍♂️")
    slow_print("Python tries to convert your input into a number using `int()`.")
    slow_print(
        "But what if you type 'potato' 🥔 instead of '5'? That's a `ValueError`! Let's see it in action."
    )

    slow_print("\n--- Demonstrating ValueError (Expected Failure) ---")
    slow_print(
        "Try typing something that isn't a whole number, like 'cat' or 'fluffy'."
    )
    try:
        x_val = int(get_user_input("What's your favourite number, {user_name}? "))
        slow_print(f"Great! Your favourite number is {x_val}! 👍")
    except ValueError:
        slow_print(
            "Oops! Python just threw a `ValueError`! It means it couldn't turn your input into a whole number. 😩"
        )
        slow_print("Just like Peter Rabbit can't turn a cloud into a carrot! 🥕➡️☁️")
    slow_print(
        "See how the program stopped when it hit the error? We need a safety net! 🥅"
    )
    slow_print("-" * 60)

    slow_print("\nThis is where `try` and `except` come in handy, {user_name}!")
    slow_print("It's like setting up a safety net for when things go a bit wobbly! 🤸‍♀️")
    slow_print(
        "We 'try' a piece of code, and if something goes 'except'-ional (meaning, an exception occurs),"
    )
    slow_print("we tell Python what to do instead of just crashing. 🛡️")
    time.sleep(1)
    slow_print("Let's try that number input again, but with a `try-except` block:")

    slow_print("```python")
    slow_print("try:")
    slow_print("    y = int(input('How many acorns did Squirrel Nutkin gather? '))")
    slow_print("    print(f'Squirrel Nutkin gathered {y} acorns! 🌰')")
    slow_print("except ValueError:")
    slow_print(
        "    print('That's not a valid number of acorns, {user_name}! Please try again with a whole number. 🐿️')"
    )
    slow_print(
        "print(f'After the attempt, we move on!') # This line is outside the try-except-else block"
    )
    slow_print("```")
    slow_print("\n--- Testing `try-except` Basic ---")
    slow_print("Try typing a number, then try typing something like 'many' or 'none'.")
    try:
        y = int(get_user_input("How many acorns did Squirrel Nutkin gather? 🐿️ "))
        slow_print(f"Squirrel Nutkin gathered {y} acorns! 🌰 That's a good count! 👍")
    except ValueError:
        slow_print(
            f"That's not a valid number of acorns, {user_name}! Python says 'ValueError' for 'many'! 😩"
        )
    slow_print(
        f"See, {user_name}? The program didn't crash this time! We caught the error! 🎉"
    )
    slow_print("-" * 60)

    slow_print(
        "\nNow for a tricky bit, {user_name}, like when Julian, Dick, and Anne got separated in a cave! 🔦"
    )
    slow_print(
        "What if our `print` statement for `x` was *outside* the `try-except` block, and an error happened?"
    )
    slow_print("```python")
    slow_print("try:")
    slow_print("    # If this line fails, 'z' is never created!")
    slow_print("    z = int(input('How many adventures did the Famous Five have? '))")
    slow_print("except ValueError:")
    slow_print("    print('That's not a number!')")
    slow_print(
        "print(f'The Famous Five had {z} adventures!') # ERROR: z might not be defined!"
    )
    slow_print("```")
    slow_print(
        "If `int(input(...))` fails, `z` never gets a value! Python wouldn't know what `z` is when it tries to print it later!"
    )
    slow_print("This would cause a `NameError`! 📛")
    slow_print(
        "This is where the `else` block comes in handy, like a clear path through the woods! 🌲"
    )
    slow_print(
        "The `else` block runs *only if* the `try` block finishes without any exceptions. 🌟"
    )
    time.sleep(1)
    slow_print("Let's refine our code with `else`:")
    slow_print("```python")
    slow_print("try:")
    slow_print(
        "    adventures = int(input('How many magical creatures live in the Faraway Tree? ✨ '))"
    )
    slow_print("except ValueError:")
    slow_print(
        "    slow_print('That's not a valid number of magical creatures, {user_name}! 🧚‍♀️❌')"
    )
    slow_print("else:")
    slow_print(
        "    slow_print(f'Wow, {user_name}! {adventures} magical creatures live in the Faraway Tree! 🌈')"
    )
    slow_print("```")
    slow_print("\n--- Testing `try-except-else` ---")
    slow_print("Try entering a number first, then try entering something non-numeric.")
    while True:
        try:
            creatures = int(
                get_user_input(
                    "How many magical creatures live in the Faraway Tree? ✨ "
                )
            )
        except ValueError:
            slow_print(
                f"That's not a valid number of magical creatures, {user_name}! Python wants a whole number. 🧚‍♀️❌"
            )
        else:
            slow_print(
                f"Wow, {user_name}! {creatures} magical creatures live in the Faraway Tree! 🌈 That's a great count! 👍"
            )
            break  # Exit the loop if valid input is received
    slow_print(
        f"So, {user_name}, with `else`, our `print` statement for `adventures` (or `creatures` here) is only attempted when we know it has a valid number! ✅"
    )
    slow_print("-" * 60)

    slow_print(
        "\nBut {user_name}, are we being a bit like Mr. Tod, just giving up when things go wrong? 🦊"
    )
    slow_print(
        "We want to be persistent, like Benjamin Bunny trying to get his shoes back! 👟🐰"
    )
    slow_print(
        "Instead of just printing an error and stopping, we can keep asking the user for input until they get it right!"
    )
    slow_print(
        "We use a `while True` loop for this, and `break` when we're happy with the input! 🔄"
    )
    time.sleep(1)
    slow_print("Let's combine `while True` with `try-except-else-break`:")
    slow_print("```python")
    slow_print("while True:")
    slow_print("    try:")
    slow_print(
        "        biscuits = int(input('How many ginger biscuits did Peter Rabbit eat? 🍪 '))"
    )
    slow_print("    except ValueError:")
    slow_print(
        "        print('That's not a number of biscuits, Peter Rabbit would be disappointed! 😔')"
    )
    slow_print("    else:")
    slow_print("        print(f'Peter Rabbit ate {biscuits} ginger biscuits! Yum! 😋')")
    slow_print("        break # Success! Exit the loop.")
    slow_print("```")
    slow_print("\n--- Testing `while True` Loop with `try-except-else` ---")
    slow_print(
        "Now, try typing wrong input multiple times, then finally type a number."
    )
    while True:
        try:
            biscuits = int(
                get_user_input("How many ginger biscuits did Peter Rabbit eat? 🍪 ")
            )
        except ValueError:
            slow_print(
                f"That's not a number of biscuits, {user_name}! Peter Rabbit would be disappointed! 😔 Try again!"
            )
        else:
            slow_print(
                f"Excellent, {user_name}! Peter Rabbit ate {biscuits} ginger biscuits! Yum! 😋"
            )
            break
    slow_print(
        f"See how this makes our program much more user-friendly, {user_name}? 👍"
    )
    slow_print(
        "It's like Jemima Puddle-Duck finally finding a safe place for her eggs! 🦢🥚"
    )
    slow_print("-" * 60)

    slow_print(
        "\nNow, {user_name}, imagine if whenever we needed a number, we had to write all that `while True-try-except-else-break` code every time. ✍️"
    )
    slow_print(
        "That would be more tedious than sorting all the Lost Property in the Faraway Tree! 🧺😩"
    )
    slow_print(
        "This is where **functions** come in! We can bundle up that useful code into a reusable block. 📦"
    )
    slow_print("Let's create a `get_int()` function to do all the hard work for us!")
    time.sleep(1)
    slow_print("Here's how we'd structure it:")
    slow_print("```python")
    slow_print("def main():")
    slow_print("    num_stories = get_int()")
    slow_print("    print(f'Enid Blyton wrote {num_stories} stories!')")
    slow_print("")
    slow_print("def get_int():")
    slow_print("    while True:")
    slow_print("        try:")
    slow_print("            val = int(input('Enter a whole number: '))")
    slow_print("        except ValueError:")
    slow_print("            print('Not a whole number, please try again!')")
    slow_print("        else:")
    slow_print(
        "            return val # Success! Return the value and exit the loop/function."
    )
    slow_print("```")
    slow_print("\n--- Demonstrating `get_int` Function ---")

    def get_int_demo_1():
        while True:
            try:
                val = int(
                    get_user_input(
                        "How many books did Enid Blyton write about The Famous Five? 📚 "
                    )
                )
            except ValueError:
                slow_print(
                    f"That's not a whole number, {user_name}! Please try again. 🧐"
                )
            else:
                return val

    num_blyton_books = get_int_demo_1()
    slow_print(
        f"Enid Blyton wrote approximately {num_blyton_books} books about The Famous Five! That's a lot of adventures! 🌳🕵️‍♀️"
    )
    slow_print(f"Isn't that neat, {user_name}? Now, our `main()` part is much cleaner!")
    slow_print(
        "It's like separating the different rooms in the Faraway Tree – each one has a specific job! 🏡"
    )
    slow_print("-" * 60)

    slow_print(
        "\nWe can make our `get_int` function even more streamlined, {user_name}! 🚀"
    )
    slow_print(
        "Python allows us to `return` a value directly from inside the `try` block, which also exits the loop and the function!"
    )
    slow_print(
        "It makes the code a bit more compact, just like how Noddy and Big-Ears always find the quickest way home! 🚗💨"
    )
    slow_print("```python")
    slow_print("def get_int_streamlined():")
    slow_print("    while True:")
    slow_print("        try:")
    slow_print(
        "            # If successful, this line returns the value AND exits the loop/function!"
    )
    slow_print("            return int(input('Enter a number for me, {user_name}: '))")
    slow_print("        except ValueError:")
    slow_print("            print('Still not a whole number. Try again, please! 🔄')")
    slow_print("```")
    slow_print("\n--- Demonstrating Streamlined `get_int` Function ---")

    def get_int_streamlined_demo():
        while True:
            try:
                return int(
                    get_user_input(
                        f"Let's try again, {user_name}. How many friends does Peter Rabbit have? 🥕 "
                    )
                )
            except ValueError:
                slow_print("Still not a whole number. Try again, please! 🔄")

    num_friends = get_int_streamlined_demo()
    slow_print(f"Peter Rabbit has {num_friends} friends! That's a lovely thought! 🐰🤝")
    slow_print("-" * 60)

    slow_print(
        "\nSometimes, {user_name}, we don't want to tell the user *exactly* what went wrong,"
    )
    slow_print(
        "but just quietly ask again. Like when Fatty-Pies just nods and re-offers you a biscuit! 🍪"
    )
    slow_print(
        "The `pass` keyword in Python does exactly that: it's a placeholder that does nothing. "
    )
    slow_print(
        "If an exception occurs, `pass` is executed, and then the loop just continues, re-prompting the user without a fuss. 🤫"
    )
    slow_print("```python")
    slow_print("def get_int_quiet():")
    slow_print("    while True:")
    slow_print("        try:")
    slow_print("            return int(input('What's your secret number? 🤔 '))")
    slow_print("        except ValueError:")
    slow_print("            pass # Just silently re-ask.")
    slow_print("```")
    slow_print("\n--- Demonstrating `pass` Keyword ---")
    slow_print(
        "Try typing incorrect input multiple times, notice there's no error message this time."
    )

    def get_int_quiet_demo():
        while True:
            try:
                return int(
                    get_user_input(
                        f"Okay, {user_name}, how many magic coins did Silky acquire? 🪙 "
                    )
                )
            except ValueError:
                pass

    magic_coins = get_int_quiet_demo()
    slow_print(f"Silky acquired {magic_coins} magic coins! What a treasure! ✨")
    slow_print(
        f"So, {user_name}, if you want to be less verbose with error messages, `pass` is your friend!"
    )
    slow_print("-" * 60)

    slow_print(
        "\nFinally, {user_name}, a super useful improvement for our `get_int` function! 🤩"
    )
    slow_print(
        "What if we want to ask different questions for different numbers? Right now, it always asks a fixed question."
    )
    slow_print(
        "We can make our function more flexible by adding a `prompt` **parameter**. 📝"
    )
    slow_print(
        "This means we can pass in the question we want the user to see, like how Moon-Face always has a new riddle! 🌕❓"
    )
    slow_print("```python")
    slow_print("def get_int_flexible(prompt_message):")
    slow_print("    while True:")
    slow_print("        try:")
    slow_print("            return int(input(prompt_message))")
    slow_print("        except ValueError:")
    slow_print("            pass # Quietly re-ask if invalid input.")
    slow_print("")
    slow_print("# Example usage:")
    slow_print(
        "num_biscuits = get_int_flexible('How many biscuits did Fatty-Pies offer? 🍪 ')"
    )
    slow_print(
        "num_adventures = get_int_flexible('How many adventures did the Famous Five have? 🗺️ ')"
    )
    slow_print("```")
    slow_print("\n--- Demonstrating Flexible `get_int` with Parameter ---")

    def get_int_flexible_demo(prompt_message):
        while True:
            try:
                return int(get_user_input(prompt_message))
            except ValueError:
                pass

    fatty_pies_biscuits = get_int_flexible_demo(
        f"First, {user_name}, how many biscuits did Fatty-Pies offer you? 🍪 "
    )
    slow_print(
        f"You received {fatty_pies_biscuits} biscuits from Fatty-Pies! What a treat! 😋"
    )

    famous_five_adventures = get_int_flexible_demo(
        f"And {user_name}, how many thrilling adventures did the Famous Five have? 🗺️ "
    )
    slow_print(
        f"The Famous Five had {famous_five_adventures} thrilling adventures! Absolutely smashing! 🤩"
    )

    slow_print(f"Now our `get_int` function is super versatile, {user_name}!")
    slow_print(
        "You can ask for anything – how many carrots Peter Rabbit hid, or how many pixies live in the Faraway Tree! 🥕🧚‍♀️"
    )
    slow_print("-" * 60)

    slow_print(
        "\nPhew! We've covered a lot today, {user_name}! You're becoming a Python pro,"
    )
    slow_print(
        "just like Julian, Dick, Anne, George, and Timmy the dog solving a mystery! 🕵️‍♀️🐕"
    )
    slow_print("\nWe refreshed our memory on:")
    slow_print(
        "✨ **Exceptions and Runtime Errors**: When things go awry during a program's run."
    )
    slow_print("✨ **`try` and `except`**: Our safety net for catching those errors.")
    slow_print("✨ **`else`**: Running code only when the `try` block succeeds.")
    slow_print(
        "✨ **`while True` and `break`**: Persistently getting valid input from the user."
    )
    slow_print(
        "✨ **Functions (`def`)**: Reusing blocks of code for clarity and efficiency."
    )
    slow_print(
        "✨ **`return`**: Getting values back from functions and exiting loops efficiently."
    )
    slow_print(
        "✨ **`pass`**: A quiet way to handle errors and continue without explicit messages."
    )
    slow_print("✨ **Parameters**: Making our functions flexible and reusable!")
    slow_print(
        "\nGreat job, {user_name}! Keep practicing, and your Python skills will grow stronger than a Wishing-Chair's magic! ✨"
    )
    slow_print("Farewell for now! 👋")


if __name__ == "__main__":
    main()
# This line ensures the main function runs when the script is executed directly
# but not when imported as a module.
