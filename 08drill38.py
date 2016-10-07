# python 3.5
# author: tyler corum
# purpose: the tech academy python course drill 38 of 63

# TOC:
# 1. load sql module, create db in mem, create cursor
# 2. create table add data
# 3. update data
# 4. fetch data, print to display 
# 5. where do these come into play?


# 1. load sql module, create db in mem, create cursor
import sqlite3

connection = sqlite3.connect(':memory:')

c = connection.cursor()


# 2. create table add data
c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")

peopleValues = (
  ('Jean-Baptiste Zorg', 'Human', 122),
  ('Korben Dallas', 'Meat Popsicle', 100),
  ('Ak\'not', 'Mangalore', -5))

c.executemany("INSERT INTO Roster VALUES(?,?,?)", peopleValues)


# 3. update data
c.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")
connection.commit()

# 4. fetch data, print to display 
c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
while True:
  row = c.fetchone()
  if row is None:
    break
  print(row)
  connection.close()
# ///one way to print the SQL data:
# for row in c.fetchall():
#     print(row)
#
# ///another way to print SQL data:
# while True:
#   row = c.fetchone()
#   if row is None:
#     break
#   print(row)


# 5. where do these come into play?
# connection.commit()
# connection.close()