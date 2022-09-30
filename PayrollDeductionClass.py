class PayrollDeduction:

    def __init__(self, desc, date, chg_amt, emp_id):
        self.__description = desc
        self.__date = date
        self.__charge = chg_amt
        self.__employeeid = emp_id
        self.__total = 0
    def get_description(self):
        return self.__description
    def get_date(self):
        return self.__date
    def get_charge(self):
        return self.__charge
    def get_employeeid(self):
        return self.__employeeid
    def get_total(self, charge2, charge4, charge5):
        self.__total = charge2 + charge4 + charge5
        return self.__total