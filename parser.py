def rm_p(toparse):
  #Turn into list
  list_parse = list(toparse)
  #We want to add all text not in <>
  #Style and script info will still show, but that is a problem for another time
  add_to_string = True
  #The string to return
  toreturn = ""
  #For all chars in html body
  for letter in list_parse:
    #If within <> then ingnore
    if letter == ">":
      add_to_string = True
    elif letter == "<":
      add_to_string = False
    #Add chars if add to string is true (will ingore > because exception)
    elif add_to_string == True and letter != ">":
      toreturn = toreturn + letter
  return toreturn