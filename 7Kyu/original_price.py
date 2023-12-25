# We need to write some code to return the original price of a product, the return type must be of type decimal and the number must be rounded to two decimal places.

# We will be given the sale price (discounted price), and the sale percentage, our job is to figure out the original price.

# For example:
# Given an item at $75 sale price after applying a 25% discount, the function should return the original price of that item before applying the sale percentage, which is ($100.00) of course, rounded to two decimal places.

# DiscoverOriginalPrice(75, 25) => 100.00M where 75 is the sale price (discounted price), 25 is the sale percentage and 100 is the original price

def discover_original_price(discounted_price, sale_percentage):
    try:
        if discounted_price is None or sale_percentage is None:
            raise TypeError
        original_price = float(discounted_price) / (1 - float(sale_percentage) / 100)
        print("{:.2f}".format(round(original_price)))
    except ValueError:
        print("ValueError")
    except TypeError:
        print("TypeError")


discover_original_price(75,25)
discover_original_price(25,75)
discover_original_price(75.75,25)
discover_original_price(373.85,11.2)
discover_original_price(458.2,17.13)
discover_original_price("hello",17.13)
discover_original_price("", 17.13)
