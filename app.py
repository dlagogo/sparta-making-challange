from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 스파르타 강의 4-13 뼈대


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


#@app.route('/memo', methods=['GET'])
#def listing():
    #sample_receive = request.args.get('sample_give')
    #print(sample_receive)
    #return jsonify({'msg': 'GET 연결되었습니다!'})


## API 역할을 하는 부분
#@app.route('/memo', methods=['POST'])
#def saving():
 #   sample_receive = request.form['sample_give']
  #  print(sample_receive)
   # return jsonify({'msg': '등록되었습니다!'})

## 즐겨찾기,삭제하기

# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_vocas():
    voca = list(db.voca.find({}, {'_id': False}).sort('like',-1))
    return jsonify({'vocas': voca})
@app.route('/api/like', methods=['POST'])
def like_voca():
    voca_receive = request.form['voca_give']
    target_voca = db.voca.find_one({'voca': voca_receive})
    current_like = target_voca['like']
    new_like = current_like + 1
    db.voca.update_one({'voca': voca_receive}, {'$set': {'like': new_like}})
    return jsonify({'msg': '좋아요 완료!'})
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)