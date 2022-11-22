from peewee import*
import peewee

db = peewee.SqliteDatabase('webshop_database.db')

class BaseModel(Model):
    class Meta:
        database = db

class Tag(BaseModel):
    name = peewee.CharField(unique=True)

class Product(BaseModel):
    name = peewee.CharField(unique=True)
    description = peewee.TextField()
    quantity = peewee.IntegerField(null=True)
    price = peewee.DecimalField()
    tags = peewee.ManyToManyField(Tag)
  

class User(BaseModel):
    name = peewee.CharField(unique=True)
    address = peewee.TextField()
    billing_info = peewee.TextField()


class UserProduct(BaseModel):
    user_id = peewee.ForeignKeyField(User)
    product_id = peewee.ForeignKeyField(Product)
    quantity = peewee.IntegerField()


class Transaction(BaseModel):
    user_id = peewee.ForeignKeyField(User)
    product = peewee.ForeignKeyField(Product)
    quantity = peewee.IntegerField()
    

Product_Tag = Product.tags.get_through_model()
