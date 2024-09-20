import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send an email
def send_email(sender_email, sender_password, recipient_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Create a secure SSL context
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

# Load email addresses from a CSV file
def load_email_addresses(file_path):
    df = pd.read_csv(file_path)
    return df['email'].tolist()  # Assumes the CSV has a column named 'email'

# Main function
def main():
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'  # Consider using an app password for security
    subject = "Exciting Offer Just for You!"
    body = "Hello! Check out our latest offers on our website."

    email_list = load_email_addresses('emails.csv')  # Update with your CSV file path

    for recipient_email in email_list:
        send_email(sender_email, sender_password, recipient_email, subject, body)

if __name__ == '__main__':
    main()
