#By Lucas Frias 2021
#Please read.me for license and other info
#iMuffin aims to be a quick, lightweight browser portable to most Linux/Unix systems
###############
### Startup ###
###############

try:
  import sys
  import requests
  import os
  import parser
except:
  print ("error (1): install sys, requests, and os modules using pip\n if this problem persists, make sure parser.py is included with your installation.")
#Starting variables
url = "home"
version = 0.2



#############
## Main #####
############
while True:
  #Bar
  print ("iMuffin - " + url)
  print ("-----------------------------")
  #Main display
  #This is home, which will display some home starting text


#################
###### Pages ####
#################

  if url == "home":
    print ("iMuffin Home Page")
    print ("Thanks for trying out iMuffin Aplha!")
    print ("You are running version " + str(version))
  #A failure page if things happen to go wrong loading the URL
  elif url == "error":
    print ("Uh Oh\nMalformed request")
    #Try and display a status code, otherwise display a "no response message"
    try:
      print ("Response: " + wanted.status_code)
    except:
      print ("No Response Sent. Is it a valid URL?")


#########################
### Request Handling ###
########################

  else:
    print (parser.rm_p(wanted.text))
  url = input(">")
  #Pass if the url is equal to home(the page render will render this)
  if url == "home":
    pass
  else:
    #Try and get the webpage if the user does not go to home
    try:
      wanted = requests.get(url)
    except:
      #Otherwise display the error page. For now, we don't really care what the error is. We set this as the url so the web render does not have to deal with an empty object
      url = "error"