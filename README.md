# ClassHook
ClassHook Coding Assignment

Purpose/Function:
This program reads JSON Payload and sends an email with given subject and body.

How and what did I use to deploy this?
For this program, I used pythonanywhere.com to deploy this application. 

What frameworks I used?
Flask

How does this program work?
You can copy this link:http://sasubillis.pythonanywhere.com/emails and paste it in the Postman.

Use the following JSON Payload:
{
    "to": "someemail@someexample.com",
    "subject": "whats up",
    "body": "hi!"
}

Make sure to use the POST Method. It should look something similar to this: 

![Screen Shot 2022-09-03 at 3 27 34 PM](https://user-images.githubusercontent.com/68266855/188289439-b616a983-ebcd-4236-b904-566850544954.png)

Once you hit send, it should say this in the console: "Sent email as per payload"


Libraries, other things I used throughout this assignment:
smtplib - built in with python and is the library used for sending mails using SMTP.
Flask - Flask is a Python Web Framework library I used to make this web application possible. 
request - request is another library and a simple API I used to make HTTP requests possible in Python. 

HTTP Methods I used throughout this assignment:
GET - less secure way but used a lot
POST - secure way but used less in the real world

SMTP server I used:
smtp.mail.yahoo.com




--Key terms--:
SMTP - Simple Transfer Mail Protocol, used by mail servers to send, recieve mail between outgoing senders and recievers

