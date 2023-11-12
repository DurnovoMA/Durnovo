# TODO  Напишите функцию count_letters
def count_letters(text):
    text_lower = text.lower()
    dict_symbol = {}
    for i in text_lower:
        if i.isalpha():
            if i in dict_symbol:
                dict_symbol[i] += 1
            else:
                dict_symbol[i] = 1
    return dict_symbol
# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_symbol):
    dict_frequency = {}
    sum_symbol = 0
    for symbol in dict_symbol.values():
        sum_symbol += symbol
    for symbol, value in dict_symbol.items():
        symbol_frequency = value / sum_symbol
        dict_frequency[symbol] = symbol_frequency
    return dict_frequency
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


# TODO Распечатайте в столбик букву и её частоту в тексте
dict_count = count_letters(main_str)
for key, value in calculate_frequency(dict_count).items():
    print(f"{key}: {value:.2f}")