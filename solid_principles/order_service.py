from models import Order
from solid_principles.invoice_generator import InvoiceGenerator
from solid_principles.notification_service import NotificationService
from solid_principles.order_respository import OrderRepository
from solid_principles.payment import Payment


class OrderService:
    def __init__(self):
        self.repository = OrderRepository()
        self.notification = NotificationService()
        self.invoice = InvoiceGenerator()
        self.payment = Payment()

    def place_order(self, user, products, payment_method):
        order =  Order(user, products)

        print("Total:", order.calculate_total())

        self.payment.pay(payment_method)

        self.repository.save_to_database()

        self.invoice.generate_invoice()

        self.notification.send_email(user.email)