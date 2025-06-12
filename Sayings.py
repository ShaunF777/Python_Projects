"""
04cSayings.py

🐰 Silly Sayings Library 🐰

A tiny, whimsical library to help your characters from the Faraway Tree, Peter Rabbit's burrow,
or Kirrin Island say hello and goodbye in fun, character-themed ways!

✌️ FUNCTIONS:
    - hello(name): Cheerful greeting with random flair
    - goodbye(name): Dramatic, silly goodbye

🚫 This file doesn't run on its own — it's meant to be imported into another script!

"""

import random

def hello(name):
    greetings = [
        f"🌞 A cheery hello to you, {name}!",
        f"🧁 Fancy a scone, {name}? Hello there!",
        f"🌿 {name}, you've just stumbled out of the Enchanted Wood — hello!",
        f"🐾 Peter Rabbit tips his hat to you, {name}!",
    ]
    print(random.choice(greetings))

def goodbye(name):
    farewells = [
        f"🚪 {name} vanishes behind a magical tree stump. Goodbye!",
        f"👋 So long, {name}! Mind the goblins on your way out!",
        f"🏞️ {name} sails off from Kirrin Island waving madly. Goodbye!",
        f"🦊 Mr. Tod says... well, nothing nice, but *we* say goodbye, {name}!",
    ]
    print(random.choice(farewells))
