def famous_births(figures_dict):
    sorted_figures = sorted(figures_dict.values(), key=lambda x: x["date_of_birth"])
    for figure in sorted_figures:
        name = figure["name"]
        birth_date = figure["date_of_birth"]
        print(f"{name} is a great scientist born in {birth_date}.")

woman_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(woman_scientists)