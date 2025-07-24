# class to store contact info
class contact:
    def __init__(self, name, phone, email, address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

#class to manage list of contacts
class contactbook:
    def __init__(self):
        self.contacts=[]

#ADD CONTACTS
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"CONTACT '{contact.name}' ADDED SUCCESSFULLY")

#VIEW CONTACTS
    def view_contacts(self):
        if not self.contacts:
            print("NO CONTACTS FOUND")
        else:
            print("\nCONTACT LIST:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")

#SEARCH CONTACTS
    def search_contact(self, query):
        results=[]
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

#UPDATE CONTACTS
    def update_contact(self, index, new_contact):
        if 0 <= index <len(self.contacts):
            self.contacts[index] = new_contact
            print("CONTACT UPDATED SUCCESSFULLY")
        else:
            print("INVALID CONTACT NUMBER")

#DELETE CONTACTS
    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            deleted = self.contacts.pop(index)
            print(f"CONTACT '{deleted.name}' DELETED")
        else:
            print("INVALID CONTACT NUMBER")

# function to collect contact details from the user
def get_contact_details():
    name = input("ENTER NAME: ")
    phone = input("ENTER PHONE NUMBER: ")
    email = input("ENTER EMAIL: ")
    address = input("ENTER ADDRESS: ")
    return contact(name, phone, email, address)

# main function to provide user options
def main():
    contact_book = contactbook()

    while True:
        print("\n---CONTACT BOOK MENU---")
        print("1. ADD CONTACT")
        print("2. VIEW CONTACT")
        print("3. SEARCH CONTACT")
        print("4. UPDATE CONTACT")
        print("5. DELETE CONTACT")
        print("6. EXIT")

        choice = input("ENTER YOUR CHOICE (1-6): ")

        if choice == '1':
            contact = get_contact_details()
            contact_book.add_contact(contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            query = input("ENTER THE NAME OR PHONE TO SEARCH: ")
            results = contact_book.search_contact(query)
            if results:
                priint("\nSEARCH RESULTS:")
                for i, contact in enumerate(results, 1):
                    print(f"{i}. {contact.name} - {contact.phone}")
            else:
                print("NO MATCHING CONTACTS FOUND.")

        elif choice == '4':
            contact_book.view_contacts()
            try:
                index = int(input("ENTER CONTACT NO. TO UPDATE:")) - 1
                new_contact = get_contact_details()
                contact_book.update_contact(index, new_contact)
            except:
                print("INVALID INPUT. PLEASE ENTER A VALID CONTACT NUMBER.")

        elif choice == '5':
            contact_book.view_contacts()
            try:
                index = int(input("ENTER CONTACT NUMBER TO DELETE: ")) - 1
                contact_book.delete_contact(index)
            except:
                print("INVALID INPUT. PLESE ENTER A VALID NUMBER.")

        elif choice == '6':
            print("EXITING CONTACT BOOK. GOODBYE!")
            break
    
        else:
            print("INVALID CHOICE. PLESE SELECT A NUMBER FROM 1 TO 6.")
# RUN THE PROGRAM
if __name__ == "__main__":
    main()   
