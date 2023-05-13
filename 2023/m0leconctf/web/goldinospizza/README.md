
### goldinospizza


![goldinospizza]()

The flag is written in the announce channel in the official discord.

![flag](https://github.com/Hed6eH0g/ctf/blob/main/2023/m0leconctf/misc/sanity_check/sanity_check_flag.png)

By extracting the attached zip file, we can find the following 42 files and `grep -i -r flag ./` allows us to find that the clue for the flag is in `./flask/api.py`.

```
.
├── docker-compose.yml
├── Dockerfile
└── flask
    ├── api.py
    ├── auth.py
    ├── models
    │   ├── __init__.py
    │   ├── order.py
    │   ├── product.py
    │   └── user.py
    ├── requirements.txt
    ├── server.py
    ├── static
    │   ├── css
    │   │   ├── common.css
    │   │   └── index.css
    │   ├── img
    │   │   ├── 4_FORMAGGI.jpg
    │   │   ├── BACON_&_CHICKEN.jpg
    │   │   ├── BBQ_CHICKEN.jpg
    │   │   ├── BOSCAIOLA.jpg
    │   │   ├── CAPRICCIO.jpg
    │   │   ├── CHEESEBURGER.jpg
    │   │   ├── COUNTRY.jpg
    │   │   ├── DIAVOLA.jpg
    │   │   ├── EXTRAVAGANZZA.jpg
    │   │   ├── favicon.svg
    │   │   ├── GOLDEN.jpg
    │   │   ├── HAWAIANA.jpg
    │   │   ├── MARGHERITA.jpg
    │   │   ├── MEATZZA.jpg
    │   │   ├── MEDITERRANEA.jpg
    │   │   ├── MENU.png
    │   │   ├── PACIFIC_VEGGIE.jpg
    │   │   ├── PEPPERONI_PASSION.jpg
    │   │   ├── PRIMAVERA.jpg
    │   │   ├── PROMO.png
    │   │   ├── VEGGIE.jpg
    │   │   ├── VIVALDI.jpg
    │   │   ├── WELCOME.png
    │   │   └── WÜRSTY.jpg
    │   └── js
    │       └── index.js
    ├── templates
    │   ├── base.html
    │   ├── index.html
    │   ├── login.html
    │   └── register.html
    └── website.py

8 directories, 42 files
```

According to the corresponding code, we can find that the flag can be obtained if we could fulfill the conditions below:

1. specifying the correct item
2. product and quantity are surely in the item
3. type of `item["product"]` and `item["quantity"]` must be int
4. `balance` must be positive 
5. order GOLDEN (id = 0) at least one or more 

```
    for item in data["orders"]:                                                                                                                                                                                                             
        if type(item) is not dict:                                                                                                                                                                                                          
            db.session.rollback()                                                                                                                                                                                                           
            raise AssertionError("ONE OF YOUR 🍕 ORDERS IS NOT AN ORDER")                                                                                                                                                                   
        if "product" not in item:                                                                                                                                                                                                           
            db.session.rollback()                                                                                                                                                                                                           
            raise AssertionError("NO 🍕 'product' IN ONE OF YOUR ORDERS")                                                                                                                                                                   
        if type(item["product"]) is not int:                                                                                                                                                                                                
            db.session.rollback()                                                                                                                                                                                                           
            raise AssertionError("ONE OF YOUR 🍕 'product' IDS IS NOT INT")                                                                                                                                                                 
        if "quantity" not in item:                                                                                                                                                                                                          
            db.session.rollback()                                                                                                                                                                                                           
            raise AssertionError("NO 🍕 'quantity' IN ONE OF YOUR ORDERS")                                                                                                                                                                  
        if type(item["quantity"]) is not int:                                                                                                                                                                                               
            db.session.rollback()                                                                                                                                                                                                           
            raise AssertionError("ONE OF YOUR 🍕 'quantity' IS NOT INT")                                                                                                                                                                    
        product = db.session.execute(db.select(Product).filter(                                                                                                                                                                             
            Product.id == item["product"])).scalars().one_or_none()                                                                                                                                                                         
        if product is None:                                                                                                                                                                                                                 
            db.session.rollback()                                                                                                                                                                                                           
            raise AssertionError("WE DON'T SELL THAT 🍕")                                                                                                                                                                                   
        quantity = item["quantity"]                                                                                                                                                                                                         
        current_user.balance -= product.price * quantity                                                                                                                                                                                    
        if current_user.balance < 0:                                                                                                                                                                                                        
            db.session.rollback()                                                                                                                                                                                                           
            raise AssertionError("NO 🍕 STEALING ALLOWED!")                                                                                                                                                                                 
        db.session.add(Order(                                                                                                                                                                                                               
            user_id=current_user.id,                                                                                                                                                                                                        
            product_id=product.id,                                                                                                                                                                                                          
            product_quantity=quantity,                                                                                                                                                                                                      
            product_price=product.price                                                                                                                                                                                                     
        ))                                                                                                                                                                                                                                  
        if product.id == 0 and quantity > 0:                                                                                                                                                                                                
            ws.send(                                                                                                                                                                                                                        
                f"WOW you are SO rich! Here's a little extra with your golden special 🍕: {os.environ['FLAG']}")          
```

Throughout several test queries, we recognized that `current_user.balance -= product.price * quantity` does not sanitize the value of `quantity`.
Thus, we set the quantity negative and increase our balance.
After that, we could buy one or more GOLDEN.

However, there was any difference in the appearance and it prevented us from getting the flag.
To observe the behavior of the request and response, we launched the inspector (with Firefox) and check the response in the Network tab.
The flag was there though 🍕 was garbled.

![flag](https://github.com/Hed6eH0g/ctf/blob/main/2023/m0leconctf/web/goldinospizza/goldinospizza_flag.png)
