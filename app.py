from flask import Flask, request, render_template
from env import EMAIL, PORT, SEND_PASSWORD
from static.email import Send_Email, Cert_Code

app = Flask(__name__, static_url_path='/static')

@app.route('/',methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        message_target = request.form['target'] #상대방
        message_title = request.form['title'] #제목
        message_context = request.form['msg'] #내용
        message_send_password = request.form['password'] #전송비밀번호
        if message_send_password == SEND_PASSWORD.PASSWORD :
            Send_Email(message_target, message_context, message_title)
            print("successfully sent email")
    return render_template('email.html')
            
if __name__ == '__main__':
    app.run('0.0.0.0', debug=False, port = PORT.PORT_NUM)