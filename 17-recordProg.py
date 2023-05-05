
db={}
valid_num = ["0","1","2","3","4","5","6","7","8","9"]
global email_exit
email_exit=-1

def main_sector():
    
    print("Main Sector")
    print("------")
    main_option =str(input("Press 1 to Register:\nPress 2 to Login\nPress 3 to Clear Database\nPress 4 Exit:"))
    if main_option == '1':
        registration()
    elif main_option=='2':
        login()
    
    elif main_option == "3" :
        database_delete()

    elif main_option=='4':
        recording_all_data()
        exit(1)
    else:
        print("Invalid Option")
        main_sector()

def registration():

    user_email = email_valid()
    email_get = Email_exit(user_email)

    if email_get!=None:
        print("Email already exit:")
        registration()
    else:
        user_name = input("Enter your username:")
        user_name = userName_valid(user_name)
        user_password = input("Enter your password:")
        user_phone = phone_valid()
        user_age = age_valid()
        

           
                        
            

       
        id = len(db)

        to_insert = {id: {"email": user_email,"u_name":user_name, "password": user_password,"phone":user_phone,"age":user_age}}
        db.update(to_insert)


def login():
    user_found=-1
    
    print("This is login sector")
    l_user_email = input("Enter your email to login:")
    l_user_password = input("Enter your password to login:")


    for i in range(len(db)):
        if db[i]["email"] == l_user_email and db[i]["password"]==l_user_password:

            user_found=i
    if user_found!=-1:
        print("Login Success!")
        user_profile(user_found)
        print("------")
    else:
        print("Not Found ")
        print("------")

def user_profile(user_found):
    print("User Info")
    print("------")
    print("Name:",db[user_found]["u_name"])
    print("Age:" , db[user_found]["age"] , "Years old")
    print("Phone No:",db[user_found]["phone"])

    option = input("Press 1 to Edit Profile::\nPress 2 to exit::")
    if option == "1":
        profile_update(user_found)
    elif option == "2":
        recording_all_data()


def Email_exit(email):

    lenght = len(db)
    for i in range(lenght):
        if db[i]["email"] == email:

            return i

def recording_all_data():
    for i in range(len(db)):
        with open("saveTest.txt" , 'w') as file:
            for i in range(len(db)):

            #write
                file.write(db[i]["email"])
                file.write(" ")
                file.write(db[i]["u_name"])
                file.write(" ")
                file.write(db[i]["password"])
                file.write(" ")
                file.write(str(db[i]["phone"]))
                file.write(" ")
                file.write(str(db[i]["age"]))
                file.write('\n')
def database_delete():
     print("Are you sure you want to clear Database?\nPress Y to continue\nPress N to cancel")
     delete_option = input("Please choose and option::")
     if delete_option == "Y":
         
        
        with open("saveTest.txt" , 'w') as file:
            
            file.truncate(0)
            db.clear()
            print("Database cleared!")
            main_sector()
     elif delete_option == "N":
         main_sector()
     else:
         print("Opreation Invalid Please try again!!")
         main_sector()
    
    
def profile_update(user_found):
    print("-----")
    option = input("Press 1 to change Email:\nPress 2 to change Username:\nPress 3 to change Phone:\nPress 4 to change age:")
    if option == "1":
        change_email = email_valid()
        db[user_found]["email"] = change_email
        print("Email changed!")
        user_profile(user_found)
def userName_valid(username):
    scorted_username = ""
    validName = []
    username = str(username)
    validName = username.split()
    for i in range(len(validName)):
        scorted_username += str(validName[i]) + "_"
    return scorted_username


def email_valid():
    count = 0
    spaceFound = False
    while True:
        user_email = input("Enter your email:")
        for i in user_email:
            if i == " ":
                spaceFound = True
                print("Please enter without spaces")
                break
            
        
        for i in user_email:
            if i == "@" and spaceFound == False:
                
                break
            
            else:
                count +=1
        if count >= len(user_email):
            spaceFound = False
            count = 0
            print("Please enter an email with 'example : @--.com' ")
            pass
        else:
            break
    return user_email
                

def phone_valid():
    count = 0
    spaceFound = False
    while True:
            
            
            user_phone = input("Enter your phone:") 
            for i in user_phone:
                if i == " ":
                    spaceFound = True
                    print("Please enter without spaces")
                    break
            for i in user_phone:
                for x in valid_num:
                    if i == x and count == len(user_phone):
                        break
                    elif i == x:
                        count += 1
                        break
                        
                    else:
                        pass
            if count >= len(user_phone):
                 return user_phone
                 break
                 
            else:
                spaceFound = False
                print("Phone Number must not contain special characters!!")
                pass

def age_valid():
    spaceFound = False
    while True:
            count = 0
            user_age = input("Enter your age:")
            for i in user_age:
                if i == " ":
                    spaceFound = True
                    print("Please enter without spaces")
                    break
            for i in user_age:
                for x in valid_num:
                    if i == x and count == len(user_age):
                        break
                    elif i == x:
                        count += 1
                        break
                        
                    else:
                        pass
            if count >= len(user_age):
                 return user_age
                 break
            else:
                spaceFound = False
                print("User age must not contain special characters!!")
                pass


def loading_all_data():
        index = 0
        total_lines = linecounter()
        
        with open("saveTest.txt" , 'r+') as file:
            lines = file.readlines()
            if total_lines == 0:
                pass
            else:
                for i in range(total_lines):
                    
                    
                    user_info = lines[index]
                    user_info = user_info.split()
                    to_insert = {index :{"email": user_info[0],"u_name":user_info[1], "password": user_info[2],"phone":user_info[3],"age":user_info[4]}}
                        
                    db.update(to_insert)
                    index += 1
                    


def linecounter():
    with open("saveTest.txt" , 'r') as file:
        line_count = 0
        for line in file:
            line_count += 1
        return line_count
            


if __name__ == '__main__':
   open("saveTest.txt" , 'a')
   
   loading_all_data()
   while True:
       main_sector()