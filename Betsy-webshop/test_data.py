from models import*

def populate_test_data():
    # open de database connectie
    db.connect()

    # maak de tabellen aan
    db.create_tables([
                        User, 
                        Product, 
                        Tag, 
                        Transaction,
                        UserProduct,
                        Product_Tag 
                    ])
    
    
    
    
    products = [
        {'name': 'Phone case',
        'description': 'A case for your iphone',
        'price': 50.00,
        'quantity': 2},
        
        {'name': 'Pinda Mini Choco',
        'description': 'Best chocolate with pinda',
        'price': 10.00,
        'quantity': 5},
        
        {'name': 'Sweater',
        'description': 'Red sweater perfect for the winter',
        'price': 200.00,
        'quantity': 50},

        {'name': 'Lightswitch',
        'description': 'Automatic lightswitch',
        'price': 3.50,
        'quantity': 350},
   
        {'name': 'Speakers',
        'description': "Listen to your favourite music with the bose speakers",
        'price': 655.50,
        'quantity': 15},
       
        {'name': 'Earphones',
        'description': 'Quality sennheiser earphones',
        'price': 75.50,
        'quantity': 890},
      
        {'name': 'Laptop dell',
        'description': " good laptop for work",
        'price': 280.00,
        'quantity': 25},
       
        {'name': 'Fabric softener ',
        'description': 'Works on all sorts of fabric',
        'price': 750.00,
        'quantity': 150},
     
    ] 

    tags = [
        'iphone',
        'chocolate',
        'winter',
        'work',
        'fabric',
        'quality'
    ]
    for product in products:
        Product.create(
            name = product['name'],
            description = product['description'],
            quantity = product['quantity'],
            price = product['price'],
        )

    for tag in tags:
            Tag.create(name = tag)
    
    users = [
        {'name':'shef', 
        'address':'verlengdestraat', 
        'billing_info':'NL34879'},
 
            
        {'name':'gert',
        'address':'meesterlaan',
        'billing_info':'NL3fh4879'},
      

        {'name':'burgerman',
        'address':'livestraat',
        'billing_info':'NL3f4879'},
        

        {'name':'balod',
        'address':'dudokstraat',
        'billing_info':'NL3g4879'}
    ]
    user_products = [
        {'user_id': '1',
        'product_id': '1',
        'quantity': 3,
        },
        {'user_id': '3',
        'product_id': '4',
        'quantity': 3,
        },
    ]
    for user in users:
        User.create(
            name = user['name'],
            address = user['address'],
            billing_info = user['billing_info']
        )
        

    for user_product in user_products:
        UserProduct.create(
            user_id = user_product['user_id'],
            product_id = user_product['product_id'],
           quantity = user_product['quantity'],
        )
        
    producttag_data = [
        {"product_id": 1, "tag_id": 1},
        {"product_id": 1, "tag_id": 5},
        {"product_id": 2, "tag_id": 3},
        {"product_id": 3, "tag_id": 4},
        {"product_id": 4, "tag_id": 4},
        {"product_id": 5, "tag_id": 5},
        {"product_id": 6, "tag_id": 2},
    ]
    for item in producttag_data:
        Product_Tag.create(
            product_id=item['product_id'],
            tag_id=item['tag_id']
        )
populate_test_data()
