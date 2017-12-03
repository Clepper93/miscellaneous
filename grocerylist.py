class Grocery:
    def __init__(self,name,price,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def item_cost(self):
        return self.price * self.quantity

grocery_list = [Grocery('beans',1),Grocery('eggs',3.5),Grocery('burritoes',1.75),Grocery('bread',3)]
my_shopping_list = []
def getquantity():
    itemget = str(input("What's on your list?\n"))
    testlist = []
    for item in grocery_list:
        testlist.append(item.name)
    if itemget not in testlist:
        newprice = float(input("how much is/are {}? Please enter an integer without a dollar sign.\n".format(itemget)))
        newquant = int(input("How many are you getting? Please enter an integer.\n"))
        grocery_list.append(Grocery(itemget,newprice,newquant))
        newitem = grocery_list[-1]
        my_shopping_list.append(newitem)         
    else:
        for item in grocery_list:
            if itemget == item.name:
                itemquant = int(input("How many are you getting? Please enter an integer.\n"))
                item.quantity = itemquant
                my_shopping_list.append(item)
    again = str(input("Anything else? Y/N\n"))
    if again.lower() == 'y' or again.lower() == 'yes':
        getquantity()
          
def get_totals():
    for item in my_shopping_list:
        print("{}: {} at ${} for a total of ${}".format(item.name,item.quantity, item.price, item.item_cost()))

def grand_total():
    total = 0
    for item in my_shopping_list:
        itemprice = item.item_cost()
        total += itemprice
    print("Grand Total: ${}".format(total))

        
def try_quantity():
    try:
        getquantity()
    except:
        print("Price and quantity input must be an integer. Please try again.\n")
        del my_shopping_list[:]
        try_quantity()
try_quantity()
get_totals()
grand_total()
