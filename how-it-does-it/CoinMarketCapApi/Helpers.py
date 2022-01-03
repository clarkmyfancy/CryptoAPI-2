def create_comma_seperated_string_from_list_of_strings(list):
    cryptos_comma_seperated_string = ""
    for i, x in enumerate(list):
        if i == len(list) - 1:
            cryptos_comma_seperated_string += x
        else:
            cryptos_comma_seperated_string += (x + ",")
    return cryptos_comma_seperated_string