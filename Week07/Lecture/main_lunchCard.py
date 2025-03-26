import lunchCard as lun

peter = lun.LunchCard(20, 1, "Peter")
alice = lun.LunchCard(30, 2, "Alice")

peter.payLunch(10)
alice.payLunch(12)

peter.displayCurrentBalance()
alice.displayCurrentBalance()

peter.depositMoney(5)

peter.payLunch(16)
alice.payLunch(14)

peter.displayCurrentBalance()
alice.displayCurrentBalance()