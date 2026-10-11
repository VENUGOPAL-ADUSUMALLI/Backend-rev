class NotificationService:
    def send_email(self,email,order):
        print(f"Sending order confirmation to {email}, {order}")