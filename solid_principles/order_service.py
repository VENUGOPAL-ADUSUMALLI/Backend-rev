from models import Order

class OrderService:
    def __init__(self,payment, repository, invoice,notification):
        self.repository = repository
        self.notification = notification
        self.invoice = invoice
        self.payment = payment

    def place_order(self, user, products):
        order =  Order(user, products)

        print("Total:", order.calculate_total())

        self.payment.pay()
        self.repository.save_to_database(order)

        self.invoice.generate_invoice(order)

        self.notification.send_email(user.email, order)


