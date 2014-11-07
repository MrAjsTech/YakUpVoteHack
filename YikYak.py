#! /usr/bin/env python3
import API as pk
import requests
import pygeocoder


def main(): 
	print("__________________________________________ \n \n \n Welcome to YikYak upvote Hack");
	geocoder = pygeocoder.Geocoder("AIzaSyAGeW6l17ATMZiNTRExwvfa2iuPA1DvJqM")
	currentlist = []
	
	
	#Code pulled from YikYak.py terminal GUI. Because there is a problem with setting long and lat manually. Trying using google locations
	# If first time using app, ask for preferred location
			
	coordlocation = newLocation(geocoder)
		# If location retrieval fails, ask user for coordinates
	if coordlocation == 0:
		print("Please enter coordinates manually: ")
		currentlatitude = input("Latitude: ")
		currentlongitude = input("Longitude: ")
		coordlocation = pk.Location(currentlatitude, currentlongitude)
	
	#Optional Set Location input
	
	#print("Enter Location data for user upvotes");
	#location set based on long and lat input
	#currentlatitude = input("Latitude: ")
	#currentlongitude = input("Longitude: ")
	
	#temp hard coded in for easy testing
	#coordlocation = pk.Location("29.0355990", "-81.3034150")
	#longitude and latitude is: Lat 29.0355990 Long -81.3034150
	
	#Create 1 yak user that will get list of yaks. From here user selects the number yak that they want to me upvoted i amount of times
	remoteyakker = pk.Yakker(None, coordlocation, True)
	currentlist = remoteyakker.get_yaks()
	read(currentlist)
	print("If you would like to upvote hack enter U and if you would like to downvote to delete enter D")
	choice = input()
	
	if choice.upper() == 'U':
		#getList of yaks and print	
		#input which yak to upvote hack
		yakID=int(input("Please enter the yak number from above: \n"))
		#input yikyak vote amount
		print("Enter the number of Yik Yak upvotes")
		numberOfVotes=int(input());
	
	
		#loop
		for num in range (0,int(numberOfVotes)):
			print(num);
			#creating a new yak user object with location at input
			remoteyakker = pk.Yakker(None, coordlocation, True)
			#Prints unique user id 
			print("User ID: ", remoteyakker.id, "\n")
			#implement upvote
			#yaklist = remoteyakker.get_yaks()
			upvoted = remoteyakker.upvote_yak(currentlist[yakID-1].message_id)		
			if upvoted:
				print("\nUpvote successful :)")
			else:
				print("\nUpvote failed :(\t", end='')
				print (posted.status_code, end='')
				print (" ", end='')
				print (requests.status_codes._codes[posted.status_code][0])
	elif choice.upper() == 'D':
		#input which yak to upvote hack
		yakID=int(input("Please enter the yak number from above: \n"))
		numberOfLikes=int(input("Enter the number of likes the Yak currently has:"))
		for num in range(0,(numberOfLikes+10)):
			remoteyakker = pk.Yakker(None, coordlocation, True)
			print("User ID: ", remoteyakker.id, "\n")
			#yaklist = remoteyakker.get_yaks()
			remoteyakker.downvote_yak(currentlist[yakID-1].message_id)
		
		#code pulled from YikYakTerminal
def newLocation(geocoder, address=""):
	# figure out location latitude and longitude based on address
	if len(address) == 0:
		address = input("Enter college name or address: ")
	try:
		currentlocation = geocoder.geocode(address)
	except:
		print("\nGoogle Geocoding API has reached the limit of queries.\n")
		return 0
		
	coordlocation = 0
	try:
		coordlocation = pk.Location(currentlocation.latitude, currentlocation.longitude)
		
		# Create file if it does not exist and write
		f = open("locationsetting", 'w+')
		coordoutput = str(currentlocation.latitude) + '\n' + str(currentlocation.longitude)
		f.write(coordoutput)
		f.write("\n")
		f.write(address)
		f.close()
	except:
		print("Unable to get location.")
		
	return coordlocation
	
def changeLocation(geocoder, address=""):
	coordlocation = newLocation(geocoder, address)
	if coordlocation == 0:
		print("\nPlease enter coordinates manually: ")
		currentlatitude = input("Latitude: ")
		currentlongitude = input("Longitude: ")
		coordlocation = pk.Location(currentlatitude, currentlongitude)
	return coordlocation
			
#read stream of yaks and print	Pulled from YikYakTerminal 	
def read(yaklist):
	yakNum = 1
	for yak in yaklist:
		# line between yaks
		print ("_" * 93)
		print (yakNum)
		yak.print_yak()
		
		commentNum = 1
		# comments header
		comments = yak.get_comments()
		print ("\n\t\tComments:", end='')
		print (len(comments))
		
		# print all comments separated by dashes
		for comment in comments:
			print ("\t   {0:>4}".format(commentNum), end=' ')
			print ("-" * 77)
			comment.print_comment()
			commentNum += 1
			
		yakNum += 1
		
main()
		
	
	
	
