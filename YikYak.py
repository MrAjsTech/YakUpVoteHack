#! /usr/bin/env python3
import API as pk
import requests

def main(): 
	print("__________________________________________ \n \n \n Welcome to YikYak upvote Hack");
	
	currentlist = []
	
	
	#Optional Set Location input
	
	#print("Enter Location data for user upvotes");
	#location set based on long and lat input
	#currentlatitude = input("Latitude: ")
	#currentlongitude = input("Longitude: ")
	
	#temp hard coded in for easy testing
	coordlocation = pk.Location("29.0355990", "-81.3034150")
	#Stetson longitude and latitude is: Lat 29.0355990 Long -81.3034150
	
	#Create 1 yak user that will get list of yaks. From here user selects the number yak that they want to me upvoted i amount of times
	remoteyakker = pk.Yakker(None, coordlocation, True)
	
	
	#getList of yaks and print
	currentlist = remoteyakker.get_yaks()
	read(currentlist)
	
	
	
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
		yaklist = remoteyakker.get_yaks()
		upvoted = remoteyakker.upvote_yak(currentlist[yakID-1].message_id)
		
		
#read stream of yaks and print		
def read(yaklist):
	yakNum = 1
	commentNum = 1
	for yak in yaklist:
		# line between yaks
		print ("_" * 93)
		print (yakNum)
		yak.print_yak()
		
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