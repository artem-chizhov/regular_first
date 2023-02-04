
from itertools import chain
import re


def normalize_separators(contacts):
    for element in contacts[1:]:
        data = ' '.join(element[:3])
        new_data = data.split()
        i = 0
        while i < len(new_data):
            element[i] = new_data[i]
            i += 1
    return contacts


def remote_double_string(contacts):
    no_double_list = []
    for data in contacts:
        if data[0] and data[1] not in list(chain(*no_double_list)):
            no_double_list.append(data)
        else:
            for id, element in enumerate(no_double_list):
                if element[0] == data[0] and element[1] == data[1]:
                    i = 0
                    for el_ in element:
                        if el_ == '':
                            element[i] = data[i]
                        i += 1
                no_double_list[id] = element
    return no_double_list


def normalize_phones(contacts):
    new_contacts = []
    for element in contacts[1:]:
        new_contacts.append(element[5])
    for id, contact in enumerate(new_contacts):
        pattern = r"((8|\+7))[-\s*]?[-\s*]?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})" \
                r"[-\s]?(\d{2})\s*\(?(\w+\.)?\s*(\d+)?\)?"
        new_contact = re.sub(pattern, r"+7(\3)\4-\5-\6 \7 \8", contact)
        new_contacts[id] = new_contact.strip(' ')
    i = 0
    for element in contacts[1:]:
        element[5] = new_contacts[i]
        i += 1
    return contacts



