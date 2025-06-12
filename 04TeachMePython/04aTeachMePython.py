#!/usr/bin/env python3
"""
interactive_libraries_tutorial.py

📚 This interactive Python program teaches or refreshes your memory on using libraries in Python,
including built-in modules, third-party packages, APIs, and how to make your own library.

✨ Topics Covered:
    - Importing libraries (`import`, `from ... import`)
    - random (choice, randint, shuffle)
    - statistics (mean)
    - Command-line arguments (sys.argv, defensive programming, sys.exit)
    - Slicing
    - Installing and using packages (pip, cowsay)
    - APIs using requests and JSON
    - Writing and using your own libraries

👶 Familiar characters like Peter Rabbit 🐰, the Famous Five 🧒👧🐶, and friends from the Faraway Tree 🍄 will join in to help you learn!

💡 Requirements:
    - Python 3.6 or newer
    - cowsay: `pip install cowsay`
    - requests: `pip install requests`

🚫 No extra .py files are required! All functionality is self-contained in this one script.
"""

import sys
import random
import statistics
import requests
import json
import time

def ask_name():
    name = input("👋 Hello there! What’s your name? ")
    print(f"Nice to meet you, {name}! 🐰 Let’s have some fun learning Python libraries together!\n")
    return name

def wait():
    input("⏳ Press Enter to continue...")

def explain_imports(name):
    print("\n📦 Let’s start with importing libraries!")
    print(f"{name}, sometimes instead of writing everything from scratch, we use existing tools in Python called *modules* or *libraries*.")
    print("Example: importing the `random` module to simulate Peter Rabbit flipping a coin...")

    print("\nCode:")
    print("    import random\n    coin = random.choice(['heads', 'tails'])\n    print(coin)")

    coin = random.choice(["heads", "tails"])
    print(f"\n🐰 Peter Rabbit flips a coin... It's {coin}!")
    wait()

def play_with_random(name):
    print("\n🎲 Let’s explore more randomness with the Famous Five!")
    print("Julian rolls a dice using `randint(1, 6)`:")

    dice_roll = random.randint(1, 6)
    print(f"🎲 Julian rolled a {dice_roll}!")

    print("\nNow let’s shuffle their adventure cards...")
    cards = ["Find treasure", "Escape smugglers", "Explore caves"]
    print("Before shuffle:", cards)
    random.shuffle(cards)
    print("After shuffle:", cards)
    wait()

def statistics_demo(name):
    print("\n📊 Let’s calculate the average score from the Faraway Tree kids using the `statistics` module.")

    scores = [88, 92, 79, 93]
    print(f"Scores: {scores}")
    avg = statistics.mean(scores)
    print(f"Their average score is: {avg}")
    wait()

def command_line_intro(name):
    print("\n💻 Sometimes, programs take input from the command line using `sys.argv`.")
    print("We use `sys.argv[1]` to get the first argument after the script name.")
    print("Here’s a quick simulation:")

    fake_args = ["script.py", "Moon-Face"]
    print("Simulated command-line input:", fake_args)
    if len(fake_args) == 2:
        print("🎉 Hello, my name is", fake_args[1])
    else:
        print("⚠️ Too few or too many arguments!")
    wait()

def slice_demo(name):
    print("\n🔪 Let’s use slice notation to greet multiple characters (and ignore the script name).")
    args = ["script.py", "Silky", "Moon-Face", "Saucepan Man"]
    for friend in args[1:]:
        print(f"🌟 Hello, {friend}!")
    wait()

def cowsay_demo(name):
    print("\n🐄 Time for a fun package called `cowsay`! You need to install it using `pip install cowsay`.")
    try:
        import cowsay
        cowsay.trex(f"Hello, {name} from the Enchanted Wood!")
    except ImportError:
        print("❌ cowsay not installed. Run: pip install cowsay")
    wait()

def api_demo(name):
    print("\n🌐 Let’s access a web API to find music using `requests` and `json`.")
    try:
        search = input("🔍 What artist would you like to search on iTunes? ").strip()
        url = f"https://itunes.apple.com/search?entity=song&limit=3&term={search}"
        response = requests.get(url)
        data = response.json()
        print(f"\n🎧 Songs by {search}:")
        for song in data["results"]:
            print("🎵", song.get("trackName", "Unknown Track"))
    except Exception as e:
        print("⚠️ Oops, something went wrong:", e)
    wait()

def make_your_own_library_demo(name):
    print("\n🛠️ You can also make your own library! Let’s simulate that by defining two functions right here:")
    
    def hello(person):
        print(f"👋 hello, {person}")
    def goodbye(person):
        print(f"👋 goodbye, {person}")
    
    friend = input("Type the name of a character you want to greet and say goodbye to: ")
    hello(friend)
    goodbye(friend)
    wait()

def final_quiz(name):
    print("\n🧠 Let’s wrap up with a mini quiz!")
    score = 0

    q1 = input("1️⃣ What module lets us generate random choices? ").strip().lower()
    if q1 == "random":
        score += 1

    q2 = input("2️⃣ What function helps calculate the average of numbers? ").strip().lower()
    if q2 == "mean":
        score += 1

    q3 = input("3️⃣ What does `sys.argv[0]` usually contain? ").strip().lower()
    if "script" in q3 or ".py" in q3:
        score += 1

    print(f"\n🎉 Well done, {name}! You scored {score}/3! 🏆")
    print("Thanks for learning with Peter Rabbit, the Famous Five, and friends from the Faraway Tree!")
    print("✨ Keep coding and exploring!\n")

def main():
    print("🚀 Welcome to the Interactive Libraries Tutorial!")
    name = ask_name()
    explain_imports(name)
    play_with_random(name)
    statistics_demo(name)
    command_line_intro(name)
    slice_demo(name)
    cowsay_demo(name)
    api_demo(name)
    make_your_own_library_demo(name)
    final_quiz(name)

if __name__ == "__main__":
    print("🚀 Welcome to the Interactive Libraries Tutorial!")
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Goodbye! Thanks for learning with us!")
        sys.exit(0)
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")
        sys.exit(1)