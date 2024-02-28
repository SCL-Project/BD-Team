import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the message to the MIME and also encode it with utf-8 to display german "Umlaute".
    msg.attach(MIMEText(message, 'plain', 'utf-8'))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, to_email, msg.as_string())

if __name__ == "__main__":
    # Set your email credentials and SMTP server details
    smtp_server = 'smtp.strato.de'
    smtp_port = 587  # Change the port accordingly
    smtp_username = 'student-project@blockchainpresence.net'
    smtp_password = 'hdlbcDSNHCLNDskmcflOUE1'

    # Email content, utf-8 encoding to also send german "Umlaute"
    with open('email_text.txt', 'r', encoding='utf-8') as file:
        message = file.read()
    
    subject = 'Blockchain Event'


    # Read the list of email addresses from a file
    with open('email_addresses.txt', 'r') as file:
        email_addresses = [line.split(",") for line in file]


    #strip the mail addresses and the names
    for i in range(len(email_addresses)):
        for j in range(len(email_addresses[0])):
            email_addresses[i][j] = email_addresses[i][j].strip()


    default_greeting = "Dear Blockchain-Enthusiast,"

    
    # Send emails to each address in the list
    for person in email_addresses:
        if person[1] == "-":
            greeting = default_greeting
        else: 
            greeting = f"Dear {person[1]},"

        message = f"{greeting}\n\n{message}"

        send_email(subject, message, person[0], smtp_server, smtp_port, smtp_username, smtp_password)
    print("Emails sent successfully.")
        
