import os
import pickle
from Account import Account

class AccountManager():
	def __init__(self, filename=''):
		self.__filename = filename
		self.__list = []

	def loadAccount(self):
		if (len(self.__filename) > 0):
			# To make sure open will not throw error/crash
			# Make sure the file exists first by using os.path.exists
			if (os.path.exists(self.__filename)):
				file = open(self.__filename, 'rb')
				if (file):
					# Since we save the Account List/array into file
					# So, when we load the file, it must be an array also
					data = pickle.load(file)
					self.__list = data
					file.close()
		else:
			print('Error! No filename')

	def saveAccount(self):
		if (len(self.__filename) > 0):
			file = open(self.__filename, 'wb')
			if (file):
				# SAVE the Account List/Array into File
				pickle.dump(self.__list, file)
				file.close()
		else:
			print('Error! No filename')

	def addAccount(self, username, password, name):
		print('=> Create new account', username, name)
		# each data of __list is Account instance
		new_account = Account(username, password, name)
		# This append Account class instance into List/Array
		self.__list.append(new_account)
		print('List now is', self.__list)

	def printAccount(self):
		# for index in range(0, len(self.__list)):
		# 	account = self.__list[index]
		# 	print(f'{account.getUsername()} {account.getName()}')		
		for account in self.__list:
			print(f'{account.getUsername()} {account.getName()}')
	
		def deleteAccount(self, username='', name=''):
		for account in self.__list:
			if name == account.getName() or username == account.getUsername():	
				self.__list.remove(account)
				return True
		print('Error! Account not found!')
		return False
	
	def editAccount(self, username, new_password, name):
		for account in self.__list:
			if name == account.getName() and username == account.getUsername():
				account.setAccount(new_password)
				return account
			
				
	def authentication(self, username, password):
		for account in self.__list:
			if (account.checkAuthentication(username, password)):
				return account
		return None
