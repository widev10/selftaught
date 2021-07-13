# mencari input yang memiliki duplikasi
# dengan menggunakan set()

def return_duplicate(a_list):
    duplikas = []
    a_set = set()
    for item in a_list:
        p_one = len(a_set)
        a_set.add(item)
        p_two = len(a_set)
        if p_one == p_two:
            duplikas.append(item)

    return duplikas

a_list = ['Rudi', 'Irawan', 'Suci', 'Suci', 'Irma']
duplikas = return_duplicate(a_list)
print(duplikas)