import random
from datetime import datetime


class Payment:
    """
    This class handles Payments in cash.
    """

    def __init__(self, amount):
        self.amount = amount
        self.payment_number = OrderNumberGenerator().get_order_number()
        self.transaction_time = datetime.now()
        self.change = 0
        self.is_valid = False

    def get_amount(self):
        """
        Get the payment amount.
        :return: a float
        """
        return self.amount

    def get_payment_number(self):
        """
        Return the Payment number
        :return: an integer
        """
        return self.payment_number

    def get_transaction_time(self):
        """
        Return the time of the transaction
        :return: a datetime object
        """
        return self.transaction_time

    def is_valid(self):
        return self.is_valid

    def pay(self, amount_paid):
        """
        This method is used to make payment.
        :param amount_paid: a float
        :return: the change/balance - a float value if any
        """
        if amount_paid < self.amount:
            print("Payment Incomplete. \n Order Cancelled")
            return None
        self.change = amount_paid - self.amount
        self.is_valid = True
        return self.change

    def __str__(self):
        """
        This function is called when print() is called upon the Payment object
        :return: a string
        """
        return f"PAYMENT NUMBER - {self.get_payment_number()}\n" \
               f"TRANSACTION TIME - {self.get_transaction_time()}\n" \
               f"AMOUNT - {self.get_amount()}\n" \
               f"CHANGE - {self.change}\n" \
               f"-----------------------------------------------------------"


class OrderNumberGenerator:
    """
    This class generates the order number for the Payment that's being made.
    """

    def __init__(self):
        """
        Constructor for the Order Number Generator class
        """
        self.order_number = random.randint(0, 1000)

    def get_order_number(self):
        """
        Get order Number
        :return: an integer
        """
        return self.order_number


class MockPaymentStore:
    """
    This class will save all the Payments being made (the Payment objects)
    """

    def __init__(self):
        self.payment_list = []

    def register_payment(self, current_payment: Payment) -> list:
        """
        This method adds a new payment to the store and returns the list of all the payments made.
        :param current_payment: a Payment object
        :return: a list
        """
        if current_payment.is_valid:
            self.payment_list.append(current_payment)
        return self.payment_list

    def show_all_payments(self):
        """
        Shows all the payments stores in a clean format
        :return:
        """
        for each_payment in self.payment_list:
            print(f"{each_payment}\n")


def main():
    # Initialize a Payment Store
    store = MockPaymentStore()

    # Initialize a payment object
    payment_1 = Payment(10.00)

    # Pay the amount
    payment_1.pay(12.00)

    # Register the Payment in store
    store.register_payment(payment_1)

    # Initialize a payment object
    payment_2 = Payment(200.23)

    # Pay the amount
    payment_2.pay(1200)

    # Register the Payment in store
    store.register_payment(payment_2)

    store.show_all_payments()


if __name__ == "__main__":
    main()
