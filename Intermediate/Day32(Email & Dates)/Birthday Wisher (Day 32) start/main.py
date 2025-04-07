import smtplib

my_email = "barrysalmon36@gmail.com"
my_password = "Nom12Las03!"
app_password = "zxxb nxnh xddr kitr"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=app_password)
connection.sendmail(from_addr = my_email,
                    to_addrs="bianca.salmon@gmail.com", 
                    msg="Subject:Hello\n\n imagine a middle finger")
connection.close()

