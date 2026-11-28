# AI Acknowlegement:
# ChatGPT was used to explain python concepts,
# review my code.
import json
from datetime import datetime
print("BANSAB VENTURES")
print("==============================")
print("INVENTORY MANAGEMENT SYSTEM")
print("Manage smarter. Grow stronger.")

try:
    with open("phones.json", "r") as file:
        phones = json.load(file)

except FileNotFoundError:
    phones = []
for phone in phones:
    phone.setdefault("status", "In stock")
with open("phones.json", "w") as file:
    json.dump(phones, file, indent=4)

running = True
try:
    with open("sales.json", "r") as file:
        sales = json.load(file)

except FileNotFoundError:
    sales = []
while running:
    print("BANSAB INVENTORY MANAGEMENT SYSTEM")
    print("1. Add New phone")
    print("2. Add Inventory")
    print("3. Search Phone by IMEI")
    print("4. Check Low Stock")
    print("5. Exit")
    print("6. Update Phone Stock Status")
    print("7. Complete Phone Sale")
    print("8. Review sales History")
    print("9. Daily Sales Report")
    print("10. Monthly Sales Report")
    print("11. Yearly Sales Report")
    choice = input("Enter your choice: ").strip()

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
                    "purchase_cost": purchase_cost,
                    "status": "In stock"
                }

                phones.append(phone)

                with open("phones.json", "w") as file:
                    json.dump(phones, file, indent=4)

                print("Phone added successfully!")

                print(phone)
    elif choice == "2":
        print("BANSAB PHONE INVENTORY")
        print("Total recorded phones:", len(phones))
        available_count = 0
        pending_count = 0
        sold_count = 0
        for phone in phones:
            if phone["status"] == "In stock":
                available_count = available_count + 1
            elif phone["status"] == "Pending":
                pending_count = pending_count + 1

            elif phone["status"] == "Sold":
                sold_count = sold_count + 1
        print("Available phones:", available_count)
        print("Pending phones:", pending_count)
        print("Sold phones:", sold_count)
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
                print("Stock Status:", phone.get("status", "In stock"))
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
            if phone["brand"] == model_brand and phone["model"] == model_name and phone["status"] == "In stock":               
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
    elif choice == "6":
        update_imei = input("Enter phone IMEI: ")
        found = False
        for phone in phones:
            if phone["imei"] == update_imei:
                found = True
                print("Phone found!")
                print("Current status:", phone.get("status", "In stock"))
                if phone["status"] == "Sold":
                    print("This phone has already been sold.")
                else:
                    print("Choose new phone status:")
                    print("1. In stock")
                    print("2. Pending")
                    new_status = input("Enter your choice: ")
                    if new_status == "1":
                        phone["status"] = "In stock"

                    elif new_status == "2":
                        phone["status"] = "Pending"
                    else:
                        print("Invalid status choice.")

        if found == False:
                print("Phone not found.")
        with open("phones.json", "w") as file:
            json.dump(phones, file, indent=4)
    elif choice == "7":
        sale_imei = input("Enter phone IMEI to sell: ")
        found = False
        for phone in phones:
            if phone["imei"] == sale_imei:
                found = True
                print("Phone found!")
                if phone["status"] == "Sold":
                    print("This phone has already been sold.")
                else:
                    print("Phone is available for sale.")
                    print("Brand:", phone["brand"])
                    print("Model:", phone["model"])
                    print("Storage:", phone["storage"])
                    print("Colour:", phone["colour"])
                    print("IMEI:", phone["imei"])
                    print("Selling Price: ₦", format(phone["selling_price"], ",.0f"))
                    confirm_sale = input("Confirm sale? (yes/no): ")
                    if confirm_sale.lower() == "yes":
                       
                        sale_date = datetime.now().strftime("%d/%m/%Y")
                        sale_time = datetime.now().strftime("%H:%M:%S")
                        profit = phone["selling_price"] - phone["purchase_cost"]
                        sale_year = datetime.now().year
                        transaction_id = "BSV-" + str(sale_year) + "-" + str(len(sales) + 1).zfill(4)
                        sale = {
                            "transaction_id": transaction_id,
                            "brand": phone["brand"],
                            "model": phone["model"],
                            "imei": phone["imei"],
                            "selling_price": phone["selling_price"],
                            "purchase_cost": phone["purchase_cost"],
                             "profit": profit,
                            "sale_date": sale_date,
                            "sale_time": sale_time
                        }
                        sales.append(sale)
                        with open("sales.json", "w") as file:
                            json.dump(sales, file, indent=4)
                        phone["status"] = "Sold"
                        with open("phones.json", "w") as file:
                            json.dump(phones, file, indent=4)
                            print("==============================")
                            print("BANSAB VENTURES")
                            print("SALE COMPLETED SUCCESSFULLY")
                            print("==============================")
                            print("Transaction ID:", transaction_id)
                            print("Product:", phone["brand"], phone["model"])
                            print("IMEI:", phone["imei"])
                            print("Amount Paid: ₦", format(phone["selling_price"], ",.0f"))
                            print("Date:", sale_date)
                            print("Time:", sale_time)
                            print("Stock Status:", phone["status"])
                            print("==============================")
                    elif confirm_sale.lower() == "no":
                        print("Sale cancelled.")

                    else:
                        print("Invalid response.")
        if found == False:
            print("Phone not found.")
        
    elif choice == "8": 
        print("BANSAB SALES HISTORY")
        if len(sales) == 0:
            print("No sales have been recorded yet.")
        else:
            for sale in sales:
                print("==============================")
                print("Transaction ID:", sale["transaction_id"])
                print("Product:", sale["brand"], sale["model"])
                print("IMEI:", sale["imei"])
                print("Amount Paid: ₦", format(sale["selling_price"], ",.0f"))
                print("Date:", sale["sale_date"])
                print("Time:", sale["sale_time"])
                print("==============================")
    elif choice == "9": 
                print("BANSAB DAILY SALES REPORT")
                today = datetime.now().strftime("%d/%m/%Y")
                print("Date:", today)
                total_sold = 0
                total_revenue = 0
                total_cost = 0
                total_profit = 0
                for sale in sales:
                    if sale["sale_date"] == today:
                        total_sold = total_sold + 1
                        total_revenue = total_revenue + sale["selling_price"]
                        total_cost = total_cost + sale["purchase_cost"]
                        total_profit = total_profit + sale["profit"]
                print("==============================")
                print("Total Phones Sold:", total_sold)
                print("Total Revenue: ₦", format(total_revenue, ",.0f"))
                print("Total Purchase Cost: ₦", format(total_cost, ",.0f"))
                print("Gross Profit: ₦", format(total_profit, ",.0f"))
                print("==============================")

    elif choice == "10":
        print("BANSAB MONTHLY SALES REPORT")
        current_month = datetime.now().strftime("%m/%Y")
        print("Month:", current_month)
        total_sold = 0
        total_revenue = 0
        total_cost = 0
        total_profit = 0
        for sale in sales:
            if sale["sale_date"].endswith(current_month):
                total_sold = total_sold + 1
                total_revenue = total_revenue + sale["selling_price"]
                total_cost = total_cost + sale["purchase_cost"]
                total_profit = total_profit + sale["profit"]
        print("==============================")
        print("Total Phones Sold:", total_sold)
        print("Total Revenue: ₦", format(total_revenue, ",.0f"))
        print("Total Purchase Cost: ₦", format(total_cost, ",.0f"))
        print("Gross Profit: ₦", format(total_profit, ",.0f"))
        print("==============================") 
    elif choice == "11":
        print("BANSAB YEARLY SALES REPORT")
        current_year = datetime.now().strftime("%Y")
        print("Year:", current_year)
        total_sold = 0
        total_revenue = 0
        total_cost = 0
        total_profit = 0
        for sale in sales:
            if sale["sale_date"].endswith(current_year):
                total_sold = total_sold + 1
                total_revenue = total_revenue + sale["selling_price"]
                total_cost = total_cost + sale["purchase_cost"]
                total_profit = total_profit + sale["profit"]
        print("==============================")
        print("Total Phones Sold:", total_sold)
        print("Total Revenue: ₦", format(total_revenue, ",.0f"))
        print("Total Purchase Cost: ₦", format(total_cost, ",.0f"))
        print("Gross Profit: ₦", format(total_profit, ",.0f"))
        print("==============================")   
                          
                
    else:
        print("Invalid choice. Please try again.")
        


    