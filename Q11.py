# Given a dictionary of products and their prices, find the product with the highest price.

Sales={"Rice":80,
       "Soup":40,
       "Milk":37,
       "Dall":60,
       "Honey":100,
       "Salt":20,
       "Suger":50}
# highest_price=0
# highest_product=""

# for product,price in Sales.items():
#     if price>highest_price:
#         highest_price=price
#         highest_product=product

# print(highest_product,highest_price)


heighest_product=max(Sales,key=Sales.get)

print(heighest_product,Sales[heighest_product])
