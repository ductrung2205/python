import re
text = input("Enter: ")
result = re.sub("[A-Za-z0-9]+", '', text)
if len(result) == 0:
    print("Success")
else:
    print("Failure")