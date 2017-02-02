def create_new_contact():
    name = input('enter name')
    try:
        add_new_contact_to_base(name)
        number = input('enter number')
        add_new_contact_to_base(name, number)
    except ValueError:
        while True:
            action_ = input('Contact already exist. Would you want to update contact? Yes/No')
            if action_ == 'Yes':
                number = input('enter new number')
                update_contact_in_base(name, number)
                break
            elif action_ == 'No':
                break
            else:
                print('Your input is incorrect. Please try again.')


def add_new_contact_to_base(name, number=None):
    if not list_of_contacts.get(name):
        list_of_contacts[name] = number
    else:
        if list_of_contacts[name]:
            raise ValueError
        else:
            list_of_contacts[name] = number


def delete_contact():
    name = input('enter name to delete')
    try:
        delete_contact_from_base(name)
    except KeyError:
        print('Contact is not exist. Please try again.')


def delete_contact_from_base(name):
    del list_of_contacts[name]


def update_contact():
    name = input('enter name')
    try:
        delete_contact_from_base(name)
        number = input('enter new number')
        add_new_contact_to_base(name, number)
    except KeyError:
        print('Contact is not exist. Please try again.')


def update_contact_in_base(name, new_number):
    if list_of_contacts.get(name):
        list_of_contacts[name] = new_number
    else:
        raise ValueError


def read_contact():
    name = input('enter name')
    try:
        number = get_contact_from_base(name)
        print(number)
    except KeyError:
        print('Contact is not exist. Please try again.')


def get_contact_from_base(name):
    number = list_of_contacts[name]
    return number

list_of_contacts = {}
actions = {'Create': create_new_contact,
           'Read': read_contact,
           'Update': update_contact,
           'Delete': delete_contact}


def main():
    while True:
        action = input('Enter what do you want? "Create, Read, Update, Delete, exit"')
        if action not in ('Create', 'Read', 'Update', 'Delete', 'exit'):
            print('Your input is incorrect. Please try again.')
        else:
            if action == 'exit':
                break
            print(action)
            actions[action]()
            print(list_of_contacts)

if __name__ == '__main__':
    main()
