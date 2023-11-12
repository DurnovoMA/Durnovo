# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, rezdelitel = ","):
    str1 = str1.split(rezdelitel)
    str2 = str2.split(rezdelitel)
    obshie = list(set(str1).intersection(str2))
    obshie.sort()
    print(obshie)
    return obshie

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group,  participants_second_group, "|")
# TODO Провеьте работу функции с разделителем отличным от запятой
