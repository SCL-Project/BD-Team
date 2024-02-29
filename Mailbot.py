import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def send_email(subject, message, to_email, smtp_server, smtp_port, smtp_username, smtp_password, image_path):
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the message to the MIME and also encode it with utf-8 to display german "Umlaute".
    msg.attach(MIMEText(message, 'plain', 'utf-8'))

    with open('Event-Flyer.jpg', 'rb') as img_file:
        img_data = img_file.read()
        image = MIMEImage(img_data, name='Event-Flyer.jpg')
        msg.attach(image)



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
    with open('email_addresses.txt', 'r', encoding='utf-8') as file:
        email_addresses = [line.split(",") for line in file]

    #deletes all the line breaks at the end of the file
    while email_addresses and email_addresses[-1] == ['\n']:
        email_addresses.pop()

    #strip the mail addresses and the names
    for i in range(len(email_addresses)):
        for j in range(len(email_addresses[0])):
            email_addresses[i][j] = email_addresses[i][j].strip()

    # This part eliminates duplicates. If a person registers twice with the same Mail the mail will only be sent once. 
    mail_addresses = set()
    result = []

    for person in email_addresses:
        mail = person[0]
        if mail not in mail_addresses:
            result.append(person)
            mail_addresses.add(mail)

    email_addresses = result

    
    #Default greeting if the name of the person is unknown
    default_greeting = "Dear Blockchain-Enthusiast,"

    #Image path
    image_path = 'Event-Flyer.jpg'  # Path to your image file

    
    # Send emails to each address in the list
    for person in email_addresses:
        if person[1] == "-":
            greeting = default_greeting
        else: 
            greeting = f"Dear {person[1]},"

        finalMessage = f"{greeting}\n\n{message}"

        send_email(subject, finalMessage, person[0], smtp_server, smtp_port, smtp_username, smtp_password, image_path)

        print(greeting)

    print("Emails sent successfully.")
