def find_the_redheads(family_dict):
    red_haired_name = filter(lambda name: family_dict[name] == "red", family_dict.keys())
    return list(red_haired_name)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))