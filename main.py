import datetime as dt
import random
import smtplib


date = dt.datetime.now()
weekday = date.weekday()

MY_EMAIL = "youremail@gmail.com"
PASSWORD = "your_password_app"


with open("quotes.txt", "r") as file:
    quotes = [line.strip() for line in file]

quote = random.choice(quotes)

if weekday == 4:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="email_to@gmail.com",
            msg=f"Subject:Your Friday Quote \n\n{quote}"
        )
