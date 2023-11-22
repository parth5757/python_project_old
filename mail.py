import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('psthakkar2@gmail.com', 'parth@it2157')
server.sendmail('psthakkar2@gmail.com',
                'psthakkar2@outlook.com',
                'hi parth from  india microsoft this is parth google')
