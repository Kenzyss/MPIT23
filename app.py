from flask import Flask, render_template, request, jsonify

from chat import compare_word_lists, get_dictionary, lemmatize
app = Flask(__name__)
lang = "rus"


@app.get("/")
def index_get():
    return render_template("base.html")

dictionary = get_dictionary(lang)


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    for i in dictionary.values():
        keys = list(dictionary.keys())
        index = list(dictionary.values()).index(i)
        key = keys[index]
        response = compare_word_lists(text, lemmatize(i), key)
        message = {"answer": response}
    return message


app.run(debug=True)
