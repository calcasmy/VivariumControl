from datetime import date, datetime

class DTOperations:
	"""Date Time related operations to keep it consistant across the application"""

	def todayDate() -> str:
		"""Returns today's data as a string value in yyyy-mm-dd format"""
		_date = date.today().strftime('%Y-%m-%d')
		return _date

	def todayDtTm() -> datetime:
		"""Returns today's date as a datetime object with out milliseconds"""
		_datetime = datetime.now().replace(microsecond=0)
		return _datetime

	def convertStrToDt(_date: str) -> date:
		"""Convert string value to date object 
		The string value should be in yyyy-mm-dd format"""
		if _date:
			_date = datetime.strptime(_date, '%Y-%m-%d').date()
		else:
			print('enter a date to be converted to DateTime object')
		return _date
	
	def convertStrToDtTm(_date: str, _time: str) -> datetime:
		"""Convert string value to datetime object
		The string value should be in yyyy-mm-dd hh:mm:ss"""

		print("To be implemented")

	def convertDtToStr(_date: date) -> str:
		"""Convert date object to string value
		The returned string value will be in yyyy-mm-dd format"""
		_date = date.strftime(_date, '%Y-%m-%d')
		return _date
	
	def convertTimeto24(_time: str) -> str:
		if(_time != ""):
			_time = datetime.strptime(_time, "%I:%M %p")
			_time = datetime.strftime(_time, "%H:%M:%S")
			return (_time)
		else:
			return('')

# DTOperations.convertStrToDtTm("2023-08-27 1:15 PM")
# DTOperations.todayDtTm()
	#Other Formats
	# dd/mm/YY
	# d1 = today.strftime("%d/%m/%Y")
	# print("d1 =", d1)

	# Textual month, day and year	
	# d2 = today.strftime("%B %d, %Y")
	# print("d2 =", d2)

	# mm/dd/y
	# d3 = today.strftime("%m/%d/%y")
	# print("d3 =", d3)

	# Month abbreviation, day and year	
	# d4 = today.strftime("%b-%d-%Y")
	# print("d4 =", d4)

	# object containing current date and time
	# now = datetime.now()

	# print("now =", now)

	# # dd/mm/YY H:M:S
	# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	# print("date and time =", dt_string)

	#Addtional Notes from ___https://www.nbshare.io/notebook/510557327/Strftime-and-Strptime-In-Python/___

	# Strftime and Strptime In Python
	# In this post, we will learn about strftime() and strptime() methods from Python datetime package.

	# Python Strftime Format
	# The strftime converts date object to a string date.

	# The syntax of strftime() method is...

	# dateobject.strftime(format)

	# Where format is the desired format of date string that user wants. Format is built using codes shown in the table below...

	# Code	Meaning
	# %a	Weekday as Sun, Mon
	# %A	Weekday as full name as Sunday, Monday
	# %w	Weekday as decimal no as 0,1,2...
	# %d	Day of month as 01,02
	# %b	Months as Jan, Feb
	# %B	Months as January, February
	# %m	Months as 01,02
	# %y	Year without century as 11,12,13
	# %Y	Year with century 2011,2012
	# %H	24 Hours clock from 00 to 23
	# %I	12 Hours clock from 01 to 12
	# %p	AM, PM
	# %M	Minutes from 00 to 59
	# %S	Seconds from 00 to 59
	# %f	Microseconds 6 decimal numbers
	# Datetime To String Python using strftime()
	# Example: Convert current time to date string...

	# In [8]:
	# import datetime 
	# from datetime import datetime
	# now = datetime.now()
	# print(now)
	# 2021-03-07 23:24:11.192196
	# Let us convert the above datetime object to datetime string now.

	# In [2]:
	# now.strftime("%Y-%m-%d %H:%M:%S")
	# Out[2]:
	# '2021-03-07 23:16:41'
	# If you want to print month as locale’s abbreviated name, replace %m with %b as shown below...

	# In [3]:
	# now.strftime("%Y-%b-%d %H:%M:%S")
	# Out[3]:
	# '2021-Mar-07 23:16:41'
	# Another example...

	# In [4]:
	# now.strftime("%Y/%b/%A %H:%M:%S")
	# Out[4]:
	# '2021/Mar/Sunday 23:16:41'
	# Date To String Python using strftime()
	# Date to string is quite similar to datetime to string Python conversion.

	# Example: Convert current date object to Python date string.

	# In [5]:
	# today = datetime.today()
	# print(today)
	# 2021-03-07 23:22:15.341074
	# Let us convert the above date object to Python date string using strftime().

	# In [6]:
	# today.strftime("%Y-%m-%d %H:%M:%S")
	# Out[6]:
	# '2021-03-07 23:22:15'
	# Python Strftime Milliseconds
	# To get a date string with milliseconds, use %f format code at the end as shown below...

	# In [7]:
	# today = datetime.today()
	# today.strftime("%Y-%m-%d %H:%M:%S.%f")
	# Out[7]:
	# '2021-03-07 23:23:50.851344'
	# Python Strptime Format
	# Strptime python is used to convert string to datetime object.

	# strptime(date_string, format)

	# example:

	# strptime("9/23/20", "%d/%m/%y")

	# Note - format "%d/%m/%y" represents the the corresponding "9/23/20" format. The output of the above command will be a Python datetime object.

	# The format is constructed using pre-defined codes. There are many codes to choose from. The most important ones are listed below.

	# Code	Meaning
	# %a	Weekday as Sun, Mon
	# %A	Weekday as full name as Sunday, Monday
	# %w	Weekday as decimal no as 0,1,2...
	# %d	Day of month as 01,02
	# %b	Months as Jan, Feb
	# %B	Months as January, February
	# %m	Months as 01,02
	# %y	Year without century as 11,12,13
	# %Y	Year with century 2011,2012
	# %H	24 Hours clock from 00 to 23
	# %I	12 Hours clock from 01 to 12
	# %p	AM, PM
	# %M	Minutes from 00 to 59
	# %S	Seconds from 00 to 59
	# %f	Microseconds 6 decimal numbers
	# Python Datetime Strptime
	# Example: Convert date string to Python datetime object.

	# In [9]:
	# import datetime
	# datetime.datetime.strptime("09/23/2030 8:28","%m/%d/%Y %H:%M")
	# Out[9]:
	# datetime.datetime(2030, 9, 23, 8, 28)