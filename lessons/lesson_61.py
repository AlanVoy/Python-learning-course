def word_counter(text: str) :
    """Функция считает количество слов в сообщении и отправляет данные о словах другим функциям."""
    text = text.split()
    count = 0
    max_lenght_word = ""
    quantity_spec_letter = 0
    count_more_four = 0
    for word in text :
        max_lenght_word = lenght_word(word, max_lenght_word,)
        quantity_spec_letter = specific_letter(word, quantity_spec_letter)
        count_more_four = more_four(word, count_more_four)
        count += 1
    if count == 0 :
        max_lenght_word = "Нет слов"
    return count, quantity_spec_letter, count_more_four, max_lenght_word

def specific_letter(text: str, quantity: int) :
    """Функция-счётчик слов начинающихся с буквы "п"."""
    letter = "п"
    if text[0].casefold() == letter.casefold() :
        quantity += 1
    return quantity
def lenght_word(text: str, word: str) :
    """Функция ищет самое длинное слово в сообщении."""
    if len(text) > len(word) :
        word = text
    return word
def more_four(text: str, count: int) :
    """Функция считает слова длиной от 5 символов."""
    if len(text) > 4 :
        count += 1
    return count
    
message = input("Введите сообщение: ")
quantity_words_in_message, quantity_spec_letter_words, quantity_more_four_letter, longest_word = word_counter(message)
print("Всего слов:", quantity_words_in_message)
print("Слов длиной от 5 символов:", quantity_more_four_letter)
print("Самое длинное слово:", longest_word)
print("Слов на букву 'п':", quantity_spec_letter_words)