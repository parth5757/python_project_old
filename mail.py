import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('parth@gmail.com', '123456789')
server.sendmail('parth@gmail.com',
                'parth@outlook.com',
                'hi parth from  india microsoft this is parth google')
