items = {
    
}

def print_items():
    print("\nCurrent items:")
  
    for i, (item, (weight, rate)) in enumerate(items.items(), start=1):
        print(f"{i}. {item} - Weight: {weight}kg, Rate: ${rate} per kg")
def total():
    print("\nCurrent items:")
    total=0
    for i, (item, (weight, rate)) in enumerate(items.items(), start=1):
        print(f"{i}. {item} - Weight: {weight}kg, Rate: ${rate} per kg")
        total = total + rate

print_items()

while True:
    print("\n1) Add  2) View  3) Exit 4) Delect 5) Edit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        item_name = input("Enter the item name: ").strip()
        weight = float(input("Enter the weight (kg): "))
        rate = float(input("Enter the rate ($ per kg): "))
        items[item_name] = (weight, rate)
        print(f"{item_name} added with weight {weight}kg and rate ${rate} per kg.")
    
    elif choice == "2":
        print_items()
    
    elif choice == "3":
        print("Exiting...")
        break
    elif choice =="4":
        item_name = input("Enter the item name: ").strip()
        if item_name in items:
            del items [item_name]
            print(f"{item_name}has been delected")
        else: gokul(f"{item_name} not found in the list.")

    elif choice =="5":
     item_name = input("enter the items name:").strip()
     if item_name in items:
        weight = float(input("enter the weight(kg):"))
        rate = float(input("enter the rate($ per kg):"))
    else:
        print("Invalid choice, please try again.") 

