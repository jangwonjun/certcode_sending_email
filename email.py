import smtplib
import string
import random
from email.mime.text import MIMEText


class Send_Email:

  def __init__(self,mail,index , contents):
    self.mail = mail
    self.index = index
    self.contents = contents

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(MY_ACCOUNT, MY_PASSWORD)

    msg = MIMEText(index)
    msg['Subject'] = contents

    smtp.sendmail(MY_ACCOUNT, mail, msg.as_string())

    smtp.quit()

def Cert_Code():
  string_pool = string.ascii_letters
  result = []
  for i in range(8):
    result.append(random.choice(string_pool)) 

  certification_code = ''.join(result)
  return(certification_code)



# (Mail Address, Certfication_Code, Mail_Main_Title)

test = ["teset@test.com","test@happy.com","activejang@activejang.co.kr"]

for i in range(3):
  Send_Email(test[i], Cert_Code()+str(" 인증번호를 다음과 같이 입력해주세요!"), "메일 인증번호 입니다!")
  print(f"{test[i]} 에게 성공적으로 메일을 전송하였습니다!")

