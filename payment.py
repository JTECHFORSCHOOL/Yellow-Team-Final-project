# payment.py
class Payment:
    def __init__(self, ride_id, amount, payment_method, status="Pending"):
        self.ride_id = ride_id
        self.amount = amount
        self.payment_method = payment_method
        self.status = status