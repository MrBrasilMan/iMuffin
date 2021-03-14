def rm_p(toparse):
  list_parse = list(toparse)
  add_to_string = True
  toreturn = ""
  for letter in list_parse:
    if letter == ">":
      add_to_string = True
    elif letter == "<":
      add_to_string = False
    elif add_to_string == True:
      toreturn = toreturn + letter
  return toreturn