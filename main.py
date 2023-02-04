import normalization_phone_book as ph_b
import csv

if __name__ == '__main__':


  with open("phonebook_raw.csv", encoding='utf-8', newline='') as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)


  new_contacts_list = ph_b.normalize_phones(ph_b.remote_double_string(ph_b.normalize_separators(contacts_list)))


  with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(new_contacts_list)