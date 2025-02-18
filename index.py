from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

def generate_story_with_llama(girl_name, boy_name, romance_level):
    prompt = f"Create a {romance_level} romantic story where the main characters are {girl_name} and {boy_name}. The story should focus on their intense attraction, chemistry, and growing desire. It should include moments of deep connection, longing gazes, and the electric tension between them during their first meeting."
    response = ollama.chat(model="llama3.2:1b", messages=[{"role": "user", "content": prompt}])
    story = response.get('message', {}).get('content', 'No content available')
    return story

@app.route('/', methods=['GET', 'POST'])
def index():
    story = None
    if request.method == 'POST':
        girl_name = request.form['girl_name']
        boy_name = request.form['boy_name']
        romance_level = request.form['romance_level']
        story = generate_story_with_llama(girl_name, boy_name, romance_level)
    return render_template('index.html', story=story)

if __name__ == '__main__':
    app.run(debug=True)
