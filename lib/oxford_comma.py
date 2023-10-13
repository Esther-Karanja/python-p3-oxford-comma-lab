def oxford_comma(items):
  if len(items) ==1:
    return f"{items[0]}"
  elif len(items) ==2:
    return f"{items[0]} and {items[1]}"
  else:
    comma_separator = ", ".join(items[:-1])
    return f"{comma_separator}, and {items[-1]}"



