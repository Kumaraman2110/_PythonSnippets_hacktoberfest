# Tell if a number is odd or even


def odd_or_even(num: int):
  is_even = not bool(num&1)
  
  if is_even:
    print(f"Number {num} is even")
  else:
    print(f"Number {num} is odd")
  
# sample
odd_or_even(10)

