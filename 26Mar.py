"""
def order_pizza(size: str, topping: str = "cheese", *toppings: str) -> str:
    toppings_text = ", ".join((topping, *toppings))
    return f"Order confirmed: {size} pizza with {toppings_text}."

result = order_pizza("small", "pepperoni", "onion", "mushrooms")
print(result)


square = lambda n: n ** 2
print(square(5))

def square(n):
    return n ** 2

"""


numbers = [1, 2, 3, 4, 5, 6]
is_even = lambda n: n % 2 == 0
evens = [n for n in numbers if is_even(n)]