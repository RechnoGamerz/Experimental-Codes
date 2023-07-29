import subprocess
def register():
    db=open("database.txt", "r")
    Username = input("create username:")
    password = input("create password:")
    password1 = input("confirm password:")
    d = []
    f = []
    for i in db:
        a,b= i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    if password != password1:
        print("passwords dont match, Pls restart")
        register()
    else:
         if len(password)<=6:
             print("Password is too short, Pls restart")
             register()
         elif Username in d:
             print("Username already exists!")
             register()
         else:
             db = open("database.txt", "a")
             db.write(Username+", "+password+"\n")
             print("Success!")


def access():
    db = open("database.txt", "r")
    Username = input("Enter your username:")
    password = input("Enter your password:")

    if not len(Username or password)<1:
        d = []
        f = []
        for i in db:
          a,b= i.split(", ")
          b = b.strip()
          d.append(a)
          f.append(b)
        data = dict(zip(d, f)) 

        try:
            if data[Username]:
                try:
                    if password == data[Username]:
                        print("Login Success")
                        print("Hi,",Username)

                    else:
                        print("Password or Username is incorrect!")
                except:
                    print("Incorrect password of the Username!")
            else:
                print("Username doesn't exists!")
        except:
            print("login error?")
def home(option=None):
    option = input("Login(1) | Signup(2)")
    if option == "1":
        access()
    elif option == "2":
        register()
    else:
        print("Enter 1 or 2 only.")
home()