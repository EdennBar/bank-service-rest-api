from abc import ABC, abstractmethod

class UserType(ABC):
    def __init__(self,user_type):
        self.user_type = user_type

    @abstractmethod
    def user_type_info(self):
        pass

class AdminUserType(UserType):
    def user_type_info(self):
        return "ADMIN"


class ProUserType(UserType):
    def user_type_info(self):
        return "PRO"


class EmployeeType(UserType):
    def user_type_info(self):
        return "EMPLOYEE"





