import smtplib,ssl  
from picamera import PiCamera  
from time import sleep  
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email.mime.text import MIMEText  
from email.utils import formatdate  
from email import encoders  

def take_pic():
    camera = PiCamera()  
      
    camera.start_preview()  
    sleep(2)  
    camera.capture('/home/pi/pi-face-recognition/image.jpg')     # image path set
    #sleep(1)  
    camera.stop_preview()
    camera.close()
def send_an_email():  
    toaddr = 'dantex2556@gmail.com'      # To id 
    HSSS = 'hsssmsgserver@gmail.com'          # your id
    subject = "INTRUDER ALERT"              # Subject
  
    msg = MIMEMultipart()  
    msg['Subject'] = subject  
    msg['From'] = HSSS  
    msg['To'] = toaddr  
    msg.preamble = "test "   
    #msg.attach(MIMEText(text))  
  
    part = MIMEBase('application', "octet-stream")  
    part.set_payload(open("image.jpg", "rb").read())  
    encoders.encode_base64(part)  
    part.add_header('Content-Disposition', 'attachment; filename="image.jpg"')   # File name and format name
    msg.attach(part)  
  
    try:  
       s = smtplib.SMTP('smtp.gmail.com', 587)  # Protocol
       s.ehlo()  
       s.starttls()  
       s.ehlo()  
       s.login(user = 'hsssmsgserver@gmail.com', password = 'cse101major')  # User id & password
       #s.send_message(msg)  
       s.sendmail(HSSS, toaddr, msg.as_string())  
       s.quit()  
    #except:  
    #   print ("Error: unable to send email")    
    except SMTPException as error:  
          print ("Error")                # Exception
  