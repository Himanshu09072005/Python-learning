names = []

while True:
    name = input("Enter a name (or type 'done' to finish): ").strip()
    
    # Check if user wants to stop
    if name.lower() == "done":
        break
    
    # Validate input
    if name.replace(" ", "").isalpha():
        clean_name = " ".join(name.title().split())
        names.append(clean_name)
    else:
        print("Invalid input, accepts only letters and spaces.")

print("\nProcessed names:")

for name in names:
    print(f"Welcome {name}")
