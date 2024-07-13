
class bankAccount(object):
    def __init__(self,a_t,bal,a_n):
        self.account_type = a_t
        self.balance = bal
        self.account_number = a_n
        self.customers = []

    def list_customers(self,customers):
        self.customers.append(customers)
    @property
    def account_type(self):
        return self._account_type
    @account_type.setter
    def account_type(self,a_t):
        self._account_type = a_t

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,bal):
        self._balance = bal

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self,a_n):
        if a_n > 99999999:
            print("The account number's specified length is too long only 8 numbers are allowed...")
        self._account_number = a_n

class customer(bankAccount):
        def __init__(self,a_t,bal,a_n,aname):
            bankAccount.__init__(self, a_t, bal, a_n)
            self.account_name = aname

        @property
        def account_name(self):
            return self._account_name

        @account_name.setter
        def account_name(self, aname):
            self._account_name = aname

        def __str__(self):
            return (f"This bank account belongs to {self.account_name} and the account number is {self.account_number}, and the balance is {self.balance}, and the account type is {self.account_type}.")




c1 = customer("Checking",10203,294920,"Chiedozie")

print(c1)


