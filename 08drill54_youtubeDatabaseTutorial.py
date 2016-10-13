#/// part 1
# import sqlite3

# conn = sqlite3.connect('tutorial.db')
# c = conn.cursor()

# def create_table():
# 	c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

# def data_entry():
# 	c.execute("INSERT INTO stuffToPlot VALUES(11515, '2016-01-01', 'Python', 5)")
# 	conn.commit()
# 	c.close()
# 	conn.close()

# create_table()
# data_entry()




# /// part 2
# import sqlite3
# import time
# import datetime
# import random

# conn = sqlite3.connect('tutorial.db')
# c = conn.cursor()

# def create_table():
# 	c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

# def data_entry():
# 	c.execute("INSERT INTO stuffToPlot VALUES(11515, '2016-01-01', 'Python', 5)")
# 	conn.commit()
# 	c.close()
# 	conn.close()


# def dynamic_data_entry():
# 	unix = time.time()
# 	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
# 	keyword = 'Python'
# 	value = random.randrange(0,10)
# 	c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?,?,?,?)",
# 		(unix, date, keyword, value)) #MySQL will use %s
# 	conn.commit()


# create_table()

# for i in range(10):
# 	dynamic_data_entry()
# 	time.sleep(1)
# c.close()
# conn.close()



# data_entry()







#/// part 3
# import sqlite3
# import time
# import datetime
# import random

# conn = sqlite3.connect('tutorial.db')
# c = conn.cursor()

# def create_table():
# 	c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

# def data_entry():
# 	c.execute("INSERT INTO stuffToPlot VALUES(11515, '2016-01-01', 'Python', 5)")
# 	conn.commit()
# 	c.close()
# 	conn.close()


# def dynamic_data_entry():
# 	unix = time.time()
# 	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
# 	keyword = 'Python'
# 	value = random.randrange(0,10)
# 	c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?,?,?,?)",
# 		(unix, date, keyword, value)) #MySQL will use %s
# 	conn.commit()


# # def read_from_db():
# # 	c.execute("SELECT * FROM stuffToPlot")
# # 	# data = c.fetchall()
# # 	# print(data)
# # 	for row in c.fetchall():
# # 		print(row)
# def read_from_db():
# 	c.execute("SELECT keyword, unix, value, datestamp FROM stuffToPlot WHERE unix > 1476295940")
# 	# data = c.fetchall()
# 	# print(data)
# 	for row in c.fetchall():
# 		print(row)

# # create_table()

# # for i in range(10):
# # 	dynamic_data_entry()
# # 	time.sleep(1)

# read_from_db()
# c.close()
# conn.close()





#/// part 4
import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
	c.execute("INSERT INTO stuffToPlot VALUES(11515, '2016-01-01', 'Python', 5)")
	conn.commit()
	c.close()
	conn.close()


def dynamic_data_entry():
	unix = time.time()
	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	keyword = 'Python'
	value = random.randrange(0,10)
	c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?,?,?,?)",
		(unix, date, keyword, value)) #MySQL will use %s
	conn.commit()


# def read_from_db():
# 	c.execute("SELECT * FROM stuffToPlot")
# 	# data = c.fetchall()
# 	# print(data)
# 	for row in c.fetchall():
# 		print(row)
def read_from_db():
	c.execute("SELECT keyword, unix, value, datestamp FROM stuffToPlot WHERE unix > 1476295940")
	# data = c.fetchall()
	# print(data)
	for row in c.fetchall():
		print(row)



def graph_data():
	c.execute("SELECT datestamp, value FROM stuffToPlot")
	dates = []
	values = []
	for row in c.fetchall():
		print(row[0])
		print(datetime.datetime.fromtimestamp(row[0]))
		#dates.append()















# create_table()

# for i in range(10):
# 	dynamic_data_entry()
# 	time.sleep(1)

# read_from_db()
graph_data()
c.close()
conn.close()
