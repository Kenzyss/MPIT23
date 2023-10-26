from flask import Flask, render_template, request, jsonify

from chat import res, get_dictionary, lemmatize, max_perc
app = Flask(__name__)
lang = "rus"


@app.get("/")
def index_get():
    return render_template("base.html")

dictionary = get_dictionary(lang)


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    best_answer = None
    max_percentage = 0
    response = ""
    for key, value in dictionary.items():
        percent = max_perc(text, lemmatize(value))
        if percent > max_percentage:
            max_percentage = percent
            best_answer = value
            keys = list(dictionary.keys())
            index = list(dictionary.values()).index(best_answer)
            key = keys[index]

            # response = res(text, lemmatize(value), key
            message = {"answer": key}
        return message
        # response = res(text, lemmatize(i), percent, key)
        # message = {"answer": response}
    # return message


app.run(debug=True)
