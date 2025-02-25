import pyperclip
import sys

# Function to process the pasted list and return a comma-separated string
def process_list(items, add_quotes):
    # Optionally wrap each item with quotes based on user input
    if add_quotes.lower() == 'y':
        items = [f'"{item.strip()}"' for item in items]
    else:
        items = [item.strip() for item in items]
    
    # Join the items with a comma and a space
    return ', '.join(items)

if __name__ == "__main__":
    # Ask the user if they want to add quotes
    add_quotes = input("Do you want to add quotes around each item? (y/n): ").strip()

    # Ask the user to paste the list
    print("Please paste the list of items (one per line). Press Enter twice when done:")
    lines = []
    while True:
        line = input().strip()
        if line == "":
            break
        lines.append(line)

    # Process the list
    result = process_list(lines, add_quotes)

    # Copy the result to the clipboard
    pyperclip.copy(result)

    # Inform the user
    print(f"Formatted list copied to clipboard: {result}")

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    processed_output = user_input.replace(" ", ",")  # Example: Replace spaces with commas
    print(processed_output)
else:
    print("No input provided.")
