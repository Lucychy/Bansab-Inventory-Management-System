# AI Acknowlegement:
# ChatGPT was used to explain python concepts,
# provide feedback and review my code.
print("BANSAB VENTURES")
print("==============================")
print("INVENTORY MANAGEMENT SYSTEM")
print("Manage smarter. Grow stronger.")

phones =[]

running = True
while running:
    print("BANSAB INVENTORY MANAGEMENT SYSTEM")
    print("1. Add New phone")
    print("2. Add Inventory")
    print("3. Search Phone by IMEI")
    print("4. Exit")
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
        print("Total phones in stock:", len(phones))

        if len(phones) == 0:
            print("No phones have been added yet.")

        else:
            for phone in phones:
                print(phone)
    
    elif choice == "3":
        search_imei = input("Enter IMEI to search: ")
        found = False

        for phone in phones:
            if phone["imei"] == search_imei:
                found = True
                print("Phone found!")
                print(phone)

        if found == False:
            print("Phone not found.")

    elif choice == "4":
        running = False
        print("Thank you for using Bansab")

    else:
        print("Invalid choice. Please try again.")
