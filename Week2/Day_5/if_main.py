# --- What is `if __name__ == "__main__"`? ---

# When you run a Python file directly, Python sets the special variable __name__ to "__main__".
# This condition lets you control code execution:
# - Code inside this block runs only when the file is executed directly.
# - It DOES NOT run if the file is imported as a module in another script.

def main():
    print("This runs when the script is executed directly.")

if __name__ == "__main__":
    main()
