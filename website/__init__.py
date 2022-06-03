from flask import Flask
from flask_login import LoginManager
from website import config_psql
from sqlalchemy_utils import database_exists, create_database
from dao.DB_orm import db
from models.ORM_models import Employee


params=config_psql.config()
# print("\n",params['user'],"\n")


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='python'
    app.config['SQLALCHEMY_DATABASE_URI']= f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['name']}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from models.ORM_models import Employee, Role, Request, EmployeRole, Category

    engine=db.create_engine(f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['name']}",{})
    createDatabase(engine,app)

    login_manager=LoginManager()
    login_manager.login_view="auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return Employee.query.filter_by(employee_id=id).first()



    return app


def createDatabase(engine,app):
    if not database_exists(engine.url):
        create_database(engine.url)
        db.create_all(app=app)
        print("\ndatabase created!\n")
