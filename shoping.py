print(("Welcome to Shopping Cart").center(30))
empty_cart=[]
total=0
while True:
    print(("1.Add Item").center(30))
    print(("2.View Cart").center(30))
    print(("3.Total Price").center(30))
    print(("4.Exit").center(30))
    choice=int(input("Enter your choice: "))
    if choice==1:
        item_name=input("Enter the name of the item: ")
        item_price=float(input("Enter the price of the item: "))
        empty_cart.append((item_name,item_price))
        print(("Added to cart successfully").center(30))
        total+=item_price
    elif choice==2:
        if len(empty_cart)==0:
            print(("Shopping cart is empty").center(30))
        else:
            print(empty_cart)
    elif choice==3:
        print(f"Total parice of items : {total}")     
    elif choice==4:
        print(("Thank you for shopping with us").center(30))
        break
    else:
        print("Invalid choise\nTry again")




    

