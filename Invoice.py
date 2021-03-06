class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v['qnt']) * float(v['unit_price']) * float(v['discount']) / 100)
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput

# Group project - Test 1 to calculate the total price of 5 notebooks!
    def fiveNotebooks(self, products):
        for k, v in products.items():
            five_notebook = 5 # harcodding
            five_notebook = float(v['unit_price']) * five_notebook
        five_notebook = round(five_notebook, 2)
        return five_notebook
# Group Project - Test 2 to calculate a 7.25% tax + the pure price of all items
    def totalTax(self, products):
        tax_calculation = self.totalImpurePrice(products) - self.totalDiscount(products)
        tax_calculation += tax_calculation * (7.25/100)
        return round(tax_calculation, 2)
