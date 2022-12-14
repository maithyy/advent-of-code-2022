NUM_MONKEYS = 7

class Item:
    def __init__(self, worry_level):
        self.worry_level = worry_level
    
    def get_worry(self):
        return self.worry_level
    
    def change_worry(self, new):
        self.worry_level = new
    
    def bored(self):
        self.worry_level = self.worry_level // 3
        #print(f"Bored, divided by 3 to get {self.worry_level}")
        return self.worry_level


class Monkey:
    def __init__(self, number, items, op, divider, throw_true, throw_false):
        self.number = number
        self.items = items
        self.op = op
        self.divider = divider
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.inspected = 0

    def print_hold(self):
        print(f"Monkey {self.number}: ", end="")
        for item in self.items:
            print(item.get_worry(), end=", ")
        print()

    def change_worry(self, item):
        old = item.worry_level
        item.worry_level = eval(self.op)
        #print(f"Worry level is increased to get {item.worry_level}")

    def inspect(self, monkeys_list):
        stopping = len(self.items)
        for item in self.items:
            self.inspected += 1
            #print(f"Monkey inspects an item with a worry level of {item.get_worry()}")
            self.change_worry(item)
            item.bored()
            self.test(item, monkeys_list)
        for _ in range(stopping):
            self.remove_item(self.items[0])
    
    def get_num(self):
        return self.number
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item_to_remove):
        for item in self.items:
            if item.get_worry() == item_to_remove.get_worry():
                self.items.remove(item)
                break

    def test(self, item, monkeys_list):
        if (item.get_worry() % self.divider == 0):
            for monkey in monkeys_list:
                if monkey.get_num() == self.throw_true:
                    monkey.add_item(item)
                    #print(f"thrown to monkey {monkey.get_num()}")
                    return
        else:
            for monkey in monkeys_list:
                if monkey.get_num() == self.throw_false:
                    monkey.add_item(item)
                    #print(f"thrown to monkey {monkey.get_num()}")
                    return

def create_items():
    monkeys = []
    with open('input.txt') as f:
        data = f.readlines()
        for i in range(NUM_MONKEYS + 1):
            start = i * 7
            number = int(data[start][-3])
            items = data[start+1].rstrip().split(": ")[1].split(", ")
            #print(items)
            op = data[start+2].rstrip().split("Operation: new = ")[1]
            divider = int(data[start+3].rstrip().split("Test: divisible by ")[1])
            throw_true = int(data[start+4].rstrip()[-1])
            throw_false = int(data[start+5].rstrip()[-1])
            for index, item in enumerate(items):
                items[index] = Item(int(item))
            monkeys.append(Monkey(number, items, op, divider, throw_true, throw_false))
    return monkeys

def do_round(monkeys):
    for monkey in monkeys:
        #print(f"Monkey {monkey.get_num()}:")
        monkey.inspect(monkeys)

def print_status(monkeys):
    for monkey in monkeys:
        monkey.print_hold()

def get_monkey_business(monkeys):
    my_list = []
    for monkey in monkeys:
        my_list.append(monkey.inspected)
    my_list = sorted(my_list)
    return my_list[-1] * my_list[-2]

def main():
    monkeys = create_items()
    for _ in range(20):
        do_round(monkeys)
        #print_status(monkeys)
    print(get_monkey_business(monkeys))



if __name__ =="__main__":
    main()