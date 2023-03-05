from flask import Flask,render_template,request
from datetime import datetime, timedelta
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

app=Flask(__name__)




def create_body(name):
    current_date=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    expiry_date=current_date+timedelta(days=90)
    template=f"<p>Hello {name},</p><p>Thank You For registering with Anubhav's Laboratory. Your Membership will expire on {expiry_date}. We hope you have a pleasant journey with us.</p>Warmest Regards,<br><p>Anubhav Sanyal</p><p>CEO & Founder - Anubhav's Laboratory</p>"
    return template

def create_email(body,email):
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
    try:
        response=sg.send(email)
    except:
        status_code=401
        return status_code
    return response.status_code

@app.route("/",methods=["GET"])
def home_route():
    return render_template('home.html')

@app.route("/",methods=["POST"])
def post_user_info():
    customer_email=request.form.get("customerEmail")
    customer_name=request.form.get("customerName")
    print(customer_email)
    print(customer_name)
    body=create_body(customer_name)
    response=create_email(body,customer_email)
    print(response)
    return render_template("home.html")


if(__name__=="__main__"):
    app.run(port=4605,debug=True)
