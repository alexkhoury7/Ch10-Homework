
import EmployeeClass as m
import PayrollDeductionClass as s


def main():

    name = 'Jimmy Smith'
    idnum = '58475'
    dep = 'Information Systems'
    title = 'Developer'
    month_sal = 6800

    emp = m.Employee(name, idnum, dep, title, month_sal)
    print()
    print()
    print()
    print('Name, ID Number, Department, Job Title, Monthly Salary')
    print(emp.get_name(), emp.get_id(), emp.get_dep(), emp.get_job(), format((emp.get_salary())))

    des1 = 'food court'
    des2 = 'gift contribution'
    des3 = 'vending machine'

    date1 = '8/14/2022'
    date2 = '8/12/2022'
    date3 = '8/17/2022' 
    date4 = '8/22/2022'
    date5 = '8/5/2022'

    charge1 = 22.5
    charge2 = 25
    charge3 = 15.25
    charge4 = 3
    charge5 = 2.75

    emp_id1 = '39119'
    emp_id2 = '58475'
    emp_id3 = '21547'

    ded1 = s.PayrollDeduction(des1, date1, charge1, emp_id1)
    ded2 = s.PayrollDeduction(des2, date2, charge2, emp_id2)
    ded3 = s.PayrollDeduction(des1, date3, charge3, emp_id3)
    ded4 = s.PayrollDeduction(des3, date4, charge4, emp_id2)
    ded5 = s.PayrollDeduction(des3, date5, charge5, emp_id2)

    print()
    print()
    print()
    print('Description, Date, Charge, Employee ID')
    print(ded1.get_description(), ded1.get_date(), ded1.get_charge(), ded1.get_employeeid())
    print(ded2.get_description(), ded2.get_date(), ded2.get_charge(), ded2.get_employeeid())
    print(ded3.get_description(), ded3.get_date(), ded3.get_charge(), ded3.get_employeeid())
    print(ded4.get_description(), ded4.get_date(), ded4.get_charge(), ded4.get_employeeid())
    print(ded5.get_description(), ded5.get_date(), ded5.get_charge(), ded5.get_employeeid())
    print()
    print()
    print()
    print('*** Employee Pay ***')
    print('Name:', emp.get_name())
    print('ID Number:', emp.get_id())
    print('Department:', emp.get_dep())
    print('Gross Pay: $', emp.get_salary())
    print('Net Pay: $', emp.get_salary() - ded2.get_total(charge2, charge4, charge5))

main()