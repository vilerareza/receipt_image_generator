# Specify company info here
company_info = {
                'company_logo_path' : 'images/test_logo.png', 
                'company_name' : 'Company Name',
                'company_address' : 'Company address, street, city, country',
                'company_contact' : 'Phone: +12 345 678910, Tax No.: 12345678910',
                'message' : 'Thank you, come again!'
                }

# Specify order info here
order_info = {
                'order_no' : '123456',
                'order_type' : 'Dine-In',
                'customer' : 'Mr. Customer',
                'customer_sequence' : 123,
                'server' : 'Ms. Server',
                'cashier' : 'Ms. Cashier',
                }

# Specify price and payment info here
price_payment_info = {
                'tax_percent' : 13,
                'tendered' : 100,
                'payment_method' : 'CASH',
                }

food_items = [
        {
        'qty':2,
        'name':'Shrimp Ques', 
        'price':10.00, 
        'options':[{'qty':1, 'name': 'White Tortilla', 'price':0.00}, {'qty':2, 'name': 'Sauce', 'price':0.10}]
        },
        {
        'qty':1,
        'name':'Beef Ribs', 
        'price':15.00, 
        'options':[{'qty':1, 'name': 'Chili', 'price':0.00}, {'qty':2, 'name': 'Sauce', 'price':0.10}]
        },
        {
        'qty':5,
        'name':'Orange Juice', 
        'price':3.00, 
        'options':[{'qty':1, 'name': 'Ice', 'price':0.00}]
        },
        {
        'qty':1,
        'name':'Shrimp Ques', 
        'price':10.00, 
        'options':[{'qty':1, 'name': 'White Tortilla', 'price':0.00}, {'qty':1, 'name': 'Sauce', 'price':0.10}]
        },
        {
        'qty':1,
        'name':'Beef Ribs', 
        'price':15.00, 
        'options':[{'qty':1, 'name': 'Chili', 'price':0.00}, {'qty':1, 'name': 'Sauce', 'price':0.10}]
        },
        {
        'qty':5,
        'name':'Orange Juice', 
        'price':3.00, 
        'options':[{'qty':1, 'name': 'Ice', 'price':0.00}]
        }
        ]