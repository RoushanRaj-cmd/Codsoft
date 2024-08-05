class Person:
    def __init__(self, full_name, phone_number, email_address, home_address):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.home_address = home_address

    def __str__(self):
        return f"Name: {self.full_name}\nPhone: {self.phone_number}\nEmail: {self.email_address}\nAddress: {self.home_address}"

class PersonManager:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)
        print("Person added successfully.")

    def display_people(self):
        if not self.people:
            print("No people available.")
        else:
            for idx, person in enumerate(self.people, 1):
                print(f"\nPerson {idx}:\n{person}")

    def find_person(self, keyword):
        matching_people = [person for person in self.people if keyword in person.full_name or keyword in person.phone_number]
        if not matching_people:
            print("No people found.")
        else:
            for person in matching_people:
                print(person)

    def modify_person(self, name):
        for person in self.people:
            if person.full_name == name:
                person.phone_number = input("Enter new phone number: ")
                person.email_address = input("Enter new email: ")
                person.home_address = input("Enter new address: ")
                print("Person updated successfully.")
                return
        print("Person not found.")

    def remove_person(self, name):
        for person in self.people:
            if person.full_name == name:
                self.people.remove(person)
                print("Person removed successfully.")
                return
        print("Person not found.")

def run():
    manager = PersonManager()

    while True:
        print("\nPerson Management System")
        print("1. Add Person")
        print("2. Display People")
        print("3. Find Person")
        print("4. Modify Person")
        print("5. Remove Person")
        print("6. Exit")

        option = input("Enter your choice (1-6): ")

        if option == '1':
            full_name = input("Enter full name: ")
            phone_number = input("Enter phone number: ")
            email_address = input("Enter email: ")
            home_address = input("Enter address: ")
            person = Person(full_name, phone_number, email_address, home_address)
            manager.add_person(person)
        elif option == '2':
            manager.display_people()
        elif option == '3':
            keyword = input("Enter name or phone number to find: ")
            manager.find_person(keyword)
        elif option == '4':
            name = input("Enter the name of the person to modify: ")
            manager.modify_person(name)
        elif option == '5':
            name = input("Enter the name of the person to remove: ")
            manager.remove_person(name)
        elif option == '6':
            print("Exiting the Person Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    run()
