# This code is used to set the user email address, which is used to send emails to.
import os

email = input("Enter email address: \n")
with open('projects-03-xufeng-harith-talia-brendan/userEmail.txt','w') as file:
   file.write(email)
