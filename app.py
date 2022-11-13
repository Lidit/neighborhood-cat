# from crypt import methods
from ast import arg, operator
from http import client
from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
import operator

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.cat


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/servay', methods=['POST', 'GET'])
def servay():
    return render_template('servay.html')


@app.route('/result', methods=['POST', 'GET'])
def showResult():
    # # data = request.json()
    # if request.method == "POST":
    #     y_score = request.form.get('y')
    #     h_score = request.form.get('h')
    #     b_score = request.form.get('b')
    #     c_score = request.form.get('c')
    #     d_score = request.form.get('d')
    #     print("y값:", y_score)
    #     print("h값:", h_score)
    #     print("b값:", b_score)
    #     print("c값:", c_score)
    #     print("d값:", d_score)
    #     return redirect(url_for('Result', y=y_score, h=h_score, b=b_score, c=c_score, d=d_score))
    # else:
    y = request.args.get('y')
    h = request.args.get('h')
    b = request.args.get('b')
    c = request.args.get('c')
    d = request.args.get('d')

    y = int(y) / 30 * 100
    h = int(h) / 30 * 100
    b = int(b) / 30 * 100
    c = int(c) / 30 * 100
    d = int(d) / 30 * 100

    score_dict = {'h': h, 'b': b, 'c': c, 'd': d}
    d1 = dict(sorted(score_dict.items(), key=lambda x: x[1], reverse=True))
    print(d1)
    print(d1.keys())
    code = ""
    for i in d1.keys():
        code += str(i)

    print(code)

    return render_template('result.html', y=y, h=h, b=b, c=c, d=d, code=code)


# @app.route('/result/')
# def Result():
    # y, h, b, c, d
    # y = request.args.get('y')
    # h = request.args.get('h')
    # b = request.args.get('b')
    # c = request.args.get('c')
    # d = request.args.get('d')

    # y = y / 30 * 100
    # h = h / 30 * 100
    # b = b / 30 * 100
    # c = c / 30 * 100
    # d = d / 30 * 100

    # return render_template('result.html', y=y, h=h, b=b, c=c, d=d)


@app.route('/submit', methods=['POST'])
def submit():
    score_receive = request.form['score_give']  # 클라이언트로부터 점수를 받는 부분
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
