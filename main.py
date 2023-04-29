from flask import Flask, request, render_template
from googletrans import Translator, LANGCODES

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    html = render_template('base.html', langs=LANGCODES)
    if request.method == 'POST':
        translator = Translator()
        html = render_template('base.html', langs=LANGCODES, lang=request.form.get('lang'), text=request.form.get('text1'), translate=translator.translate(request.form.get('text1'), dest=request.form.get('lang')).text)
    return html


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')