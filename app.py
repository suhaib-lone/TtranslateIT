from googletrans import Translator, LANGUAGES
from flask  import Flask,request,render_template
app = Flask(__name__)

translator=Translator()


def translate_text(source_text, target_lang):
    source_lang=LANGUAGES.get((translator.detect(source_text)).lang)
    translation=translator.translate(source_text, target_lang)
    return translation,source_lang
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        source_text=request.form['src_text']
        destination_lang=request.form['dest_lang']
        translation,source_lang=translate_text(source_text, destination_lang)
        return render_template('index.html', source_lang=source_lang, translation=translation)
    return render_template('index.html', translation=None, source_lang=None)
if __name__ == "__main__":
    app.run(debug=True)

