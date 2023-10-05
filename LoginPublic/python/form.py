from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")

    # Send the email
    sender_email = "sender@example.com"
    password = "your_password"
    recipient_email = "recipient@example.com"
    message = f"Subject: New form submission\n\nName: {name}\nEmail: {email}"
    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=message
        )

    return "Thank you for submitting the form!"

if __name__ == "__main__":
    app.run(debug=True)
