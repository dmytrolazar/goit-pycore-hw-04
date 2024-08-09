def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return "Contact already exists."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact doesn't exist."

def show_contact(args, contacts):
    try:
        name = args[0]
        return f"{contacts[name]}"
    except KeyError:
        return "Contact doesn't exist."

def show_all_contacts(contacts):
    result = ''
    for name, phone in contacts.items():
        result += f"{name}: {phone}\r\n"
    return f"{result.strip()}" if result != '' else "Your contact list is empty."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"] and len(args) == 0:
            print("Good bye!")
            break
        elif command == "hello" and len(args) == 0:
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            print(add_contact(args, contacts))
        elif command == "change" and len(args) == 2:
            print(change_contact(args, contacts))
        elif command == "phone" and len(args) == 1:
            print(show_contact(args, contacts))
        elif command == "all" and len(args) == 0:
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()