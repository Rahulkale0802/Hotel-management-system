
#define menu of restaurant

menu ={
    'pizza':50,
    'Bergur':70,
    'salad':100,
    'Coffee':100,
    'Pasta':120,
}

#Greet
print("Welcome to our restaurant")
print("pizza:Rs50\n Bergur:Rs70\n  salad:Rs100\n Coffee:Rs100\n Pasta:Rs120\n")

Order_total = 0
#80+70 =150

item_one= input("Enter the name of item you want to order=")

if item_one in menu:
    Order_total += menu[item_one]
    print(f"Your item {item_one} has been added to your order")

else:
    print(f"your item {item_one} is not available yet")

another_order=input("Do you want to add another item? (Yes/No)")
if another_order=="Yes":
    item_2=input("Enter the name of second item=")

    if item_2 in menu:
        Order_total += menu[item_2]
        print(f"item  {item_2} has been added to your order")
        
        

    else:
        print(f"Ordered item {item_2} is not available")

    print(f"Total amount to pay is {Order_total}")
