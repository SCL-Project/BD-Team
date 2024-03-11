<div align="justify">


# MailBot


## Motivation 

The BD/CRM Team, tasked with organizing guest speaker events, noticed a concerning trend: many emails sent to past event attendees to inform them about upcoming events were ending up in spam folders. Furthermore, we encountered difficulty in sending personalized bulk emails to our attendees, hindering the efficient distribution of information or updates to multiple recipients simultaneously. Recognizing the importance of addressing this issue, Ioannis Dougas, a member of the BD Team responsible for external events, took proactive steps to investigate potential solutions. Through thorough research, Ioannis discovered that creating a MailBot, capable of sending emails in limited quantities while being able to customize the greeting based on optional recipient names, could potentially resolve our deliverability challenges (see Background Research). Collaborating with Samuel Clauss, another member of the BD Team, they joined forces to develop a MailBot tailored to SCLs needs, with the primary goal of ensuring our emails reach recipients' inboxes reliably.  

## Background Research 

_What is a spam folder?_ 

The spam folder serves as storage space within your email account designated for unwanted messages or those deemed suspicious by email service providers (ESPs), consequently failing to land in your inbox. This folder is alternatively referred to as the "Bulk Folder" or "Junk Folder." Designed to streamline user experience, these filtering mechanisms aid users decrease the number of unnecessary and promotional emails. 

_How does this system operate?_  

When an email is dispatched, ESPs examine both the sender's email address reputation and the message content. Should any elements raise suspicion, ESPs automatically block the email from reaching the recipient's inbox. Additionally, recipients possess the ability to flag incoming emails as spam, further informing the ESPs' filtering algorithms. 
Sending emails improperly can have detrimental effects, potentially tarnishing the senders reputation and leading to placement in spam folders or even blockage by email providers. Adhering to email sending best practices is crucial for maintaining deliverability and ensuring messages reach the intended audience's inbox.  

_Several strategies can help prevent emails from being flagged and ending up in the spam folder:_

1. Manage Email Volume:  

It's essential to send a reasonable volume of emails within a specific timeframe. Exceeding the sending limits set by email providers can trigger spam filters. Aim to keep your sending volume between 50 and 200 emails per sender per day. If you need to send more, consider utilizing multiple sending addresses to distribute the load. 

2. Maintain a Balanced Sent-to-Received Ratio: 

Striking a good balance between emails sent and those received signals to email providers that your messages are relevant and authentic. Monitor your sent-to-received ratio after sending email campaigns and aim for a 4:1 ratio— for every four emails sent, aim to receive at least one reply. Additionally, craft email sign-offs that encourage engagement and prompt responses from your audience. 

3. Distribute Sending Speed: 

Rather than sending all your emails simultaneously, it's advisable to pace your sending speed throughout the day. This approach minimizes the risk of triggering spam filters and enhances the likelihood of your emails reaching recipients at opportune times. By spreading out the sending schedule, you optimize the chances of engagement and response from your audience. 

## Brief Code Description 

This Python script, known as the MailBot, simplifies the bulk sending of personalized emails via SMTP while mitigating the chance of ending in spam folders. It defines a function, `send_email`, which constructs and dispatches emails using provided subject, message, recipient email address, and SMTP server details. The script's main execution reads the SMTP configuration and email content from files, iterates through a list of recipients extracted from another file (in this case would be from the Eventbrite Attendees List), customizes the greeting based on optional recipient names, and sends individualized emails to each recipient. The MailBot efficiently avoids sending duplicate emails by intelligently skipping recipients listed multiple times, thereby minimizing redundant mailings. Additionally, it is programmed to seamlessly include image attachments along with the composed message, enhancing its versatility for diverse communication needs. By automating the email sending process, the script streamlines communication tasks, enabling efficient distribution of information or updates to multiple recipients simultaneously. 

## Outlook 

In response to the challenge of emails consistently ending up in spam folders, the BD/CRM Team developed a specialized MailBot. Led by Ioannis Dougas and assisted by Samuel Clauss, the team utilized insights from research to ensure reliable inbox delivery. Through strategic implementation of email volume management and distributing sending speed, the team mitigated the risk of triggering spam filters. The MailBot represents a significant advancement in SCL's communication strategy, ensuring important messages reach recipients effectively and consistently. In conclusion, the development of the MailBot demonstrates the team's commitment to innovation and proactive problem-solving.  

## How to Use the Mailbot

1. Clone the Repo and open the Mailbot folder in your favourite Code environment.
2. In the email_addresses.txt file, add the mail addresses you want to reach and add a Name if you want to address the Recepient personally or add a "-" if you want to use the default greeting.
   It is important that the mails and the Name are separated by a comma. (see the example mails in the file)
4. In the email_text.txt file, add the mail you want to send.
5. Add the image you want to attach in the same folder as the three other files.
6. In the mailbot.py file, you have to change the following lines: 
-  line 20 & line 83:    replace the "Event-Flyer.jpg" by the name of your image/attachment.
-  line 38 - 41:         insert your SMTP server details
-  line 48:              set the subject of the mail
-  line 52:              set the default greeting
7. run the mailbot.py file


</div>
