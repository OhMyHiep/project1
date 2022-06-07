from dao.DB_orm import db
from models.ORM_models import Category

def getAllCategories():
    categories=Category.query.all()
    for i in categories:
        print(i.categoryName)
    return categories