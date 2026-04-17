try:
    note = input("Enter your note: ")

    with open("notes.txt", "w") as file:
        file.write(note)

    with open("notes.txt", "r") as file:
        print("\nFile Content:")
        print(file.read())

    new_note = input("\nEnter another note: ")

    with open("notes.txt", "a") as file:
        file.write("\n" + new_note)

    with open("notes.txt", "r") as file:
        print("\nUpdated File Content:")
        print(file.read())

except FileNotFoundError:
    print("Error: File not found!")