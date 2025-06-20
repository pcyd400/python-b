import account_module as am 
def main():
    while True:
        print("1) Create account")
        print("2) Login")
        print("3) forgot  password")
        print("4) Exit")
        choice = input("please enter the respective number: ")
        if choice == '1':
            am.register()
        elif choice == '2':
            am.login()
        elif choice == '3':
            am.forgot_password()
        elif choice == '4':
            print("thanks for using our app")
            break 
        else:
            print("invalid input")
main()