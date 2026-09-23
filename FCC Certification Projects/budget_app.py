class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        output = self.name.center(30, "*") + "\n"
        for item in self.ledger:
            desc = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            output += f"{desc:<23}{amount:>7}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output

# 1. Create your categories
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

# 2. Add some deposits and withdrawals (spending)
food.deposit(1000, "initial deposit")
food.withdraw(300.50, "groceries")

clothing.deposit(500, "initial deposit")
clothing.withdraw(150.25, "new clothes")

auto.deposit(800, "initial deposit")
auto.withdraw(50.00, "gas")
print(food)
print(clothing)
print(auto)


def create_spend_chart(categories):
    # 1. Calculate total withdrawals (spending) for each category
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(spent)

    # 2. Calculate total spending across all categories
    total_spent = sum(spent_amounts)

    # 3. Calculate percentages rounded down to the nearest 10
    percentages = []
    if total_spent > 0:
        for spent in spent_amounts:
            # Formula to round down to the nearest 10 (e.g., 87 -> 80)
            percent = int((spent / total_spent) * 100 // 10) * 10
            percentages.append(percent)
    else:
        percentages = [0 for _ in categories]

    # 4. Build the chart title and y-axis rows (from 100 down to 0)
    chart = "Percentage spent by category"
    
    for i in range(100, -1, -10):
        # Format the y-axis label (e.g., "100|", " 90|", ..., "  0|")
        chart += f"\n{i:>3}|"
        for percent in percentages:
            if percent >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " "  # Trailing space required at the end of each bar row

    # 5. Build the horizontal line underneath the bars
    # Length depends on how many categories there are (3 dashes per category + 1 extra)
    chart += "\n    " + "-" * (len(categories) * 3 + 1)

    # 6. Build the vertical category names
    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        chart += "\n     "  # 4 spaces of padding to match the y-axis width
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "  # Blank space if the name is shorter than the max length

    return chart


categories_list = [food, clothing, auto]

print(create_spend_chart(categories_list))