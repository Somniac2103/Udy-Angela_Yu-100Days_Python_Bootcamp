import smtplib

my_email = "barrysalmon36@gmail.com"
my_password = "Nom12Las03!"
app_password = "zxxb nxnh xddr kitr"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_password)
    connection.sendmail(
        from_addr = my_email,
        to_addrs="brian.salmon@gmail.com", 
        msg="Subject:Sent from my python program\n\n"
    )

