name = input("Enter your name: ").strip().title()

# load existing names first
with open("names.txt", "r") as file:
    names = [n.strip() for n in file.readlines()]

# check duplicate
if name in names:
    print("Name already exists.")
else:
    with open("names.txt", "a") as file:
        file.write(name + "\n")
    names.append(name)
    print("Name added.")

print("Names list:", names)
