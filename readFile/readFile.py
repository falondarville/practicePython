# count how many times each name appear in the txt file
with open("read.txt", "r") as open_file:
	names = open_file.read()

names = names.split("\n")

darth_count = names.count("Darth")

lea_count = names.count("Lea")

luke_count = names.count("Luke")

print(f"The name Darth appears {darth_count} times.")
print(f"The name Lea appears {lea_count} times.")
print(f"The name Luke appears {luke_count} times.")