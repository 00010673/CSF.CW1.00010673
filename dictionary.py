# Dictionaries contain more specified data collection.
# Instead of indexes, values are specified with keys.
# Each value can be edited, another key with a value can be added.

country_names = {
    "uz": "Uzbekistan",
    "us": "United States of America",
    "ru": "Russian Federation",
    "it": "Italy"
}

country_languages = {
    "uz": "uzbek",
    "us": "english",
    "ru": "russian",
    "it": "italian"
}

print("People in", country_names["ru"], "talk in", country_languages["ru"] + ".\n")

# We can automate the whole process and print sentences for all countries by looping.
# But looping two dictionaries is not possible. We should zip them.
# Corresponding keys and values cannot be zipped directly. In order to do so, we can use items method.

countries = zip(country_names.items(), country_languages.items())

for (k1, country), (k2, language) in countries:
    print("People in", country, "talk in", language + ".")
