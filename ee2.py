def book_cost(quantity):
	discount_factor = 0.6
	discounted_price = 24.95 * discount_factor
	total_price = discounted_price * quantity
	return total_price
	
def shiping_cost(quantity):
	shipping_first = 3
	shipping_rest = 0.75
	total_shipping = shipping_first + ((quantity-1) * shipping_rest)
	return total_shipping
	
num_books = int(raw_input('How many books do your want? '))
total_cost = book_cost(num_books) + shiping_cost(num_books)
print "shipping", num_books, "books costs", total_cost
