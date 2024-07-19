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
trigger = "" # Link to macrodroid trigger goes here https://
lastActivePath = path + "lastActive.txt" # Path to file with information when macros last used

def delete_first_ten_lines(filename):
    # Read the contents of the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Write all lines except the first ten back to the file
    with open(filename, 'w') as file:
        file.writelines(lines[20:])


print("Working") # Just to see if program is working

while True:
	# Check if input file exists
	if os.path.isfile((pathi)):
		# if exists do this:
		today = date.today() # get time now
		print(today.strftime('%d/%m')) # Print day/month
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
			f = open(lastActivePath, "w") # Write todays date if there is none in the file
			f.write(today.strftime('%d/%m'))
			f.close()
			print("Wrote current date")
		f = open(lastActivePath, "w") # If everything is okay write today
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
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "assistant", "content": str(contextText)},
        {"role": "user", "content": str(text)},
    ],
)
		response = completion.choices[0].message.content # Extract text from response
		print(response)
		tokens = completion.usage # Get number of tokens used
		print(str(tokens))
		#Auto deletion of context when it is too much
		if tokens.total_tokens >= 3500:
			delete_first_ten_lines(context)
			print("Emergency deletion of context to prevent error")
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
