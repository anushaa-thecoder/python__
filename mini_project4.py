hot_beverages={'Espresso': 'Rs80',
               'Americano':'Rs90',
               'Cappuccino':'Rs120',
               'Latte': 'Rs140',
               'Hot chocolate': 'Rs130', 
               'Masala Chai': 'Rs70'}

cold_beverages={'Iced coffee': 'Rs120',
                'Cold brew': 'Rs150',
                'Milkshake':{'Vanila':'Rs100', 'Choclate': 'Rs120', 'Strawberry': 'Rs150' }, 
                'Mojito':{'Lime': 'Rs90', 'Orange':'Rs100', 'Blue lagoon': 'Rs130'},
                'Smoothies':{'Mango': 'Rs90', 'Berry': 'Rs180'},
                'Fresh lime soda': 'Rs60'}

main_bites={'Veg Sandwich': 'Rs90',
            'Grilled cheese sandwich': 'Rs120',
            'Wraps':{'Paneer':'Rs90', 'Veggie':'Rs110', 'Per peri':'Rs140'},
            'Fries':{'Plain': 'Rs80', 'Masala': 'Rs100', 'Peri peri':'Rs140'},
            'Garlic bread':{'Plain': 'Rs100', 'Cheese': 'Rs130'}, 
            'Pizza':{'Regular':'Rs100', 'Cheese': 'Rs120', 'Exotic': 'Rs150'},
            'Pasta':{'White sauce': 'Rs180', 'Red sauce': 'Rs210'}}

desserts={'Brownie': 'Rs100',
          'Cheesecake':{'Blueberry': 'Rs150', 'Classic': 'Rs160', 'Biscoff': 'Rs290'},
          'Cookies':'Rs40',  
          'Ice cream': {'Vanila':'Rs70', 'Chocolate': 'Rs80', 'Red velvet': 'Rs100'},
          'Pastries':{'Mango': 'Rs90', 'Black forest': 'Rs50', 'Strawberry': 'Rs120','Belgium Chocolate': 'Rs160'}}

cheesy_combos={'Coffee+Sandwich': 'Rs180',
               'Milkshake+Fries': 'Rs200',
               'Pasta+Brownie': 'Rs300',
               'Pizza+Cookies': 'Rs130',
               'Wraps+Ice cream': 'Rs150'}

extras={'Extra whipped cream': 'Rs20',
        'Extra chocochips': 'Rs10',
        'Extra cheese': 'Rs30',
        'Extra scoop': 'Rs40',
        'Extra veggies': 'Rs50'}

order = {}
total = 0

while True:
    print("\n===== WELCOME TO THE CAFE =====")
    print("1. Show Menu")
    print("2. Place Order")
    print("3. View Bill")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice =='1':
            print(hot_beverages)
            print(cold_beverages)
            print(main_bites)
            print(desserts)
            print(cheesy_combos)
            print(extras)
    elif choice =='2':
          break;