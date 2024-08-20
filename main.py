import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()


### Custom imports

from mailer import send_email

################# CONFIGURATIONS ####################


sender_mail = os.getenv("SENDER_MAIL")
sender_pass = os.getenv("SENDER_PASS")
excel_file = "HRContacts.xlsx"
mail_body_file = "mailbody.html"
mail_subject = "Seeking Internship/Full-Time Opportunity for Software Development roles"


#####################################################


# Load the data from the XLSX file and template
data = pd.read_excel(excel_file, names=["Email"])

if "Email" in data.columns:
    email_col = data["Email"]
else:
    raise ValueError("The 'Email' column does not exist in the dataframe")

if "Company" in data.columns:
    company_col = data["Companymail"]
else:
    raise ValueError("The 'Company' column does not exist in the dataframe")

with open(mail_body_file, "r", encoding='utf-8') as file:
    body = file.read()


################## User inputs ##################


total_emails = len(email_col)
start = int(input("Enter the row number to start from: "))
start = start - 1

if start >= total_emails:
    raise ValueError(f"Starting row number {start+1} is out of range of {len(total_emails)}")


######################### Core Logic #########################


successful_emails = []
failed_emails = []
count = 1
for i in range(start,len(email_col)):
    email = email_col[i]
    company =company_col[i]
    new_body = body.replace("{{company}}", company)

    result = send_email(email, mail_subject, new_body,sender_mail,sender_pass)
    if result:
        successful_emails.append(email)
    else:
        failed_emails.append(email)
    print(f"Sent email to {email} ({count}/{total_emails})")
    count += 1


######################### Printing Results #########################


print(f"All emails sent successfully! {len(successful_emails)}/{total_emails}")
if failed_emails:
    print(f"Emails that failed to send: {failed_emails}")