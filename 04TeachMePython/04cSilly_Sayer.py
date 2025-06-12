#!/usr/bin/env python3
"""
04cSilly_Sayer.py

🎤 Uses your custom 'sayings' library to greet or farewell a friend in a silly way.

📌 USAGE:
    python 04cSilly_Sayer.py hello Silky
    python 04cSilly_Sayer.py goodbye Julian

🧠 NOTE:
    - First argument: "hello" or "goodbye"
    - Second argument: the name of the person/character

🎉 Examples:
    python 04cSilly_Sayer.py hello Moon-Face
    python 04cSilly_Sayer.py goodbye Peter

🗂️ Folder Structure
    your_project/
    │
    ├── Sayings.py
    ├── 04cSilly_Sayer.py

💡 Depends on:
    - Sayings.py (must be in the same folder)
"""

import sys
from Sayings import hello, goodbye

if len(sys.argv) != 3:
    sys.exit("❌ Usage: python silly_sayer.py [hello|goodbye] name")

action, name = sys.argv[1], sys.argv[2]

if action == "hello":
    hello(name)
elif action == "goodbye":
    goodbye(name)
else:
    sys.exit("❌ First argument must be either 'hello' or 'goodbye'.")
