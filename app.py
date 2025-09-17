import time
from functools import lru_cache
from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/')
def index() -> str:
    return render_template('index.html', time=None, n=100)

@app.post('/')
def index_post() -> str:
    n = request.form.get('n', 100)
    n = int(n)
    if n < 1 or n > 100:
        return render_template('index.html', time=None, n=n, error="Invalid input")
    start = time.perf_counter_ns()
    num = fib(n)
    end = time.perf_counter_ns()
    return render_template('index.html', num=num, time=end - start, n=n)

@app.get('/center')
def center() -> str:
    return render_template('center.html')

@lru_cache(maxsize=100)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()