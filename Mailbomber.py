import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Bomber")

        # Create and place labels and entry widgets
        self.create_label_and_entry("SMTP Server:", 0)
        self.create_label_and_entry("Port:", 1)
        self.create_label_and_entry("Username:", 2)
        self.create_label_and_entry("Password:", 3, show="*")
        self.create_label_and_entry("Send To:", 4)
        self.create_label_and_entry("Sent From:", 5)
        self.create_label_and_entry("Subject:", 6)
        self.create_label_and_entry("Number of Copies:", 7)

        # Body text area
        tk.Label(root, text="Message:").grid(row=8, column=0, sticky=tk.W, padx=5, pady=5)
        self.body_text = tk.Text(root, height=10, width=50)
        self.body_text.grid(row=8, column=1, padx=5, pady=5)

        # Send button
        send_button = tk.Button(root, text="Send Email", command=self.send_email)
        send_button.grid(row=9, column=1, pady=10)

    def create_label_and_entry(self, text, row, show=None):
        label = tk.Label(self.root, text=text)
        label.grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        entry = tk.Entry(self.root, width=50, show=show)
        entry.grid(row=row, column=1, padx=5, pady=5)
        setattr(self, text.replace(" ", "_").replace(":", "").lower(), entry)

    def send_email(self):
        try:
            smtp_server = self.smtp_server.get()
            port = int(self.port.get())
            username = self.username.get()
            password = self.password.get()
            send_to = self.send_to.get().split(',')
            send_from = self.sent_from.get()
            subject = self.subject.get()
            number_of_copies = int(self.number_of_copies.get())
            body = self.body_text.get("1.0", tk.END)

            for _ in range(number_of_copies):
                # Set up the MIME
                message = MIMEMultipart()
                message['From'] = send_from
                message['To'] = ', '.join(send_to)
                message['Subject'] = subject

                # Attach the body with the msg instance
                message.attach(MIMEText(body, 'plain'))

                # Create SMTP session
                with smtplib.SMTP(smtp_server, port) as server:
                    server.starttls()
                    server.login(username, password)
                    server.sendmail(send_from, send_to, message.as_string())

            messagebox.showinfo("Success", "Email(s) sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailSenderApp(root)
    root.mainloop()
