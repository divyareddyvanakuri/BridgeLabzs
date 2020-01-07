username = input("enter username: ")
if len(username)<3:
    print("Ensure username minimum three characters")
else:
    print("Hello {0},How are you?".format(username))