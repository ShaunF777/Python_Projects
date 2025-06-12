#!/usr/bin/env python3
"""
silly_sayer.py

🎤 Uses your custom 'sayings' library to greet or farewell a friend in a silly way.

📌 USAGE:
    python silly_sayer.py hello Silky
    python silly_sayer.py goodbye Julian

🧠 NOTE:
    - First argument: "hello" or "goodbye"
    - Second argument: the name of the person/character

🎉 Examples:
    python silly_sayer.py hello Moon-Face
    python silly_sayer.py goodbye Peter

💡 Depends on:
    - sayings.py (must be in the same folder)
"""

import sys
from sayings import hello, goodbye

if len(sys.argv) != 3:
    sys.exit("❌ Usage: python silly_sayer.py [hello|goodbye] name")

action, name = sys.argv[1], sys.argv[2]

if action == "hello":
    hello(name)
elif action == "goodbye":
    goodbye(name)
else:
    sys.exit("❌ First argument must be either 'hello' or 'goodbye'.")
