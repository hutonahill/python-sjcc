
def delete():
    running = True
    while running == True:
        test = raw_input('Runing This Command Will Deleate ALL Posts, And Is Irreversible. Are You Sure You Want To Do This?(y/n): ')  
        if test != 'n'and test != 'y':
            print "That Is Not A Valid Answer Please Answer 'y' Or 'n'"
        
        elif test == 'y':
            wPosts = open('posts.txt','w')
            wPosts.write('')
            wPosts.close()
            running = False
        
        elif tests == 'n':
            print "Program Aborted."
            running = False

#-------------------------------------------

def recall():
    posts = open('posts.txt')
    posts = posts.read()
    print posts
    
#-------------------------------------------   

def writePost(user,post):
    postFile = open('posts.txt','a')
    x = ' %s: %s\n' %(user,post)
    postFile.write(x)
    postFile.close()

#-------------------------------------------

def loginChecker(username,password):
    userPassword = username+':'+password
    
    userList = open('userTest.txt')
    userList = userList.read()

    if userPassword in userList:
        return True
    else:
        return False
    
#-------------------------------------------

def userCheck(username):
    #checks for a username in login
    if username in lit:
        return True
    else:
        return False
    
#-------------------------------------------

def whichUser(user):
    #returns the number of a user
    import ast
    x = ast.literal_eval(text)
    return x.index(user)

#-------------------------------------------

def userCount():
    #returns the number of users
    x=True
    y=-1
    while x==True:
        y+=1
        raw = open("users.txt")
        raw = raw.read()
        users = raw.split(",")
    
        try:
            z = users[y]
            
        except IndexError:
            x=False
        
        if x==False:
            return y

#-------------------------------------------

def newUserCheck(username):
    #checks for duplicit usernames dureing regitration
    if username in lit:
        return False
    else:
        return True

#-------------------------------------------

def register():
    ### The bulk of the following code was provided by Qi Jing with premition. Thanks. ###
        
        # Register a new user and password
        
        # The userTest.txt file must have this format for each record: user_name:password
        # Also the user name and password cannot contain BLANK and ":".
        
        raw = open("userTest.txt", "a+")
        text = raw.read().split()
        raw.close()
        
        user_list = []
        password_list = []
        new_user_flag = False
        
        # Split each element to user and password and append to the 2 lists
        if len(text) != 0:
            for item in text:
                user_name, password = item.split(":")
                user_list.append(user_name)
                password_list.append(password)
        
        while True:
            user_input = raw_input("Enter User Name ['stop' to end this program]:")
            if user_input.lower() == "stop":
                new_user_flag = False
                print "Program Ended"
                break
            
            new_user_flag = True
            if " " in user_input or ":" in user_input:
                print "Sorry, User Name cannot have BLANK or ':'. Please Re-Enter!"
                continue
            
            if user_input in user_list:
                print "The User Name You Entered already Exists. Please Try A Difrent One"
                continue
            
            while True:
                password_input1 = raw_input("Enter Password ['stop' to end this program]: ")
                
                if password_input1.lower() == "stop":
                    new_user_flag = False
                    print "Program Ended"
                    break
                
                if " " in password_input1 or ":" in  password_input1:
                    print "Sorry, Password cannot have BLANK or ':'. Please Re-Enter!"
                    continue
                
                password_input2 = raw_input("Re-enter Password: ")
                if password_input1 != password_input2:
                    print "Sorry the Password You Entered Doesn't Match. Please Try Again!"
                    continue
                
                break
                
            # We are all set and need to exit the loop
            break
        
        if new_user_flag == True:     
            print "Good job. Your new user name is registered."
             # We need to append the new user to the file userTest.txt
            string = "{" + "'" + user_input+"':'"+password_input1+"'}\n"
            raw = open("userTest.txt", "a+")
            raw.write(string)
            raw.close()


    
    

#-------------------------------------------

def startProgram():
    #runs the program
    #pre recs
    import ast
    
    class InputError(ValueError):
        pass
    
    raw = open("userTest.txt")
    text = raw.read()
    lit = text
    users = text.split(",")
    
    login = False
    
    print 'Welcome to Python Chat.' 
    
    running = True
    
    #loop starts
    while running == True:
        running = True
        
        #request a command
        com = raw_input("Please Input A Command: ")
        com = str(com.lower())
        
        
        ##test the command
        #login command
        if com == 'log in':
            username = raw_input("Input Your Username: ")
            password = raw_input('Please Enter Your Password: ')
            
            login = loginChecker(username,password)
            if login == True:
                print 'You Are Now Loged In'
            else:
                print 'an error has ocured '
            print ''
            
        #Register new user command
        elif com == 'register':
            print "in register"
            register()
            print ''
            #running = False
        
        #help command
        elif com == 'help':
            print 'help  ==>  you are here.  you should know what this does.'
            print 'log in  ==>  this command allows you to log in to Python Chat with an existing username and password'
            print 'register  ==>  this command allows you to create a username and password'
            print 'post  ==>  this allows you to post.'
            print 'recall  ==>  this allows you to call up old posts'
            print 'stop  ==>  this stops the program'
            print ''
            #running = False
            
        #post command
        elif com == 'post':
            if login == True:
                post = raw_input('Please Type Your Post(you may not include "\\n")')
                if '\n' in post:
                    raise InputError('you may not user \\n')
                writePost(username,post)
                print'Post Posted'
                print ''
                #running = False
            else:
                print 'Sorry, You Must Log In To Acses This Feature'
                print ''
                #running = False
                
        #recall command
        elif com == 'recall':
            if login == True:
                recall()
                print''
                #running = False
            else:
                print 'Sorry, You Must Log In To Acses This Feature'
                print ''
                #running = False
        elif com == 'stop':
            running = False
            print ''
            
        #delete command(admin user only)
        elif com == 'delete':
            if login == True:
                if username == 'Admin':
                    delete()
                    print ''
                else:
                    print 'You Must Be The Admin To Run This Command'
                
                #running = False
            else:
                print 'Sorry, You Must Log In To Acses This Feature'
                print ''
        
        #check for invaliad commands
        else:
            print 'You Have Not Entered An Invalled Command.  Please try Again.  You May Type "help" For Help.'
            print ''
            #running = False
    
    print 'Program Has Stoped'