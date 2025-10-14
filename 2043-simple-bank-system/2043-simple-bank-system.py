class Bank(object):
    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if not (1 <= account1 <= len(self.balance) and 1 <= account2 <= len(self.balance)):
            return False
        if money > self.balance[account1 - 1]:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not (1 <= account <= len(self.balance)):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not (1 <= account <= len(self.balance)):
            return False
        if money > self.balance[account - 1]:
            return False
        self.balance[account - 1] -= money
        return True