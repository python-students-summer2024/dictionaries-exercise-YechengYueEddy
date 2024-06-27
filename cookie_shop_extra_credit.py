"""
Functions necessary for running a virtual cookie shop.
See README.md for instructions.
Do not run this file directly.  Rather, run main.py instead.
"""


def bake_cookies(filepath):
    """
    Opens up the CSV data file from the path specified as an argument.
    - Each line in the file, except the first, is assumed to contain comma-separated information about one cookie.
    - Creates a dictionary with the data from each line.
    - Adds each dictionary to a list of all cookies that is returned.

    :param filepath: The path to the data file.
    :returns: A list of all cookie data, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    with open(filepath, 'r') as cookie_info:
        next(cookie_info)
        all_cookies = []
        
        for line in cookie_info:
            cur_line_list = line.strip().split(',')
            cur_line_dict = {}
            cur_line_list_index = 0
            
            for characteristic in ['id', 'title', 'description', 'price', 'sugar free', 'gluten free', 'contains nuts']:
                if characteristic == 'id':
                    cur_line_dict[characteristic] = int(cur_line_list[cur_line_list_index])
                elif characteristic == 'price':
                    price = cur_line_list[cur_line_list_index][1:]
                    cur_line_dict[characteristic] = round(float(price), 2)
                elif characteristic in ['sugar free', 'gluten free', 'contains nuts']:
                    cur_line_dict[characteristic] = cur_line_list[cur_line_list_index].strip().lower() == 'true'
                else:
                    cur_line_dict[characteristic] = cur_line_list[cur_line_list_index]
                cur_line_list_index += 1
            
            all_cookies.append(cur_line_dict)
        
        return all_cookies


def welcome_and_check_allergies():
    """
    Prints a welcome message to the customer in the format:

      Welcome to the Python Cookie Shop!
      We feed each according to their need.

    """
    # write your code for this function below this line
    print("\nWelcome to the Python Cookie Shop!\nWe feed each according to their need.\n")
    print("We'd hate to trigger an allergic reaction in your body. So please answer the following questions:\n")
    is_valid = False

    while not is_valid:
        is_allergic_nuts = input("Are you allergic to nuts? (answer 'yes', 'y', 'no', or 'n') ").lower()
        is_allergic_gluten = input("Are you allergic to gluten? (answer 'yes', 'y', 'no', or 'n') ").lower()
        is_diabetes = input("Do you suffer from diabetes? (answer 'yes', 'y', 'no', or 'n') ").lower()
        accept_ans = ['yes', 'y', 'no', 'n']
        if is_allergic_nuts in accept_ans and is_allergic_gluten in accept_ans and is_diabetes in accept_ans:
            is_valid = True
            return [is_diabetes in ['yes', 'y'], is_allergic_gluten in ['yes', 'y'], is_allergic_nuts in ['yes', 'y']]


def display_cookies(cookies):
    """
    Prints a list of all cookies in the shop to the user.
    - Sample output - we show only two cookies here, but imagine the output continues for all cookiese:
        Here are the cookies we have in the shop for you:

          #1 - Basboosa Semolina Cake
          This is a This is a traditional Middle Eastern dessert made with semolina and yogurt then soaked in a rose water syrup.
          Price: $3.99

          #2 - Vanilla Chai Cookie
          Crisp with a smooth inside. Rich vanilla pairs perfectly with its Chai partner a combination of cinnamon ands ginger and cloves. Can you think of a better way to have your coffee AND your Vanilla Chai in the morning?
          Price: $5.50

    - If doing the extra credit version, ask the user for their dietary restrictions first, and only print those cookies that are suitable for the customer.

    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below this line
    user_allergies = welcome_and_check_allergies()
    if user_allergies[0] and user_allergies[1] and user_allergies[2]:
        print("\nGreat! Here are the cookies without sugar, gluten, and nuts that we think you might like:\n")
    elif user_allergies[0] and user_allergies[1]:
        print("\nGreat! Here are the cookies without sugar and gluten that we think you might like:\n")
    elif user_allergies[0] and user_allergies[2]:
        print("\nGreat! Here are the cookies without sugar and nuts that we think you might like:\n")
    elif user_allergies[1] and user_allergies[2]:
        print("\nGreat! Here are the cookies without gluten and nuts that we think you might like:\n")
    elif user_allergies[0]:
        print("\nGreat! Here are the cookies without sugar that we think you might like:\n")
    elif user_allergies[1]:
        print("\nGreat! Here are the cookies without gluten that we think you might like:\n")
    elif user_allergies[2]:
        print("\nGreat! Here are the cookies without nuts that we think you might like:\n")
    else:
        print("\nHere are the cookies we have in the shop for you:\n")

    filtered_cookies = []
    for cookie in cookies:
        id = cookie['id']
        title = cookie['title']
        description = cookie['description']
        price = cookie['price']
        if user_allergies[0] and user_allergies[1] and user_allergies[2]:
            if cookie['sugar free'] and cookie['gluten free'] and not cookie['contains nuts']:
                filtered_cookies.append(cookie)
                print(f"#{id} - {title}\n{description}\nPrice: ${price:.2f}\n")
        elif user_allergies[1] and user_allergies[2]:
            if cookie['gluten free'] and not cookie['contains nuts']:
                filtered_cookies.append(cookie)
                print(f"#{id} - {title}\n{description}\nPrice: ${price:.2f}\n")
        elif user_allergies[0] and user_allergies[2]:
            if cookie['sugar free'] and not cookie['contains nuts']:
                filtered_cookies.append(cookie)
                print(f"#{id} - {title}\n{description}\nPrice: ${price:.2f}\n")
        elif user_allergies[0] and user_allergies[1]:
            if cookie['sugar free'] and cookie['gluten free']:
                filtered_cookies.append(cookie)
                print(f"#{id} - {title}\n{description}\nPrice: ${price:.2f}\n")
        elif user_allergies[2]:
            if not cookie['contains nuts']:
                filtered_cookies.append(cookie)
                print(f"#{id} - {title}\n{description}\nPrice: ${price:.2f}\n")
        elif user_allergies[1]:
            if cookie['gluten free']:
                filtered_cookies.append(cookie)
                print(f"#{id} - {title}\n{description}\nPrice: ${price:.2f}\n")
        elif user_allergies[0]:
            if cookie['sugar free']:
                filtered_cookies.append(cookie)
                print(f"#{id} - {title}\n{description}\nPrice: ${price:.2f}\n")
        else:
            filtered_cookies.append(cookie)
            print(f"#{id} - {title}\n{description}\nPrice: ${price:.2f}\n")
    return filtered_cookies


