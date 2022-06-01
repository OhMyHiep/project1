from flask import Flask
from flask_login import LoginManager
from models import UserDto 
from service import userService


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='python'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager=LoginManager()
    login_manager.login_view="auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(user_id):
        user_info=userService.getUserbyId(user_id)
        # print(f"user id: {user_id}")
        # print(f"(queried Id: {user_info[0][0]})")
        # print(int(user_id) not in user_info[0])
        if int(user_id) not in user_info[0]:
            return
        user = UserDto.User(user_info[0][0],user_info[0][1],user_info[0][2],user_info[0][3])
        return user

    return app