import string
import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

lang = "rus"  # 0 - ru; 1 - eng


def lemmatize(text):
    words = nltk.word_tokenize(text.lower())
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words if word not in string.punctuation]
    result = lemmatized_words
    # print(result)
    return result


def response(answer):
    return lemmatize(answer)


def compare_word_lists(list1, list2, key):
    list1 = lemmatize(list1)
    max_p = 0
    result = ""
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
            result = key

    return result


def get_dictionary(language):
    if language == "rus":
        dictionary = {
            'Question': 'Answer',
            "Нужно идти на кпп": 'Я приехал, что делать дальше?',
        }
    else:
        dictionary = {
            'привет': 'Привет!',
        }

    return dictionary


dictionary = get_dictionary(lang)


