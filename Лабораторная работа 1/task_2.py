list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

count_of_players = len(list_players)
middle_of_list_players = count_of_players // 2
first_team = list_players[:middle_of_list_players]
second_team = list_players[middle_of_list_players:]

print(first_team)
print(second_team)