def get_cookie_from_dict(id, cookies):
    """
    Finds the cookie that matches the given id from the full list of cookies.

    :param id: the id of the cookie to look for
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: the matching cookie, as a dictionary
    """
    # write your code for this function below this line
    for cookie in cookies:
        if cookie['id'] == int(id):
            return cookie
    
    return False


def solicit_quantity(id, cookies):
    """
    Asks the user how many of the given cookie they would like to order.
    - Validates the response.
    - Uses the get_cookie_from_dict function to get the full information about the cookie whose id is passed as an argument, including its title and price.
    - Displays the subtotal for the given quantity of this cookie, formatted to two decimal places.
    - Follows the format (with sample responses from the user):

        My favorite! How many Animal Cupcakes would you like? 5
        Your subtotal for 5 Animal Cupcake is $4.95.

    :param id: the id of the cookie to ask about
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: The quantity the user entered, as an integer.
    """
    # write your code for this function below this line
    chosen_cookie = get_cookie_from_dict(id, cookies)
    if not chosen_cookie:
        return False
    
    is_integer = False
    while not is_integer:
        user_order_quantity = input(f"My favorite! How many {chosen_cookie['title']} would you like? (please enter an integer) ")
        if user_order_quantity.isdigit():
            user_order_quantity = int(user_order_quantity)
            is_integer = True
    
    subtotal = user_order_quantity * chosen_cookie['price']
    print(f"Your subtotal for {user_order_quantity} {chosen_cookie['title']} is ${subtotal:.2f}.\n")
    return user_order_quantity


def solicit_order(cookies):
    """
    Takes the complete order from the customer.
    - Asks over-and-over again for the user to enter the id of a cookie they want to order until they enter 'finished', 'done', 'quit', or 'exit'.
    - Validates the id the user enters.
    - For every id the user enters, determines the quantity they want by calling the solicit_quantity function.
    - Places the id and quantity of each cookie the user wants into a dictionary with the format
        {'id': 5, 'quantity': 10}
    - Returns a list of all sub-orders, in the format:
        [
          {'id': 5, 'quantity': 10},
          {'id': 1, 'quantity': 3}
        ]

    :returns: A list of the ids and quantities of each cookies the user wants to order.
    """
    # write your code for this function below this line
    all_suborders = []
    is_finished = False
    
    while not is_finished:
        user_order_id = input("Please enter the id number of the cookie you want (enter 'finished', 'done', 'quit', or 'exit' when you finished you order): ")
        if user_order_id.isdigit():
            user_order_id = user_order_id
            user_order_quantity = solicit_quantity(user_order_id, cookies)
            if not user_order_quantity:
                print('id not found')
                continue
            cur_suborder = {'id' : int(user_order_id), 'quantity' : user_order_quantity}
            all_suborders.append(cur_suborder)
        elif user_order_id.lower() in ['finished', 'done', 'quit', 'exit']:
            is_finished = True
    
    return all_suborders


def display_order_total(order, cookies):
    """
    Prints a summary of the user's complete order.
    - Includes a breakdown of the title and quantity of each cookie the user ordereed.
    - Includes the total cost of the complete order, formatted to two decimal places.
    - Follows the format:

        Thank you for your order. You have ordered:

        -8 Animal Cupcake
        -1 Basboosa Semolina Cake

        Your total is $11.91.
        Please pay with Bitcoin before picking-up.

        Thank you!
        -The Python Cookie Shop Robot.

    """
    # write your code for this function below this line
    print("\nThank you for your order. You have ordered:\n")
    total = 0
    
    for cookie in order:
        cookie_ordered = get_cookie_from_dict(cookie['id'], cookies)
        quantity_ordered = cookie['quantity']
        total += cookie_ordered['price'] * quantity_ordered
        print(f"-{quantity_ordered} {cookie_ordered['title']}")
    
    print(f"\nYour total is ${total:.2f}.\nPlease pay with Bitcoin before picking-up.")
    print("\nThank you!\n-The Python Cookie Shop Robot.\n")


def run_shop(cookies):
    """
    Executes the cookie shop program, following requirements in the README.md file.
    - This function definition is given to you.
    - Do not modify it!

    :param cookies: A list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    filtered_cookies = display_cookies(cookies)
    order = solicit_order(filtered_cookies)
    display_order_total(order, filtered_cookies)