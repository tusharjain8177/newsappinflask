from flask import Flask, render_template
import requests



app=Flask(__name__)

@app.route("/")
def index():
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=6df7f92b2b014ce0ad722ed3b760c806"
    r=requests.get(url).json()

    cases={
        'articles' : r['articles']
    }
    return render_template('index.html', case=cases)


if __name__ == "__main__":
    app.run(debug=True)