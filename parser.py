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
def link_list(possiblelinkbody):
  #This was a very complex function to write, and even I do not fully understand how it works. But it does (somewhat) and I am here to document it.
  #First, get a list of functions
  allchar = list(possiblelinkbody)
  #Create a list to add all text to.
  text_list = []
  #PPossible href is True when < appears, possibly conveying that <> contains a link
  possible_href = False
  #Where it is followed by an a, which leads it to assume it to be a link. It could not be, but 9/10 times, this will display a link.
  is_href = False
  #For all charecters in the body
  for char in allchar:
    #If the letter is a(processes before removing possible href)
    if char == "a" and possible_href == True:
      is_href = True
    #Only scans one line looking for a, shuts down if it is not on the second one.
    if possible_href == True:
      possible_href = False
    #If the charecter is equal to <, then flag it as a possible url.
    if char == "<":
      possible_href = True
    #If the line ends, stop.
    if char == ">" and is_href == True:
      is_href = False
    #Otherwise display the link for the person.
    if is_href == True:
      text_list.append(char)
  str1 = ""
  return str1.join(text_list)