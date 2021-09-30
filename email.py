import smtplib    
sender_mail = 'mohan.kv1136@gmail.com'    
receivers_mail = ['o161516@rgutkong.ac.in']    
message ="sample mail"    
try:    
   password = input('Enter the password');    
   smtpObj = smtplib.SMTP('o161516@rgutkong.ac.in',587)    
   smtpobj.login(sender_mail,password)    
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    
except Exception:    
   print("Error: unable to send email")