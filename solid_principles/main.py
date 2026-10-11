from models import Product, User, Order
from solid_principles.card_payment import CardPayment
from solid_principles.invoice_generator import InvoiceGenerator
from solid_principles.notification_service import NotificationService
from solid_principles.order_respository import OrderRepository
from solid_principles.order_service import OrderService
from solid_principles.refund_service import Refundable
from solid_principles.upi_payment import UPIPayment

user = User(
    1,
    "Venu",
    "venu@gmail.com"
)

products = [
    Product(1, "Laptop", 60000),
    Product(2, "Mouse", 2000)
]

order = Order(user, products)

print("Total:", order.calculate_total())

email = NotificationService()
email.send_email(user.email,order)

invoice = InvoiceGenerator()
invoice.generate_invoice(order)


upi = UPIPayment()
upi.pay()

card = CardPayment()
card.pay()

repo = OrderRepository()
invoice = InvoiceGenerator()
notification = NotificationService()

order_service = OrderService(upi, repo, invoice,notification)

order_service.place_order(
    user,
    products
)



def process_refund(payment:Refundable):
    payment.refund()

card = CardPayment()
process_refund(card)
