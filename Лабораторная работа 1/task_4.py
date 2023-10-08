users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

visits_dictionary = {"Общее количество" : 0, "Уникальные посещения" : 0}

visits_dictionary["Общее количество"] = len(users)
visits_dictionary["Уникальные посещения"] = len(set(users))

print(visits_dictionary)
