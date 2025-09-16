from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()