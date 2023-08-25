from flask import Flask, request, render_template
from env import EMAIL, PORT
from static.email import Send_Email, Cert_Code

app = Flask(__name__, static_url_path='/static')
test = ["admin@activejang.com","won2005won@naver.com","admin@activejang.kro.kr"]

@app.route('/', methods=['GET','POST'])
def send(): 
    try : 
        for i in range(3):
            Send_Email(test[i], Cert_Code()+str(" 인증번호를 다음과 같이 입력해주세요!"), "메일 인증번호 입니다!")
            print(f"{test[i]} 에게 성공적으로 메일을 전송하였습니다!")
            
    except Exception as e:
        print(e)
        return render_template('index.html')
        
if __name__ == '__main__':
    app.run('0.0.0.0', debug=False, port = PORT.PORT_NUM)