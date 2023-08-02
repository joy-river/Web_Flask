import smtplib as sm
from email.mime.text import MIMEText

naver_username = "dlrkd1122"
naver_password = "WFTWLYKJUP7D"


def send_email(email_data):
    with sm.SMTP("smtp.naver.com", port=587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(naver_username, naver_password)
        msg = MIMEText(email_data["message"])
        msg["From"] = "dlrkd1122@naver.com"
        msg["Subject"] = f"Contact Email From {email_data['name']}"
        msg["Title"] = email_data["phone"]
        msg["To"] = "You"
        connection.sendmail("dlrkd1122@naver.com",
                            "dlrkd1122@gmail.com", msg.as_string())
