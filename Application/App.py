class NLPApp:
    def __init__(self):
        self.__database = {}
        self.__first_menu()

    def __first_menu(self):

        first_input = input("""Hi How would you like to proceed? 
        1. Not a Member? Register
        2. Already a member? Login
        3. Exit. 
        """)
        if first_input == '1':
            self.__register()
        elif first_input == '2':
            self.__login()
        else:
            exit()

    def __register(self):
        print(self, 'Register')

    def __login(self):
        print(self, 'Logged In')


obj = NLPApp()
