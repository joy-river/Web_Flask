from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)

# 파이썬 데코레이터 -> 어떤 함수에다가 특정한 기능을 일괄적으로 붙이고 싶을때 (전부 2초 지연같이)
# 말 그대로 데코가 가능한 장식용 함수.
# @ 기호는 자기 밑에 있는 함수를 데코해주겠다는 뜻.
@app.route('/') # "/" => 홈페이지로 갈 때. route는 특정 url에서 밑의 함수를 실행하게하는 데코레이터.
def Hello_World():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return "See you again!"

# __name__ -> 지금 어디서 어떤 모듈을 쓰는지 알려줌. __main__ 은 지금 현재 이 파일 내에서 코드가 실행중이란 뜻.
if __name__ == '__main__':
    app.run()
