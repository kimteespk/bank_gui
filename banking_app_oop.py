#### banking system
# parent class: user
# hold detail about an user ### done
# has a func to show user details

#child class: bank
# stores details about the account balance
# stores deatils about the amount
# allows for depostis, withdraw, view balance


############# parent class #############

class User():
    def __init__(self, name, age, gender, password) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.password = password
    @property
    def show_details(self):
        print('Personal Details')
        print('')
        print('Name ', self.name)
        print('Age ', self.age)
        print('Gender ', self.gender)
        print('Password', self.password)

############ child class ###############
class Bank(User):
    def __init__(self, name, age, gender, password) -> None:
        super().__init__(name, age, gender, password)
        self.balance = 0 #'' 

    def deposit(self, balance, amount):
        self.balance = int(balance)
        self.balance = self.balance + amount
        print('Account balance has been updated : THB', self.balance)
        Write.update_book(self)
        return

    def withdraw(self, balance, amount):
        self.balance = int(balance)
        if amount > self.balance:
            print('Insufficient Funds | Balance Available : THB', self.balance)
        else:
            self.balance = self.balance - amount
            Write.update_book(self)
            print('Withdrawing : THB', amount)
            print('Balance has been updated : THB', self.balance)


    def view_balance(self):
        self.show_details()
        print('Available Balance : THB', self.balance)

class Write(Bank):
    def __init__(self, name, age, gender, password):
        super().__init__(name, age, gender, password)
        #self.new_file = open(self.name, 'w')

    def write_new_account(self):
        self.new_file = open(self.name, 'w')
        self.new_file.write(self.name+'\n')
        self.new_file.write(self.password+'\n')
        self.new_file.write(self.age+'\n')
        self.new_file.write(self.gender+'\n')
        self.new_file.write('0')
        self.new_file.close()

    def update_book(self):
        
        self.new_file = open(self.name, 'w')
        self.new_file.write(self.name+'\n')
        self.new_file.write(self.password+'\n')
        self.new_file.write(self.age+'\n')
        self.new_file.write(self.gender+'\n')
        self.new_file.write(str(self.balance))
        self.new_file.close()
        return      

    def get_book(self):
        self.file = open(self.name, 'r')   
        self.file_data = self.file.read()
        self.file_data = self.file_data.split('\n')
        
class Read():
    def __init__(self, name):
        self.name = name

    def get_password(self):
        self.file = open(self.name, 'r')    
        self.file_data = self.file.read()
        self.file_data = self.file_data.split('\n')
        self.password = self.file_data[1]
        return self.password

    def get_data(self):
        self.file = open(self.name, 'r')    
        self.file_data = self.file.read()
        self.file_data = self.file_data.split('\n')    
        return self.file_data

    def get_balance(self):
        self.file = open(self.name, 'r')
        self.file_data = self.file.read()
        self.file_data = self.file_data.split('\n')    
        self.file_balance = self.file_data[4]
        return self.file_balance

if __name__ == '__main__':

    kimtee = Bank('kimtee', '26', 'male', 'pass')
    kimtee.show_details
    kimtee.balance
    kimtee.deposit(100)
    test =Read('t')
    test.get_password()
    t = Read('t').get_password()
    
    kimteee = Bank('kimtee', '26', 'male', 'pass')
    kimtee = User('kimtee', '26', 'male', 'pass')
    
    kimteee.show_details()
    kimteee.deposit(200)
    kimteee.withdraw(1)
    kimteee.view_balance()
    kimteee.balance
    kimteee.name
    kimteee.password
