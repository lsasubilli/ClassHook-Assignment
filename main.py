import smtplib
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/emails", methods=["POST", "GET"])
def process_json():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":

        records = request.get_json()
        #initialize variables
        to_str = ""
        subject_str = ""
        body_str = ""
        to_list = []

        for r in records:
            # print(records[r])
            if r == "to":
                to_str = records[r]
            if r == "subject":
                subject_str = records[r]
            if r == "body":
                body_str = records[r]

        print ("Now trying to send an email")
        try:
            smtp_ssl = smtplib.SMTP_SSL(host="smtp.mail.yahoo.com", port=465)
        except Exception as e:
            #print ("Error with smtp ssl connection")'
            print ("ErrorType : {}, Error : {}".format(type(e).__name__, e))
            smtp_ssl = None

        resp_code, response = smtp_ssl.login(user="sasubillis@yahoo.com", password="---")

        frm = "sasubillis@yahoo.com"
        to_list.append(to_str)
        message = "Subject: {}\n\n{}".format(subject_str, body_str)


        response = smtp_ssl.sendmail(from_addr=frm, to_addrs=to_list, msg=message)

        return "Sent email as per payload"+response
    else:
        return "Content-Type not supported...!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
