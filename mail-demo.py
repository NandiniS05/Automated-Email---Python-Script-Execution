import smtplib

EMAIL_ADDRESS = "nandinisinghpoonia5dec@gmail.com"
EMAIL_PASSWORD = "mddeduwsjpvhkzip"

recipients = [
    'nandinisinghpoonia5dec@gmail.com',
    'scholasticshiksha@gmail.com'
]

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Automated Email Notification - Python Script Execution'
    body = """Hi,

Just a quick update - your scheduled task has been completed successfully using the Python automation script.

Everything is running smoothly.

Best regards,  
Nandini
"""

    msg = "Subject: " + subject + "\n\n" + body

    smtp.sendmail(EMAIL_ADDRESS, recipients, msg)

print("Email sent successfully ✅")