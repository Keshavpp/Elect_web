import sqlite3,time,sys

def login():
	while True:
		username= input("Please enter the username: ")
		password= input("Please enter your password: ")
		with sqlite3.connect("names.db") as db:
			cursor=db.cursor()
		find_user=("SELECT * FROM user WHERE username= ? AND password= ?")
		cursor.execute(find_user,[(username),(password)])
		result=cursor.fetchall()

		if result:
			for i in result:
				print("WELCOME "+i[1])
			break
		else:
			print("Incorret usernamea or password ")
			again=input("DO you wanna try again(Y/N)?")
			if again.lower()== "n":
				print("Good bye")
				time.sleep(1)
				#return("exit")
				break

def newUser():
	found=0
	while found==0:
		username =input("Please Enter a username: ")
		with sqlite3.connect("names.db") as db:
			cursor=db.cursor()
		findUser=("SELECT * FROM user WHERE username= ?")
		cursor.execute(findUser,[(username)])
		if cursor.fetchall():
			print("Username already taken! Please try again")
		else:
			found=1
	name=input("Please enter ur name:")
	password=input("Please enter ur password:")
	password1=input("Please re-enter ur password: ")
	while password!=password1:
		print("Passwords do not match")
		password=input("Please enter ur password:")
		password1=input("Please re-enter ur password:")
	insertData = '''INSERT INTO user(username,name,password)
	VALUES(?,?,?) 
	'''
	cursor.execute(insertData,[(username),(name),(password)])
	db.commit()


def menu():
	while True:
		print("WELCOME TO MY PAGE")
		menu =('''
			1-Create new user
			2-login to page
			3-Exit\n
			''')
		userchoice=input(menu)
		if userchoice=='1':
			newUser()
		elif userchoice=='2':
			login()
		elif userchoice=='3':
			print("VISIT AGAIN")
			sys,exit()
		else:
			print("ENTER ONLY FROM THE OPTIONS")


menu()