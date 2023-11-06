from flask import Flask, render_template, request
from flask_mail import Message, Mail
from chat import get_dictionary, lemmatize, percent
import time
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.rambler.ru'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mpit23project@rambler.ru'  # адрес электронной почты
app.config['MAIL_PASSWORD'] = 'dFgHjK123'  # \ пароль

mail = Mail(app)

with app.app_context():
    recipient = "mpit23project@rambler.ru"
    subject = "hello"
    body = "Hello"
    lang = "rus"
    msg = Message(subject=subject,
                  recipients=["mpit23project@rambler.ru"], )
    msg.body = body
    # mail.send(msg)

dictionary = get_dictionary(lang)


@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    best_answer = None
    max_percentage = 0
    for key, value in dictionary.items():
        perc = percent(text, value)

        if perc > max_percentage:
            max_percentage = perc
            best_answer = value

    if best_answer:
        keys = list(dictionary.keys())
        index = list(dictionary.values()).index(best_answer)
        key = keys[index]
        message = {"answer": key}

        return message
    else:
        message = {
            "answer": "На данный момент я не могу ответить на данный вопрос, но я его отправил на нашу оффициальную "
                      "почту."}
        # mail.send(message)

        return message


app.run(debug=True)
