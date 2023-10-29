def find_common_participants(first_group, second_group, separator=','):
    first_set = set(first_group.split(separator))
    second_set = set(second_group.split(separator))
    common_list = list(first_set.intersection(second_set))
    common_list.sort()
    return common_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))

