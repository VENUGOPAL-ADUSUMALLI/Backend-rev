from solid_principles.payment import PaymentMethod


class CashPayment(PaymentMethod):

    def pay(self):
        print("paying using cash....")
