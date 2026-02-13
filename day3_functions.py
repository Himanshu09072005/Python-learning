def process_name(name):
    clean_name = " ".join(name.strip().title().split())
    
    # Remove spaces before validation
    if not clean_name.replace(" ", "").isalpha():
        return None, None
    
    letter_count = len(clean_name.replace(" ", ""))
    return clean_name, letter_count


user_input = input("Enter your name: ")

formatted_name, count = process_name(user_input)

if formatted_name is None:
    print("Invalid name. Only letters allowed.")
else:
    print(f"Hello {formatted_name}, welcome to Day 3!")
    print(f"Your name has {count} letters (excluding spaces).")
