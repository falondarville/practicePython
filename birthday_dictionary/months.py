# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.
import json
from collections import Counter

with open("info.json", "r") as f:
    info = json.load(f)

# print the months, which will be added to a list
for each in info["birthdays"]:
	birthday_month = each["month"]
	print(birthday_month)
