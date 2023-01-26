class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + other_category.name)
            other_category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"*************{self.name}*************"
        items = ""
        for item in self.ledger:
            if len(item["description"]) > 23:
                item["description"] = item["description"][:23]
            items += f"{item['description']:<23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + "\n" + items + total

def create_spend_chart(categories):
    total_spent = 0
    for category in categories:
        for item in category.ledger:
            if item["amount"] < 0:
                total_spent -= item["amount"]

    chart = "Percentage spent by category\n"
    for i in range(10, -1, -1):
        chart += f"{i*10:<3}|"
        for category in categories:
            spent = 0
            for item in category.ledger:
                if item["amount"] < 0:
                    spent -= item["amount"]
            if (spent / total_spent) * 100 >= i * 10:
                chart += " o"
            else:
                chart += "  "
        chart += "\n"

    chart += "    " + "-"*(len(categories)*2+2) + "\n"
    chart += "     "
    for category in categories:
        chart += f"{category.name[0]}  "
    chart += "\n"
    chart += "     "
    for category in categories:
        chart += f"{category.name[1]}  "
    chart += "\n"
    chart += "     "
    for category in categories:
        chart += f"{category.name[2]}  "
    chart += "\n"
    chart += "     "
    for category in categories:
        chart += f"{category.name[3]}  "
    chart += "\n"
    chart += "     "
    for category
