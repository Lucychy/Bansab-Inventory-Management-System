# AI Acknowlegement:
# ChatGPT was used to explain python concepts,
# review my code.
import json
print("BANSAB VENTURES")
print("==============================")
print("INVENTORY MANAGEMENT SYSTEM")
print("Manage smarter. Grow stronger.")

try:
    with open("phones.json", "r") as file:
        phones = json.load(file)

except FileNotFoundError:
    phones = []

running = True
while running:
    print("BANSAB INVENTORY MANAGEMENT SYSTEM")
    print("1. Add New phone")
    print("2. Add Inventory")
    print("3. Search Phone by IMEI")
    print("4. Check Low Stock")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        phone_brand = input("Enter phone brand: ")
        phone_model = input("Enter phone model: ")
        phone_storage = input("Enter phone storage: ")
        phone_colour = input("Enter phone colour: ")
        phone_location = input("Enter phone location: ")
        phone_imei = input("Enter phone imei: ")
        imei_exists = False

        for phone in phones:
            if phone["imei"] == phone_imei:
                imei_exists = True
        if imei_exists == True:
                print("This IMEI already exists! phone cannot be added.")

        else:
                print("IMEI is available. Continue adding phone.")
                selling_price = float(input("Enter selling price (₦): "))
                purchase_cost = float(input("Enter purchase cost (₦): "))

                phone = {
                    "brand": phone_brand,
                    "model": phone_model,
                    "storage": phone_storage,
                    "colour": phone_colour,
                    "location": phone_location,
                    "imei": phone_imei,
                    "selling_price": selling_price,
                    "purchase_cost": purchase_cost
                }

                phones.append(phone)

                with open("phones.json", "w") as file:
                    json.dump(phones, file, indent=4)

                print("Phone added successfully!")

                print(phone)
    elif choice == "2":
        print("BANSAB PHONE INVENTORY")
        print("Total phones in stock:", len(phones))

        if len(phones) == 0:
            print("No phones have been added yet.")

        else:
            for phone in phones:
                print("------------------------------")
                print("Brand:", phone["brand"])
                print("Model:", phone["model"])
                print("Storage:", phone["storage"])
                print("Colour:", phone["colour"])
                print ("Location:", phone.get("location", "Not recorded"))
                print("IMEI:", phone["imei"])
                print("Selling Price: ₦", format(phone["selling_price"], ",.0f"))
                print("------------------------------")
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
        print("BANSAB LOW STOCK ALERT")
        low_stock_threshold = 3

        model_brand = input("Enter phone brand: ")
        model_name = input("Enter phone model: ")
        model_count = 0
        for phone in phones:
            if phone["brand"] == model_brand and phone["model"] == model_name:
                model_count = model_count + 1
        if model_count == 0:
            print("Out of stock")

        elif model_count <= low_stock_threshold:
            print("Low stock:", model_count, "phones remaining")

        else:
            print("In stock:", model_count, "phones available")
    elif choice == "5":
        running = False
        print("Thank you for using Bansab")

    else:
        print("Invalid choice. Please try again.")