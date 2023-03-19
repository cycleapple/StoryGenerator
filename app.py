from flask import Flask, request, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

def generate_story(theme, language):
    if language == 'en':
        prompt = f"Write a short story about {theme}"
        model = 'text-davinci-002'
    elif language == 'zh':
        prompt = f"#zh-tw 用台灣小說的風格，寫一個關於{theme}的短故事 "
        model = 'text-davinci-002'
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    story = response.choices[0].text.strip()
    return story

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-story', methods=['POST'])
def generate_story_endpoint():
    theme = request.form['theme']
    language = request.form['language']
    story = generate_story(theme, language)
    return story

if __name__ == '__main__':
    app.run(debug=True)
