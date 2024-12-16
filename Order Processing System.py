#Order processing 
class Order:
    def __init__(self, order_id, customer_id, items, total_price):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.total_price = total_price
        self.status = 'Pending'

    def process_order(self):
        print(f"Processing order {self.order_id}...")
        # Simulating inventory check
        if self.check_inventory():
            self.status = 'Processed'
            print(f"Order {self.order_id} is processed.")
        else:
            self.status = 'Failed'
            print(f"Order {self.order_id} failed due to inventory issues.")

    def check_inventory(self):
        # Simulate inventory check, return True for success
        return True

    def update_status(self, status):
        self.status = status
        print(f"Order {self.order_id} status updated to {self.status}")

# Example usage
order = Order(1, 101, ['item1', 'item2'], 100)
order.process_order()


#Payment 
import random

class PaymentGateway:
    def __init__(self, order):
        self.order = order
        self.payment_status = 'Pending'

    def process_payment(self):
        print(f"Processing payment for order {self.order.order_id}...")
        # Simulating payment success or failure
        if random.choice([True, False]):
            self.payment_status = 'Success'
            self.order.update_status('Paid')
            print(f"Payment successful for order {self.order.order_id}.")
        else:
            self.payment_status = 'Failed'
            print(f"Payment failed for order {self.order.order_id}.")
        
        
        
        
        
        
# Example usage
payment_gateway = PaymentGateway(order)
payment_gateway.process_payment()


#Customer support
class SupportTicket:
    def __init__(self, ticket_id, customer_id, issue):
        self.ticket_id = ticket_id
        self.customer_id = customer_id
        self.issue = issue
        self.status = 'Open'

    def resolve_ticket(self):
        print(f"Resolving ticket {self.ticket_id}...")
        # Simulating ticket resolution process
        if self.issue.lower() == "order issue":
            self.status = 'Resolved'
            print(f"Ticket {self.ticket_id} resolved successfully.")
        else:
            self.status = 'Pending'
            print(f"Ticket {self.ticket_id} is still pending resolution.")
    
    def update_status(self, status):
        self.status = status
        print(f"Ticket {self.ticket_id} status updated to {self.status}")

# Example usage
ticket = SupportTicket(1, 101, "Order issue")
ticket.resolve_ticket()

#shipping 
class Shipping:
    def __init__(self, order):
        self.order = order
        self.shipping_status = 'Pending'

    def fulfill_order(self):
        print(f"Fulfilling order {self.order.order_id}...")
        # Simulating fulfillment process
        if self.check_shipping_availability():
            self.shipping_status = 'Shipped'
            self.order.update_status('Shipped')
            print(f"Order {self.order.order_id} has been shipped.")
        else:
            self.shipping_status = 'Failed'
            print(f"Shipping for order {self.order.order_id} failed.")

    def check_shipping_availability(self):
        # Simulating shipping availability check
        return True

# Example usage
shipping = Shipping(order)
shipping.fulfill_order()



#Full integration 
class ECommerceProcess:
    def __init__(self, order_id, customer_id, items, total_price):
        self.order = Order(order_id, customer_id, items, total_price)
        self.payment_gateway = PaymentGateway(self.order)
        self.shipping = Shipping(self.order)
        self.support_ticket = SupportTicket(order_id, customer_id, "Order issue")

    def execute_process(self):
        # Step 1: Process order
        self.order.process_order()

        # Step 2: Process payment
        self.payment_gateway.process_payment()

        # Step 3: Handle shipping
        self.shipping.fulfill_order()

        # Step 4: Manage customer support (if any)
        self.support_ticket.resolve_ticket()

# Example usage
ecommerce_process = ECommerceProcess(1, 101, ['item1', 'item2'], 100)
ecommerce_process.execute_process()
