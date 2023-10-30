from icecream import ic

class Pay:
    def __init__(self, pay): 
        self.pay = pay

    def pay_no_overtime(self, hours):
        return hours * self.pay * .8

    def pay_overtime(self, hours):
        return hours * self.pay * .8

    def total_pay(self, hours):
        if hours > 40:
            hours_in_overtime = hours - 40 
            return self.pay_overtime(hours_in_overtime) + self.pay_no_overtime(40)
        else:
            return self.pay_no_overtime(hours)

    def salary(self, hours):
        return 52 * self.total_pay(hours)
    
    def payPotential(self, func):
        return ["Salary: %s\nHours a week: %s\n" % (func(x), x) for x in range(40, 80, 5)]
        

maddypay = Pay(23)
jamespay = Pay(30)
ic(maddypay.payPotential(maddypay.salary))
ic(jamespay.payPotential(jamespay.salary))

