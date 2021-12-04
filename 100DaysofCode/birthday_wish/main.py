import pandas as pd
import datetime as dt
import smtplib
import random

MY_EMAIL = "gusi97.it@gmail.com"
PASSWORD = "Uzizero0830199719191"

month = dt.datetime.now().month
day = dt.datetime.now().day

today = (month, day)

#Read CSV file using panda
data = pd.read_csv("birthday.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password= PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL,
                            to_addrs= birthday_person["email"],
                            msg = f"Subject: Happy Birthday! \n\n {content}")






