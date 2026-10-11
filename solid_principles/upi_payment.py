from solid_principles.payment import PaymentMethod


class UPIPayment(PaymentMethod):

    def pay(self):
        print("processing upi payment method")

    def refund(self):
        print("processing refund for upi payment")
