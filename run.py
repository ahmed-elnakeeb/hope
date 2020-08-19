import os,sys,time,atexit
from db import mysqlite
from desgin import fig
def exit_handler():
    clear()
    print ('My application is ending!')
    time.sleep(1)
    clear()
def  clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    while (True):
        clear()
        print(fig.write("main",fontNumber=0,color="cyan"))
        print("1- log in")
        print("2- register")
        print("3- exit")
        myinput=input()
        if myinput=="1":
            login()
        elif myinput=="2":
            register()
        elif myinput=="3":
            clear()
            sys.exit()
        else:
            print("wrong entery")
            time.sleep(.5)
def login():
    clear()
    print(fig.write("log in",fontNumber=0,color="magenta"))
    print("user name")
    username=input()
    print("password")
    password=input()
    try:
        users=dblogin(username,password)
        if len(users)==0:
            print("wrong user name or password")
            time.sleep(1)
        else:
   
            print("welcome")
            time.sleep(2)
            controle(username,password)
    except Exception as e :
        print("some thing went wrong ")
        print(e)
        time.sleep(.5)
        main()
def dblogin(username,password):
    sql=mysqlite("users.db")
    rows=sql.rows("select * from users where username='"+ username+"' and userPassword='"+password+"'")
    sql.conn.close()
    return (rows)
def chick(username)->bool:
    sql=mysqlite("users.db")
    rows=sql.rows("select * from users where username='"+ username+"'")
    sql.conn.close()
    return (len(rows)>0)
def controle(username,password):
    username=username
    password=password
    clear()
    print(fig.write("controle panel",fontNumber=0,color="green"))
    print("1- change user name")
    print("2- change user password")
    print("3- user info")
    print("4- logout")
    print("5- exit")
    myin=input()
    if myin=="1":
        print ("new user name is ")
        new=input()
        if chick(new):
            print("user allredy exists")
            time.sleep(1)
            controle(username,password)
        else:
            print("user name avilable")
            mysqlite.qurey("update users set userName='"+new+"' where userName='"+username+"'")
            username=new
            time.sleep(3)
            controle(username,password)
    elif myin=="2":
        controle(username,password)
    elif myin=="3":
        print("user name :",username,"\n","password :",password,"\n press any key to continue")
        input()
        time.sleep(1)
        controle(username,password)
    elif myin=="4":
        main()
    elif myin=="5":
        sys.exit()
    else:
        print("what?!!!")
        time.sleep(1)
        controle(username,password)
def register():
    clear()
    print(fig.write("register",fontNumber=0,color="red"))
    print("user name")
    username=input()
    if chick(username):
        print("user allredy exists")
        time.sleep(1)
        register()
    else:
        print("user name avilable")
    print("new password")
    password=input()
    sql=mysqlite("users.db")
    try:
        sql.qurey("insert into users (userName,userPassword) VALUES('"+username+"','"+password+"')")
        sql.conn.commit()
        clear()
        print(fig.write("congratulations",fontNumber=0,color="bright_magenta"))
        time.sleep(3)
        main()
    except:
        print("cant add user ")
atexit.register(exit_handler)
main()