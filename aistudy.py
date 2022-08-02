from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'


def home():
    return "Home"

#路由的第二种方式，第一个参数是url路径，view——func参数对应的是视图函数
#app.add_url?rule('/home',view_func=home)

#完整写法
app.add_url_rule('/home',view_func=home)


if __name__ == '__main__':
    app.run(debug = True)
 
#