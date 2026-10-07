from models import Product, User, Order
from solid_principles.order_service import OrderService
from solid_principles.payment import Payment
from solid_principles.invoice_generator import InvoiceGenerator
from solid_principles.notification_service import NotificationService

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
email.send_email(user.email)

invoice = InvoiceGenerator()
invoice.generate_invoice()

payment_method = Payment()
payment_method.pay("upi")


order_service = OrderService()

order_service.place_order(
    user,
    products,
    "upi"
)