# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    # Apply discount only if 20% or higher
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price  # return original price if discount < 20

# Main program
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

# Display result
if discount_percent >= 20:
    print(f"Discount applied. Final price: {final_price:.2f}")
else:
    print(f"No discount applied. Price remains: {final_price:.2f}")
