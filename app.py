from flask import Flask,render_template,request
from datetime import datetime, timedelta
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

app=Flask(__name__)




def createBody(name):
    currentDate=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    expiryDate=currentDate+timedelta(days=90)
    template=f"<p>Hello {name},</p><p>Thank You For registering with Anubhav's Laboratory. Your Membership will expire on {expiryDate}. We hope you have a pleasant journey with us.</p>Warmest Regards,<br><p>Anubhav Sanyal</p><p>CEO & Founder - Anubhav's Laboratory</p>"
    return template

def createEmail(body,email):
    if((not body) or (not email) ):
        status_code=400
        return status_code

    sg=SendGridAPIClient("Use your own API Key Here")
    email=Mail(
        from_email="princebest3@rediffmail.com",
        to_emails=email,
        subject="Introductory Email from our CEO , specially curated for you!",
        html_content=body
    )
    response=sg.send(email)
    return response.status_code

@app.route("/",methods=["GET"])
def homeRoute():
    return render_template('home.html')

@app.route("/",methods=["POST"])
def postUserInfo():
    customerEmail=request.form.get("customerEmail")
    customerName=request.form.get("customerName")
    print(customerEmail)
    print(customerName)
    body=createBody(customerName)
    response=createEmail(body,customerEmail)
    print(response)
    return render_template("home.html")


if(__name__=="__main__"):
    app.run(port=4605,debug=True)