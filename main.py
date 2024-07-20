import json
import os
import time
import json
import requests
import openai
from datetime import date

openai.api_key = "" # Openai api key goes here

# I coded this in nano editor inside termux
# Why?
# Because of the war in my country
# russians desroyed most of power generation in Ukraine
# Our cities are getting bombed everyday and we have lights for 3-12 hours out of 24 hours
# Please, help us if you can, donate to our charities
# This is an unfortunate reality that I have to live in
# Sorry for my bad English and code.


path = "//storage//emulated//0//Android-Intelligence//" # Path to cloned git repo
pathi = path + "input.txt" # Path to input file
patho = path + "output.txt" # Path to output file
context = path + "context.txt" # Path to context file
trigger = "" # Link to macrodroid trigger
lastActivePath = path + "lastActive.txt"


print("Working") # Just to see if program is working
#print("Current directory" + os. getcwd())
while True:
	# Check if input file exists
	if os.path.isfile((pathi)):
		# if exists do this:
		today = date.today() # get time now
		print(today.strftime('%d/%m'))
		f = open(lastActivePath, "r") # Read when macros was activated last time
		lastActive = f.read()
		f.close()
		lastActive = lastActive.strip()
		# If it is not today and variable is not "" then clear context.txt
		if lastActive != today.strftime('%d/%m'):
			if lastActive != "":
				open(context, 'w').close() # Clear context of GPT
				print("Deleted context")

		# If it is "" then write tosays dqy and month
		if lastActive == "":
			f = open(lastActivePath, "w") # Write >
			f.write(today.strftime('%d/%m'))
			f.close()
			print("Wrote current date")
		f = open(lastActivePath, "w")
		f.write(today.strftime('%d/%m'))
		f.close()
		f = open(pathi, "r") # Read input
		text = f.read()
		f.close()
		print(text)
		c = open(context, "r") # Read context for GPT
		contextText = c.read()
		c.close()
		completion = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "assistant", "content": str(contextText)},
        {"role": "user", "content": str(text)},
    ],
)
		response = completion.choices[0].message.content # Extract text from response
		print(response)
		tokens = completion.usage # Get number of tokens used
		print(str(tokens))
		c = open(context, "a") # Open context file for appending text
		c.write("Human: " + text + "\n") # Appending ehat human said to GPT
		c.write("GPT: " + response + "\n") # Appending GPT's reply
		c.close()
		f = open(patho, "w") # Write GPT's answer to output file
		f.write(response)
		f.close()
		requests.get(trigger) # Set trigger for macrodroid
		time.sleep(3) # IMPORTANT delay is to prevent second request from happening
	time.sleep(1) # Delay between checks if input file exists
