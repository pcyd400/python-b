#create a function that allows the user to register
users = {}
notes = []
def register():
    '''function to reguster the new user'''
    name = input("enter your name: ").strip()
    while True:
        if  name not in users:
            users['name'] = name
            address = input("please enter your address: ")
            phone = int(input("please enter your phone number: "))
            numbers= ['1','2','3','4','5','6','7','8','9','0'] 
            special_chars =['!','@','#','$','%','&'] 
            in_number = False 
            in_special = False
            password = input("please enter your password: ")
            pw_list = list(password)
            for char in pw_list:
                if char in numbers:
                    in_number =True
                if char  in special_chars:
                    in_special = True 
            if in_number and in_special:
                c_password = input("please confirm your password: ")
                if password == c_password:
                    users[name] = {'address':address,'phone':phone, 'password':password}
                    print("Done!!!")
                    break
                else:
                    print("password doesnt match")
            else:
                print("password should have combination of special characters and numbers")
        else:
            choice  =  input("user already exists do you want to login (y/n)? ")
            if choice.lower() == 'y':
                login()
            else:
                print("THANKS!!")
                break
#login 
def login():
    '''allows the user to login'''
    name =  input("please enter your name: ")
    while True:
        if name in users:
            password  = input("please enter the password: ")
            if users[name]['password'] == password:
                print(f"WELCOME {name}")
                print("a) CREATE NOTES")
                print("b) SEE NOTES")
                print("c) DELETE NOTES")
                print("d) logout")
                select =  input("Select the action: ")
                if select.lower() == 'a':
                     create_note(name) 
                elif select.lower() == 'b':
                     show_notes(name)
                elif select.lower() == 'c':
                     del_notes(name)
                else:
                    print("----THANKS-----")
                    break
            else:
                print("password didn't match")
        else: 
            print("no user found!!")
#forgot password 
def forgot_password():
        '''allows the user to reset the password'''
        name =  input("please enter your name: ")
        if  name in users:
                phone =int(input("please enter your phone number: "))
        else:
                print('User dosent exist')
        while True:
                if users[name]['phone'] == phone:
                    n_pwd = input("please enter your new password: ")
                    c_pwd = input("please confirm your password : ")
                    if n_pwd == c_pwd:
                        users[name]['password'] = n_pwd
                        print("Your new password  has been set successfully")
                        break
                    else:
                        print("password new password and confirn password didnt matched")
                else:
                    print("phone number dosent match")
##let the  user  create the notes
def create_note(name):
     '''allows the user to create the reminders and notes'''
     active = True
     while active: 
        print("___REMINDER__PRESS Q TO QUIT ANY TIME___")
        reminder = input("please enter the reminder you want to save: ")
        if reminder.lower() == 'q':
             print("Exiting  from the reminder app")
             users[name]['notes'] = notes
             active = False
        else:
             notes.append(reminder)
#let the user see the notes
def show_notes(name):
     '''shows  the notes to the user'''
     while True:
        print("____HERE ARE YOUR NOTES________")
        for note in users[name]['notes']:
            print(f"{notes.index(note)}: {note}")
        choice = input("do you want to close the note? y/n")
        if choice.lower() == 'y':
             break
##allow the user to delete the notes
def del_notes(name):
    '''deletes the selected reminder'''
    print("---SELECT THE NOTE YOU WANT TO DELETE press q to exit---")
    for note in  users[name]['notes']:
        print(f"{notes.index(note)}: {note}")
    while True:
        delt = input("select the reminder number you want to delete: ")
        if delt.lower() == 'q':
            print("THANKS")
            break
        index = int(delt)
        del users[name]['notes'][index]
        print("the note has been deleted successfully!!")
        
          
