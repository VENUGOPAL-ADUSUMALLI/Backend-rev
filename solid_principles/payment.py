class Payment:
    def pay(self, payment_method):
        if payment_method == "card":
            print("Processing card payment...")
        elif payment_method == "upi":
            print("Processing UPI payment...")
        elif payment_method == "paypal":
            print("Processing PayPal payment...")