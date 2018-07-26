from ..repositories.user import UserRepository


class UserService:
    def __init__(self, session):
        self._repository = UserRepository(session)

    def find_by_email(self, email):
        """
        Find a user by email address
        :param email: str a user's email address
        :return: User
        """
        return self._repository.find_by_email(email)
