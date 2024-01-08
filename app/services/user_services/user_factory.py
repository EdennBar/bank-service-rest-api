



from app.services.user_services.user_type import AdminUserType, EmployeeType, ProUserType, UserType


class UserFactory:
    @staticmethod
    def create_user_type(user_type: str) -> UserType:
        """Static method to create user type based on the provided string."""
        if user_type == "ADMIN":
            return AdminUserType("ADMIN")
        elif user_type == "PRO":
            return ProUserType("PRO")
        elif user_type == "EMPLOYEE":
            return EmployeeType("EMPLOYEE")
        else:
            raise ValueError("Invalid user type")


