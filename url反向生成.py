from flask import Flask, request

app = Flask(__name__)

def decorator(fn):
    def inner(*args, **kwargs):
        print('来了')
        res = fn(*args, **kwargs)
        print('走了')
        return res

    return inner



@app.route('/')
@decorator
def index():
    print(request.endpoint)
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)
