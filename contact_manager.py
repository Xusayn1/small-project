import re
class Contact :
    def __init__(self, name, email, age, phone):
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone

contact = Contact("John", "John@gmail.com", 18,'998901234567')
contact2 = Contact('Charls',"charls@icloud.com",31,'998912345678')

base = [contact, contact2]


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    pattern = r'^998\d{9}$'
    return re.match(pattern, phone) is not None


def view_contact(c:list):
    count = 0
    for item in c:
        count += 1
        print(f'{count}.name: {item.name} email: {item.email} age: {item.age} phone: {item.phone}')

def add_contact():
    name = input('Enter your name: ')

    while True:
        email = input('Enter your email: ')
        if is_valid_email(email):
            break
        print(" Invalid email format, try again!")

    age = int(input('Enter your age: '))

    while True:
        phone = input('Enter your phone: ')
        if is_valid_phone(phone):
            break
        print('invalid phone format, try again!')
    new_contact = Contact(name, email, age, phone)
    base.append(new_contact)

def delete_contact(c:list):
    name = input('Enter the name: ')
    for item in c:
        if item.name == name:
            base.remove(item)
            print('Contact deleted successfully')
            return
    print('Contact not found')

def manager_contact():
    while True:
        print('**** Contact Manager ****')
        kod = input('1.add contact \n 2.view contact \n 3.delete contact \n 4.exit \n choose option:= ')
        if kod == '1':
            add_contact()
        elif kod == '2':
            view_contact(base)
        elif kod == '3':
            delete_contact(base)
        else:
            print('Exiting...')
            break

if __name__ == '__main__':
    manager_contact()