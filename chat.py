import string
from pymystem3 import Mystem

# import time
# start_time = time.time()
# end_time = time.time()
# elapsed_time = end_time - start_time
# print('Elapsed time: ', elapsed_time)

lang = "rus"  # 0 - ru; 1 - eng
lemmatizer = Mystem()

lemmatize_dictionary = []
answers_list = []


def get_dictionary(language):
    if language == "rus":
        dictionary = {
            "Организовывать туристическую стоянку на Куршской косе запрещено! В дневное время можно ставить палатку "
            "или параван на берегу моря для защиты от солнца и ветра. Ставить палатку для ночлега можно только в "
            "специально организованных для этого местах: на территории турбаз, туркемпингов и гостевых домов, "
            "на пикниковом месте возле озера Чайка (32-й км).": 'Где на Куршской косе можно разместиться с палаткой?',
            "Национальный парк открыт для посещения 24/7 – круглосуточно и круглогодично. Визит-центр, расположенный "
            "на 14 км косы, открыт с 9 до 17 часов: с мая по сентябрь ежедневно, с октября по апрель – со среды по "
            "воскресенье. Полевой стационар кольцевания птиц открыт для посещения с апреля по октябрь с 10 до 17 "
            "часов.": 'В какие дни и в какое время национальный парк «Куршская коса» открыт для посещения?',
            "Для осмотра основных достопримечательностей на Куршской косе требуется транспорт. Можно перемещаться на автомобиле, туристическом или рейсовом автобусе. Есть парковки. Экскурсию в составе туристической группы нужно заказывать заранее в любой из калининградских турфирм, рейсовый автобус № 210 отправляется от вокзала в Зеленоградске, в летний сезон из Калининграда на косу ходит автобус № 593": "Как попасть на Куршскую косу? Мы приехали на КПП/в Зеленоградск – куда идти дальше?",
            "Чтобы посетить национальный парк с экскурсией, нужно заранее записаться в группу в любой из калининградских турфирм или заказать индивидуальную экскурсию на автомобиле/микроавтобусе с выездом из Калининграда или курортных городов области. Экскурсию по залам Визит-центра и тематические занятия для детских групп можно заказать, позвонив в отдел экопросвещения 8 4012 310028.": "Как попасть на экскурсию на Куршскую косу?",
            "Да, каждый въезд на территорию национального парка необходимо оплачивать и покупать входной билет.": "Нужно ли каждый раз покупать входной билет при въезде на территорию национального парка?",
            "Не нужно, билет действует трое суток при условии непрерывного пребывания на территории национального парка. Билет необходимо сохранять до момента выезда с Куршской косы.": "Если приехать вечером и разместиться на Куршской косе на ночлег, нужно ли на следующий день снова покупать входной билет в парк?",
            "Пассажиры рейсовых автобусов могут купить входной билет только онлайн – на сайте национального парка для перехода на сайт онлайн-оплаты нужно нажать «оплатить посещение». Для посещения экологических троп, маршрутов и других объектов национального парка это нужно сделать обязательно. Если пассажир едет на Куршскую косу с иными целями, например, в какой-то из поселков, покупать входной билет, в летний сезон из Калининграда на косу ходит автобус № 593.": "Как покупать входные билеты посетителям, въезжающим на рейсовых автобусах, и в каких случаях им можно не покупать билеты?",
        }
    else:
        dictionary = {
        }

    return dictionary


dictionary = get_dictionary(lang)


def lemmatize(text):
    lemmatized_words = lemmatizer.lemmatize(text)
    for word in lemmatized_words:
        if word in string.punctuation or word in ",     ":
            lemmatized_words.remove(word)
    return lemmatized_words


def start():
    for key, value in dictionary.items():
        lemmatize_dictionary.append(lemmatize(value))
        answers_list.append(value)


def get_answer(list1):
    best_answer = None
    max_p = 0

    list1 = lemmatize(list1)
    set1 = set(list1)
    for value in lemmatize_dictionary:
        set2 = set(value)
        common_words = set1.intersection(set2)

        # if len(set1) == 0 or len(set2) == 0:
        #     return 0.0
        # else:
        max_len = max(len(list1), len(value))
        percentage = len(common_words) / max_len * 100

        if percentage > max_p and percentage >= 13:
            max_p = percentage
            best_answer = answers_list[lemmatize_dictionary.index(value)]
    if best_answer is None:
        msg = "На данный момент я не могу ответить на данный вопрос, но я его отправил на нашу официальную почту"
    else:
        keys = list(dictionary.keys())
        index = list(dictionary.values()).index(best_answer)
        msg = keys[index]

    return msg
