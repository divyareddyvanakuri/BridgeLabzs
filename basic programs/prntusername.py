import re
username = input("enter username: ")
if len(username)<3:
    print("Ensure username minimum three characters")
else:
    string = "Hello <<username>>,How are you?"
    f = re.sub("<<username>>",username,string)
    print(f)