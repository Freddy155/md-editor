from flask import Flask, render_template, request
import markdown2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    markdown_content = request.form['markdown']
    html = markdown2.markdown(markdown_content)
    return html

if __name__ == '__main__':
    app.run(debug=True)
