#!/usr/bin/env python3
"""
silly_sentence.py

🎩✨ Welcome to the Silly Sentence Generator! ✨🎩

This script creates a silly sentence using words you provide on the command line.
Perfect for wordplay fans, Peter Rabbit, or the Famous Five! 🐰🧒👧

📌 USAGE:
    python silly_sentence.py noun adjective verb adverb

📌 EXAMPLE:
    python silly_sentence.py rabbit blue dances happily

📌 OUTPUT:
    "The blue rabbit dances happily through the Faraway Tree!"

🚨 You must provide exactly 4 arguments: a noun, an adjective, a verb, and an adverb.

💡 Dependencies:
    Only Python 3 — no extra installations required.
"""

import sys
import random

if len(sys.argv) != 5:
    sys.exit("❌ Please provide exactly 4 words: noun adjective verb adverb\nExample: python silly_sentence.py rabbit blue jumps joyfully")

# Assign the arguments to named variables
_, noun, adjective, verb, adverb = sys.argv

# Fun places and objects for variety
places = ["the Faraway Tree", "Rabbit Hollow", "Kirrin Island", "a picnic with the Famous Five"]
endings = ["!", " under the moon 🌝.", " with wild giggles 🎉.", " like nobody's watching 💃."]

# Compose the silly sentence
place = random.choice(places)
ending = random.choice(endings)
sentence = f"The {adjective} {noun} {verb} {adverb} through {place}{ending}"

# Print the final output
print("📝 Your Silly Sentence:")
print(sentence)
