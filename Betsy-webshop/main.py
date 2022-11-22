__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

import models
from peewee import *

def search(term):
    
    
    lower_term = term.lower()
    q = (models.Product.select()
        .where ((models.Product.name.contains(lower_term)) | (models.Product.description.contains(lower_term))))
    if q:
        for product in q:             
            return f'Product: {product.name} found'
    else:
            return "No products found"


def list_user_products(user_id):
    q = (models.Product.select()
    .join(models.UserProduct).join(models.User) 
    .where (models.UserProduct.user_id == user_id))

    username = models.User.get(user_id).name
  

    if q:
        print(f"User {username} has the following products: ")
        for product in q:
            return f"- {product.name}"
    else:
        return f"No user found for: {username}"


def list_products_per_tag(tag_id):

    q = (
        models.Product.select(models.Product, models.Product_Tag, models.Tag)
        .join(models.Product_Tag, on=(models.Product_Tag.product_id == models.Product.id))
        .join(models.Tag, on=(models.Product_Tag.tag == models.Tag.id))
        .where(models.Tag.id == tag_id)
    )
      
        
    if q:
        print(f'Tag_id: {tag_id} has the following products:')
        for product in q:
            return f"- {product.name}"
    else:
        return f"No tag found for Tag id: {tag_id}"
       
      


def add_product_to_catalog(user_id, product):
    #find_product = models.Product.select().where(models.Product.name == product)
    #find_user = models.UserProduct.select().where(models.UserProduct.user_id == user_id)
    get_product = models.Product.get(models.Product.name == product)
    get_user = models.User.get(user_id).name
        
    
    try:
    
        models.UserProduct.create(
                user_id = user_id,
                product_id = get_product.id,
                quantity = 1,
            
            )
        return(f"{product} is now added to user: {get_user}.")
         
        
    except: return("No user of product are found.")



def update_stock(product_id, new_quantity):
    try:
        product = models.Product.get(models.Product.id==product_id)
        models.Product.update(quantity=new_quantity).where(models.Product.id==product_id).execute()
        return f'{product.name} quantity is updated to {new_quantity}'
    except: return 'Something went wrong, stock did not update'
    


def purchase_product(product_id, buyer_id, quantity):

    try:
        product = models.Product.get(models.Product.id==product_id)
        buyer = models.User.get( models.User.id==buyer_id)
        
        models.Transaction.create(
                product = product.id,
                quantity = quantity,
                user_id = buyer.id
        )
        new_quantity = product.quantity - quantity
        update_stock(product_id, new_quantity)
        return f'{buyer.name} has  bought the product: {product.name} '
    except: return 'Something went wrong, transaction didnt go through'


   


def remove_product(product_id):

    try:
        
        product = models.Product.get(models.Product.id == product_id)
        product.delete_instance()
        return f'Product: {product.name} has been removed'

    except: return 'Something went wrong, product was not deleted'



#print(search('laptop'))

#print(list_user_products(3))
#print(list_products_per_tag(5))
#print(add_product_to_catalog(3,'Earphones'))
#print(update_stock(3, 4))
#print(purchase_product(3, 2, 2))
#print(remove_product(5))
