"""
🎉 Art Explorer 2.0 - Search Artists and Artworks using Python Modules & Packages 🎨

This Python program demonstrates how to:
- Structure code with reusable modules
- Organize code in a custom package
- Use abstraction to keep the code clean
- Interact with a real-world API
- Make things fun and user-friendly 🤹

Dependencies:
- Python 3.x
- `requests` library (`pip install requests`)
"""

from museum.artists import get_artists
from museum.artwork import get_artwork

def main():
    print("🎨 Welcome to Art Explorer 2.0!")
    print("You can search for artists 🧑‍🎨 or artworks 🖼️ from the Art Institute of Chicago.\n")

    while True:
        choice = input("🔍 Type 'artist' or 'artwork' (or 'exit' to quit): ").strip().lower()

        if choice == 'exit':
            print("👋 Thanks for visiting the Art Explorer. Goodbye!")
            break
        elif choice in ['artist', 'artwork']:
            query = input("📝 What would you like to search for? ").strip()
            if not query:
                print("⚠️ You must enter something to search for!\n")
                continue
            limit = 5

            if choice == 'artist':
                results = get_artists(query, limit)
            else:
                results = get_artwork(query, limit)

            if results:
                print(f"\n✅ Found {len(results)} result(s):")
                for i, result in enumerate(results, 1):
                    print(f"{i}. {result}")
            else:
                print("😕 No results found. Try a different query.")

        else:
            print("🚫 Invalid option. Please type 'artist', 'artwork', or 'exit'.\n")

        print("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    main()
