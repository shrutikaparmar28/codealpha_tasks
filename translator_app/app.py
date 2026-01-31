from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""

    if request.method == "POST":
        text = request.form["text"]
        source_lang = request.form["source"]
        target_lang = request.form["target"]

        translated_text = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
