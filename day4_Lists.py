names = []

for i in range(3):
    name = input("Enter a name: ").strip().title()
    names.append(name)

print("\n Processed names:")

for name in names:
    print(f"Welcome {name}")