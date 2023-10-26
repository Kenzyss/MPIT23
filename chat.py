import string
import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


def lemmatize(text):
    words = nltk.word_tokenize(text.lower())
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words if word not in string.punctuation]
    result = lemmatized_words
    # print(result)
    return result


def response(answer):
    return lemmatize(answer)


def compare_word_lists(list1, list2, key):
    max_p = 0
    result = []
    set1 = set(list1)
    set2 = set(list2)

    common_words = set1.intersection(set2)

    if len(set1) == 0 or len(set2) == 0:
        return 0.0
    else:
        max_len = max(len(list1), len(list2))
        percentage = len(common_words) / max_len * 100
        if percentage > max_p:
            max_p = percentage

    # print(list2)
    # if len(result) > 0 and result is not None:
    return key


lang = "rus"  # 0 - ru; 1 - eng
if lang == "rus":
    dictionary = {
        'Question': 'Answer',
        "Нужно идти на кпп": 'Я приехал, что делать дальше?',
    }
else:
    dictionary = {
        'привет': 'Привет!',
    }

question = lemmatize(input("Введите ваш вопрос: "))
for i in dictionary.values():
    keys = list(dictionary.keys())
    index = list(dictionary.values()).index(i)
    key = keys[index]
    print(compare_word_lists(question, lemmatize(i), key))

# print(f"Процент совпадения: {result:.2f}%")


# print(text.get(1)[1][lang])


# return "I do not understand..."


# if __name__ == "__main__":
#     print("Let's chat! (type 'quit' to exit)")
#     while True:
#         # sentence = "do you use credit cards?"
#         sentence = input("You: ")
#         if sentence == "quit":
#             break
#
#         resp = get_response(sentence)
#         print(resp)
