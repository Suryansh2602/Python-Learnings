def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax-discount
    return final_price

# total = ;
print(f"The total price is: {calculate_total(100, 0.05, 10)}") 