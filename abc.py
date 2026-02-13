first_name = input("Enter your name: ").strip()
surname = input("Enter your surname: ").strip()

formatted_first = first_name.title()
formatted_surname = surname.title()

print(f"Welcome {formatted_first} {formatted_surname}!")
print(f"Your name has {len(formatted_first)} letters in first name.")
if formatted_first.isalpha():
    print("invalid string")
else:
    print(f"Welcome {formatted_first} {formatted_surname}!")
    print(f"Your name has {len(formatted_first)} letters in first name.")