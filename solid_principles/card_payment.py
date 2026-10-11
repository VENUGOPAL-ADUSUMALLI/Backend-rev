from solid_principles.payment import PaymentMethod
from solid_principles.refund_service import Refundable


class CardPayment(PaymentMethod, Refundable):

    def pay(self):
        print("processing card payment method")

    def refund(self):
        print("processing refund for card payment")


