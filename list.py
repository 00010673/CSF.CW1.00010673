# Lists are the set of several and various other data types. They can contain all other data types.
# Lists can be edited and other items can be added after being declared.
team_names = [["Barcelona", "Real Madrid"], "Juventus", "Bayern Munich", "PSG"]
team_countries = ["Spanish", "Italian", "German", "French"]

team_names.append(["Arsenal", "Liverpool"])
team_countries.append("France")

# Two related lists can be zipped so relative items are merged together.
teams = zip(team_names, team_countries)

for name, country in teams:
    if isinstance(name, str):  # checks whether string to identify list data type later
        print(name, "is a", country, "soccer team.")
    else:
        print(name[0], "and", name[1], "are", country, "soccer teams.")

# List items can be enumerated as well
for number, team in enumerate(team_names):
    if isinstance(team, str):  # checks whether string to identify list data type later
        print(str(number) +")", team)
    else:
        print(str(number) +")", team[0], "and", team[1])
    