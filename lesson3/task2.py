def print_data(name = '', last_name = '', birth_year = '', city = '', email = '', phone = ''):
    print_list = []

    if name:
        print_list.append('Name: ' + name)

    if last_name:
        print_list.append('Last name: ' + last_name)

    if birth_year:
        print_list.append('Birth: ' + birth_year)

    if city:
        print_list.append('City: ' + city)

    if email:
        print_list.append('Email: ' + email)

    if phone:
        print_list.append('Phone: ' + phone)

    print(', '.join(print_list))


print_data(last_name = 'Golotiuk', name = 'Denys', city = 'Kyiv')
