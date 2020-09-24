def get_animal(sound):
  if sound == "meow":
    return "cat"
  elif sound == "woof":
    return "dog"
  elif sound == "quack":
    return "duck"
  else:
    return "I don't recognize that animal sound"

print(get_animal(input("Enter sound")))

    

