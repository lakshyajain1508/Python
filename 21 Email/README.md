# Sending Emails with Python

This guide explains how to use Python's built-in `smtplib` library to send emails. It's a common and effective method for automating email notifications, reports, and more.

A key step for modern email providers like Google, Microsoft, and others is using an **App Password** instead of your regular account password. This is required for security reasons, as these providers block attempts to log in with a regular password from third-party applications.

---

### Step 1: Generate an App Password (For Gmail)

To use `smtplib` with a Gmail account, you must create a specific "App Password" to use in your script.

1.  **Enable 2-Step Verification:** If you haven't already, enable 2-Step Verification on your Google Account. This is a prerequisite for creating app passwords. You can do this in your Google Account settings under **Security**.
2.  **Navigate to App Passwords:** Go to the [Google Account Security page](https://myaccount.google.com/security).
3.  **Select App Passwords:** Click on **App Passwords** under the "How you sign in to Google" section. You may be asked to log in again.
4.  **Create a New App Password:**
    * In the "Select app" dropdown, choose **Mail**.
    * In the "Select device" dropdown, choose **Other (Custom Name)**.
    * Give it a descriptive name like "Python Email Script" and click **Generate**.
5.  **Copy the Password:** A 16-character password will be displayed. **Copy this password immediately.** You will not be able to see it again. This is the password you will use in your Python script.

---

### Step 2: Write the Python Script

The following script is a basic example of how to send an email. You will need to replace the placeholder values with your own information and the app password you just generated.

```python
import smtplib
from email.message import EmailMessage

# --- User-defined variables ---
# Your email address and the app password you generated
SENDER_EMAIL = 'your_email@gmail.com'
APP_PASSWORD = 'your_16_digit_app_password'

# The recipient's email address
RECIPIENT_EMAIL = 'recipient_email@example.com'

# The subject of the email
SUBJECT = "Test Email from Python"

# The body of the email
BODY = """
Hello,

This is a test email sent from a Python script.
It uses the `smtplib` library.

Best regards,
Your Python Script
"""
# --- End of user-defined variables ---

try:
    # Create the email message object
    msg = EmailMessage()
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg.set_content(BODY)

    # Connect to the SMTP server (for Gmail, this is the server)
    print("Connecting to SMTP server...")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        # Log in to the server using your email and app password
        print("Logging in...")
        smtp.login(SENDER_EMAIL, APP_PASSWORD)

        # Send the email
        print("Sending email...")
        smtp.send_message(msg)

    print("Email sent successfully!")

except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Did you use the correct App Password?")
    print("Make sure you are not using your regular account password.")
except Exception as e:
    print(f"An error occurred: {e}")
```

**How to Run the Script**
1. Save the code above as a Python file (e.g., send_email.py).
2. Update the SENDER_EMAIL, APP_PASSWORD, and RECIPIENT_EMAIL variables in the script.
3. Open a terminal or command prompt.
4. Navigate to the directory where you saved the file.
5. Run the script with the following command:
```
python send_email.py
```
If everything is configured correctly, you should see "Email sent successfully!" in your terminal, and the recipient will receive the email.
