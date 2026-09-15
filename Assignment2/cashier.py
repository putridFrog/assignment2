class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("please insert coins")
        dlr = int(input("how many dollars?: "))
        hdlr = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickles = int(input("how many nickles?: "))
        coins = dlr + hdlr / 2 + quarters / 4 + nickles / 20
        return coins

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##
