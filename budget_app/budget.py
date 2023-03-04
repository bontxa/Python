class Category:
    
    def __init__(self, cat_name):
        self.name = cat_name
        self.ledger = []
        self.count_plus = 0
        self.count_minus = 0

    def deposit(self, amount, opt=None):
        if opt == None:
            opt = ''
        self.ledger.append({"amount": amount, "description": opt})
        self.count_plus += amount

    def withdraw(self, amount, opt=None):
        if opt == None:
            opt = ''
        partial = self.count_minus + amount
        if partial <= self.count_plus:
            self.ledger.append({"amount": amount * -1, "description": opt})
            self.count_minus += amount
            return True
        return False

    def transfer(self, amount, obj):
        if self.withdraw(amount, f'Transfer to {obj.name}') == True:
            obj.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def get_balance(self):
        return self.count_plus - self.count_minus
    
    def check_funds(self, value):
        if self.count_plus - self.count_minus >= value:
            return True
        return False
    
    def __str__(self):
        sh = self.name.center(30, '*') + '\n'
        sb = ''
        format_total = "{:.2f}".format(self.count_plus - self.count_minus)
        total = str(format_total)
        st = 'Total: ' + total
        for values in self.ledger:
            format_float = "{:.2f}".format(values["amount"])
            new_value = "{:<7}".format(str(format_float)[:7].rjust(7))
            sb += "{:<23}".format(values["description"][:23]) + new_value + '\n'
        sh += sb + st
        return sh

def split_names(categories):
    splitted = []
    result = ''
    i = 0
    length = 0
    j = 0
    for values in categories:
        letter = [x for x in values.name]
        splitted.append(letter)
    for values in splitted:
        if length < len(values):
            length = len(values)
    while j < length:
        result += '    ' 
        for values in splitted:
            if i < len(values):
                result += ' ' + values[i] + ' '
            else:
                result += '   '
        result += ' '
        if j < length -1:
            result += '\n'
        i += 1
        j += 1
    return result


def percent(part, total):
  percent = 100 * int(part)/int(total)
  return percent

def create_table(categories):
    number_column = 100
    total_exit = 0
    graph = ''
    for values in categories:
        total_exit += values.count_minus
    while number_column >= 0:
        if number_column == 0:
            graph += '  '
        elif number_column != 100:
            graph += ' '
        graph += str(number_column) + '|'
        for values in categories:
            value = percent(values.count_minus, total_exit)
            if value > number_column:
                graph += ' o '
            else:
                graph += '   '
        graph += ' \n'
        number_column -= 10
    graph += '    '
    for values in categories:
        graph += '---'
    graph += '-\n'
    return graph

def create_spend_chart(categories):
    title = 'Percentage spent by category\n'
    table = create_table(categories)
    names = split_names(categories)
    return title + table + names