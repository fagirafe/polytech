# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, delimiter=','):
    part1 = set(group_1.split(delimiter))
    part2 = set(group_2.split(delimiter))
    value = sorted(part1 & part2)
    return value


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group)
print(result)
# TODO Провеьте работу функции с разделителем отличным от запятой
