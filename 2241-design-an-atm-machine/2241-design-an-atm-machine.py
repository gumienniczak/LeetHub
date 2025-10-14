class ATM(object):

    def __init__(self):
        self.banknotes = [0] * 5

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for i in range(5):
            self.banknotes[i] += banknotesCount[i]
        

    def withdraw(self, amount):
        denoms = [20, 50, 100, 200, 500]
        banknotes_copy = self.banknotes[:]
        trans = [0] * 5

        for idx in range(4, -1, -1):
            if self.banknotes[idx] and amount >= denoms[idx]:
                can_use = min(self.banknotes[idx], amount // denoms[idx])
                trans[idx] += can_use
                self.banknotes[idx] -= can_use
                amount -= can_use * denoms[idx]

        if amount != 0:
            self.banknotes = banknotes_copy
            return [-1]
        return trans

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)