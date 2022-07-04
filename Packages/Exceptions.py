class ClassCreationError(Exception):
    def __init__(
        self, message="Failed to build an object, check the input!:500"
    ) -> None:

        self.message = message
        super().__init__(self.message)


class UserDoesNotExistError(Exception):
    def __init__(
        self, message="User is not in the database, please enter an existing user!:401"
    ) -> None:

        self.message = message
        super().__init__(self.message)


class UserisNotAdminError(Exception):
    def __init__(self, message="User has no admin privileges!:405") -> None:

        self.message = message
        super().__init__(self.message)


class AdminIsNotMasterError(Exception):
    def __init__(self, message="Admin has no master privileges!:405") -> None:

        self.message = message
        super().__init__(self.message)


class ChangeYourUsernameError(Exception):
    def __init__(
        self, message="Username doesn't match with policy, change it!:403"
    ) -> None:

        self.message = message
        super().__init__(self.message)


class ChangeYourPasswordError(Exception):
    def __init__(
        self, message="Password is not valid any more, change it!:403"
    ) -> None:

        self.message = message
        super().__init__(self.message)


class PasswordIsPwnedError(Exception):
    def __init__(self, message="this password is already leaked!:400") -> None:

        self.message = message
        super().__init__(self.message)


class UserExistsAlreadyError(Exception):
    def __init__(
        self, message="User exists already, try with another one!:400"
    ) -> None:

        self.message = message
        super().__init__(self.message)


class AccountError(Exception):
    def __init__(self, message="go to login to check your account!:403") -> None:

        self.message = message
        super().__init__(self.message)


class LengthError(Exception):
    def __init__(self, message="length doesn't match policy!:403") -> None:

        self.message = message
        super().__init__(self.message)


class PasswordUsedBeforeError(Exception):
    def __init__(self, message="password used before!:406") -> None:

        self.message = message
        super().__init__(self.message)


class AdminHimSelfError(Exception):
    def __init__(self, message="you cannot excute it on yourself!:403") -> None:

        self.message = message
        super().__init__(self.message)


class PasswordPolicyError(Exception):
    def __init__(self, message="password policy is not valid, try again!:400") -> None:

        self.message = message
        super().__init__(self.message)


class UsernamePolicyError(Exception):
    def __init__(self, message="username policy is not valid, try again!:400") -> None:

        self.message = message
        super().__init__(self.message)
