import time
import math
import ast
import os
from replit import db
Idkey = os.environ["User IDs"]
Datakey = os.environ["User data"]
"""
0. Usernames
1. Passwords
2. ...
"""

class user:
  def __init__(self, Username, Pass):
    self.username = Username
    self.password = Pass




def outputfile(array: []):
  for i in range(len(array)):
      print(f"{i+1}. {array[i][0]}, from {days_from(i)} days ago")
def get_days(time_since):
  return math.pow(time_since, 2) + time_since / 2


def is_day(time_since):
  a = 0.5
  b = 0.5
  c = -1 * time_since
  days = (-1 * b) + math.sqrt((b * b) - (4 * a * c))
  return days == math.floor(days)


def days_from(revision_set):
  return day_from_1970(time.time()) - day_from_1970(file[revision_set][1])


def day_from_1970(unix_time):
  return math.floor(unix_time / 86400)

def set_storage_to_file():
  global file
  storage = open("Storage.txt", "w")
  storage.write(str(file))
  storage.close()


while True:
  action = input("(c for create account) Username:")
  if action == "c":
    myuser = user(None, None)
    end = 0
    while end == 0:
      k = input("New account: username: ")
      fast = set(db[Datakey][0])
      works = (k.lower() != "c") and ( not( k in fast))
      if works:
        print(f"Username: {k}")
        end = 1
    myuser.username = k
    end = 0
    while end == 0:
      k = input("Password (At least 6 charecters): ")
      if len(k) > 6:
        print(f"Password: {k}")
        end = 0
    myuser.password = k
  else:
    end = 0
    myuser = user(None, None)
    while end == 0:
      k = input("Username: ")
      fast = set(db[datakey][0])
      if k in fast:
        end = 1
    end = 0
    myuser.username = k
    while end == 0:
      k = input("Password: ")
      if fast.index(myuser.username) == k:
        print("Access granted.")
        end = 1
      
      
f = open("Storage.txt", "rt")
try:
  file = ast.literal_eval(f.read())
except SyntaxError:
  f.write("[]")
  file = []
  set_storage_to_file()
f.close()
restore = ["Base restore!", 0]

while True:
  Action = input("Command: ").lower()
  day = day_from_1970(time.time())
  if Action == "today":
    j = 0
    for i in file:
      day_from = days_from(j)
      if is_day(day_from):
        print(f"\"{i[0]}\" It has been {day_from} days.")
      j += 1
    print("Done!")
  elif Action == "new":
    f = open("Storage.txt", "w")
    new_add = [input("Revision set name?"), time.time()]
    print(file)
    file.append(new_add)
    f.write(str(file))
    print(new_add)
    f.close()
    f = open("Storage.txt", "rt")
    file = ast.literal_eval(f.read())
    f.close()
  elif Action == "test":
    outputfile(file)
  elif Action == "edit":
    print("Edit which?")
    outputfile(file)
    end = 0
    while end == 0:
      try:
        j = int(input("So which one: ")) - 1
        end = 1
      except ValueError:
        pass
    if input("Change time? (yes) or Change name (no)").lower()[0] == "y":
      end = 0
      while end == 0:
        try:
          k = int(input(f"Set {file[j][0]} to how many days from now? "))
          end = 1
        except ValueError:
          pass

      file[j][1] = k * 86400
    else:
      k = input(f"Rename {file[j][0]} to what? ")
      file[j][0] = k
    set_storage_to_file()
  elif Action == "remove":
    print("Remove which?")
    outputfile(file)
    end = 0
    while end == 0:
      try:
        j = int(input("So which one: ")) - 1
        end = 1
      except ValueError:
        pass
    print(f"Are you sure that you want to delete {file[j][0]}, from {days_from(j)} days ago?")
    k = input("y/n ")
    if k[0].lower() == "y":
      restore = file[j]
      del file[j]
      print(f"{restore} is restore.")
    set_storage_to_file()
  elif Action == "restore":
    k = input(f"Add back {restore}?")
    if k[0].lower() == "y":
      file.append(restore)
      set_storage_to_file()
  else:
    print("Options are today, new, test, edit, remove, restore")
    outputfile(file)