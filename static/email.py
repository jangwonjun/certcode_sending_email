import smtplib
import string
import random
from email.mime.text import MIMEText
from env import EMAIL


class Send_Email:

  def __init__(self,mail,index , contents):
    self.mail = mail
    self.index = index
    self.contents = contents

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL.MY_ACCOUNT, EMAIL.MY_PASSWORD)

    msg = MIMEText(index)
    msg['Subject'] = contents

    smtp.sendmail(EMAIL.MY_ACCOUNT, mail, msg.as_string())

    smtp.quit()

def Cert_Code():
  string_pool = string.ascii_letters
  result = []
  for i in range(8):
    result.append(random.choice(string_pool)) 

  certification_code = ''.join(result)
  return(certification_code)

