#By Lucas Frias 2021
#Please read.me for license and other info
#iMuffin aims to be a quick, lightweight browser portable to most Linux/Unix systems
try:
  import sys
  import requests
  import os
  import parser
except:
  print ("error (1): install sys, requests, and os modules using pip\n if this problem persists, make sure parser.py is included with your installation.")
#Starting variables
url = "home"
version = 0.1
while True:
  #Bar
  print ("iMuffin - " + url)
  print ("-----------------------------")
  #Main display
  if url == "home":
    print ("iMuffin Home Page")
    print ("Thanks for trying out iMuffin Aplha!")
    print ("You are running version " + str(version))
  elif url == "error":
    print ("Uh Oh\nMalformed request")
  else:
    print (parser.rm_p(wanted.text))
  url = input(">")
  #Pass if the url is equal to home
  if url == "home":
    pass
  else:
    #Try and get the webpage if the user does not go to home
    try:
      wanted = requests.get(url)
    except:
      #Otherwise display the error page. FOr now, we don't really care what the error is.
      print ("error (2): cant get webpage")
      url = "error"