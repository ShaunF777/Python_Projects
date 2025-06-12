"""
🎨 Art Explorer - Powered by the Art Institute of Chicago API 🎨

This Python 3 script demonstrates how to use a public API using `requests`.
It shows how to:
- Make HTTP GET requests to an API
- Handle JSON data (JavaScript Object Notation)
- Use query parameters to filter data (search by artist)
- Handle connection errors gracefully
- Display data in a human-friendly way

✨ Dependencies:
- Python 3.x
- `requests` library (install with `pip install requests`)

Just run the script and enter an artist's name (e.g., Monet, Picasso, Kahlo) to discover artworks from the museum! 🖼️✨
"""

import sys
import requests
import random

def main():
    print("🎉 Welcome to Art Explorer! 🖼️")
    print("Let's search the Art Institute of Chicago for some masterpieces.\n")

    artist = input("🔍 Enter an artist's name to search (e.g., Monet, Van Gogh, O'Keeffe): ").strip()

    if not artist:
        print("🚫 You didn't type anything. Goodbye!")
        return

    try:
        # Add query parameters (search query and limit number of results)
        params = {
            "q": artist,
            "limit": random.randint(3, 7)  # Randomize how many artworks we show (make it playful)
        }

        response = requests.get("https://api.artic.edu/api/v1/artworks/search", params)
        response.raise_for_status()

    except requests.HTTPError as http_err:
        print("❌ HTTP error occurred:", http_err)
        sys.exit(1)
    except requests.RequestException as err:
        print("❌ Connection error:", err)
        sys.exit(1)

    # Convert the response to JSON
    content = response.json()

    # Get the list of artworks
    artworks = content.get("data", [])

    if not artworks:
        print(f"😞 No artworks found for '{artist}'. Try another artist!")
        return

    # Show results with emojis and fun formatting
    print(f"\n🎨 Found {len(artworks)} artwork(s) by '{artist.title()}':\n")
    for i, artwork in enumerate(artworks, 1):
        title = artwork.get("title", "Untitled")
        print(f"{i}. 🖌️ {title}")

    print("\n✨ Thanks for exploring the art world with us! ✨")

if __name__ == "__main__":
    main()
