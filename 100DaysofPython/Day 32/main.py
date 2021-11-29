import smtplib
import datetime as dt
import random

MY_EMAIL = "gusi97.it@gmail.com"
PASSWORD = "Uzizero083dsadasdsadas"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password= PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL,
                            to_addrs= MY_EMAIL,
                            msg = f"Subject: Monday Motivation \n\n {quote}")


















# import smtplib
#
# my_email = "gusi97.it@gmail.com"
# password = "Uzizero0830"
#
# with smtplib.SMTP("smtp.gmail.com") as connection: #yahoo - smtp.mail.yahoo.com
#     connection.starttls()
#     connection.login(user = my_email, password = password)
#     connection.sendmail(
#         from_addr = my_email,
#         to_addrs="gusi08.it@yahoo.com",
#         msg = "Subject:Hello\n\n This is the body of my email"
#     )
#
#
# import datetime as dt
#
# now = dt.datetime.now()
#
# date_of_birth = dt.datetime(year = 1997, month = 8, day = 30, hour=4)
# print(date_of_birth)

