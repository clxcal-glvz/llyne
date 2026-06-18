def get_price_category(price):
    # Logic to determine if Budget, Mid-range, or Premium
    if price < 500:  # Secret Value 1 (e.g., below P500)
        return "Budget"
    elif price < 2000:  # Secret Value 2 (e.g., P500 to P1999)
        return "Mid-range"
    else:
        return "Premium"

def check_stock_level(stock):
    # Logic to determine if stock is sufficient
    if stock >= 10:  # Secret Threshold (e.g., 10 units)
        return "OK"
    else:
        return "LOW STOCK - Reorder needed"

def save_product(name, price, category, stock, stock_status):
    # File handling logic using 'a' for append mode
    with open('inventory.txt', "a") as file:
        file.write(f"Product: {name} | Price: P{price:.2f} | Category: {category} | Stock: {stock} ({stock_status})\n")

# Main Loop
while True:
    print("\n--- ADD NEW PRODUCT ---")
    # 1. COLLECTION: Get data from user
    name = input("Enter product name: ")
    price = float(input("Enter product price: P"))
    stock = int(input("Enter stock quantity: "))
    
    # 2. PROCESSING: Call the functions above
    category = get_price_category(price)
    stock_status = check_stock_level(stock)
    
    # 3. OUTPUT: Display status and save to file
    print(f"\nProduct Category: {category}")
    print(f"Stock Status: {stock_status}")
    
    save_product(name, price, category, stock, stock_status)
    print("Product saved to inventory.txt successfully.")
    
    choice = input("\nAdd another product? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting Inventory System. Goodbye!")
        break