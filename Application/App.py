import nlpcloud


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

    def __second_menu(self):
        second_input = input("""Hi How would you like to proceed? 
        1. NER 
        2. Language Detection
        3. Sentiment Analysis
        4. Logout. 
        """)
        if second_input == '1':
            self.__ner()
        elif second_input == '2':
            self.__lang_detection()
        elif second_input == '3':
            self.__sentiment_anlys()
        else:
            exit('Logged out')

    def __register(self):
        name = input('enter name: ')
        email = input('enter email: ')
        password = input('enter Password: ')

        if email in self.__database:
            print('email already exits')
        else:
            self.__database[email] = [name, password]
            print(self.__database)
            print('Registration Successful! Now login ')
            self.__login()

    def __login(self):
        email = input('enter email: ')
        password = input('enter password: ')

        if email in self.__database:
            if self.__database[email][1] == password:
                print('Login successful')
                self.__second_menu()
            else:
                print('Password did not match')
                self.__login()

        else:
            print('Not registered')

    def __ner(self):
        para = input('enter the sentences: ')
        search_term = input('enter the search term: ')

    def __lang_detection(self):
        pass

    def __sentiment_anlys(self):
        pass


obj = NLPApp()
