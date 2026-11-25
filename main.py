# AI Acknowlegement:
# ChatGPT was used to explain python concepts,
# provide feedback and review my code.
print("BANSAB VENTURES")
print("==============================")
print("INVENTORY MANAGEMENT SYSTEM")
print("Manage smarter. Grow stronger.")
business_name = "Bansab Ventures"
product_name = "iphone 17pro"
brand = "Apple"
storage = "512GB"
colour = "Black"
print("Business:",business_name)
print("Product:",product_name)
print("Brand:",brand)
print("Storage:",storage)
print("Colour:",colour)

quantity = 10
selling_price = 1500000
imei = "003567891234567"
discount = 25000.50
print(type(quantity))
print(type(selling_price))
print(type(imei))
print(type(discount))
product_name=input("Enter product name: ")
print("You entered:", product_name)
quantity= int(input("Enter quantity: "))
print(type(quantity))
selling_price = float(input("Enter selling price: "))
print(type(selling_price))


products=["iphone 17pro", "Samsung Galaxy S26ultra", "Google pixel 10 Pro"]
print(products[1])
products.append("iphone 17 promax")
print(products)
print(len(products))
products.remove("Google pixel 10 Pro")
print(products)
for number, product in enumerate(products, start=1):
    print(number, product)
phones =[]

running = True
while running:
    print("BANSAB INVENTORY MANAGEMENT SYSTEM")
    print("1. Add New phone")
    print("2. Add Inventory")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        phone_brand = input("Enter phone brand: ")
        phone_model = input("Enter phone model: ")
        phone_storage = input("Enter phone storage: ")
        phone_colour = input("Enter phone colour: ")
        phone_imei = input("Enter phone imei: ")
        selling_price = float(input("Enter selling price (₦): "))
        purchase_cost = float(input("Enter purchase cost (₦): "))

        phone = {
            "brand": phone_brand,
            "model": phone_model,
            "storage": phone_storage,
            "colour": phone_colour,
            "imei": phone_imei,
            "selling_price": selling_price,
            "purchase_cost": purchase_cost
        }

        phones.append(phone)
        print("Phone added successfully!")

        print(phone)
    elif choice == "2":
        print("BANSAB PHONE INVENTORY")

        if len(phones) == 0:
            print("No phones have been added yet.")

        else:
            for phone in phones:
                print(phone)
    elif choice == "3":
        running = False
        print("Thank you for using Bansab")

    else:
        print("Invalid choice. please try again.")









