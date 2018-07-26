from pyramid.view import view_defaults, view_config

from label_automobile.services.user import UserService
from label_automobile.models.user import User


@view_defaults(renderer='json')
class UserView:
    def __init__(self, request):
        self.request = request
        self.session = request.dbsession

    @view_config(route_name='user.list')
    def list(self):
        return [{
            "name": user.name,
            "surname": user.surname,
            "email": user.email
        } for user in self.session.query(User).all()]

    def get(self):
        raise NotImplementedError

    @view_config(route_name='user.find_by_email')
    def get_by_email(self):
        email = self.request.params.get('email', None)
        service = UserService(self.session)
        user = service.find_by_email(email)

        return {
            "name": user.name,
            "surname": user.surname,
            "email": user.email
        }
