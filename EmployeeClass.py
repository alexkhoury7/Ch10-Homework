class Employee:

    def __init__(self,name,idnum,dep,job,salary):

        self.__name = name
        self.__IDnumber = idnum
        self.__department = dep
        self.__jobtitle = job
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__IDnumber

    def get_dep(self):
        return self.__department

    def get_job(self):
        return self.__jobtitle

    def get_salary(self):
        return self.__salary

