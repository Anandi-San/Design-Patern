class transferFacade:
    def transfer(self, fromAccount, toAccount, amount):
        #transfer uang sejumlah 1.000.000 dari akun 1 ke akun 2
        #Find account by id
        self.account1 = account.findById(fromAccount)
        self.account2 = account.findById(toAccount)

        #set balance
        self.account1.setBalance(self.account1.getBalance() - amount)
        self.account2.setBalance(self.account2.getBalance() + amount)

if __name__ == '__main__':
    transfer = transferFacade()

    transfer.transfer(1, 2, 1000000)