import json
import datetime

def register_user(user_json, name, age, password, phn):
    user = {
    "id":1,
    "name": name,
    "age": age,
    "password": password,
    "phone number": 24897389,
    "order_history": {}
    }
    try:
        file = open("user.json", "r+")
        content =json.load(file)
        for i in range(len(content)):
            if content[i]["phone number"] == phn:
                fp.close()
                return "user already Exists"
        else:
            user["id"] = len(content) + 1
            content.append(user)
    except JSONDecodeError:
        content = []
        content.append(user)
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent = 4)
    file.close()
    return "Success"
    
def update_user(user_json, key ,val, userid):
    file = open(user_json, "r+")
    content =json.load(file)
    for i in range(len(content)):
        if content[i] == key:
            x = content[i]
            if content[i]["id"] == userid:
                content[i][x] = val
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent = 4)
    file.close()
    return "Success"

def order_history(user_json, id):
    file = open("user.json","r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == id:
            print("Order History")
            print("Date     |  ordered_item")
            for i,j in content[i]['order_history'].items():
                print(f"{i}     |{j} ")
                file.close()
            return True
    file.close()
    return(False)
    
def user_placeOreder(user_json, food_json, user):
    food=[int(input("enter food id:"))for j in range(int(input("enter no of foods you want to order")))] 
    food_list = {id:int(input("enter the no of plates you want to order")) for id in food}
    date = datetime.datetime.today().strftime('%d-%m-%Y')
    file = open(user_json,"r+")
    content = json.load(file)
    file1 = open(food_json,"r+")
    content1 = json.load(file1)
    for i in range(len(content1)):
        for k in food_list:
            if content1[i]["id"] == k:
                if content1[i]["stock"] > food_list[k]:
                    for j in range(len(content)):
                        if content[j]["id"] == user:
                            if date in content[j]["order_history"]:
                                content[j]["order_history"][date].append(content1[i]["food_name"])
                            else:
                                content[j]["order_history"][date] = []
                                content[j]["order_history"][date].append(content1[i]["food_name"])
                                
                else:
                    print("Pls Enter less quantity")
                    break    
        else:
            print("Food Not Available")
        
        
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    
    file1.seek(0)
    file1.truncate()
    json.dump(content1, file1, indent=4)
    file1.close()
                 


#CRUD for food:
def add_food(food_json,food_name,no_plates,stock,price,discount):
    food = {
    "id":1,
    "food_name" : food_name,
    "no_plates":no_plates,
    "stock": stock,
    "price": price,
    "discount" : discount
    }
    try:
        file = open("food.json","r+")
        content = json.load(file)
        for i in range(len(content)):
            if content[i]["food_name"] == food_name:
                print("Food is already available")
        food["id"] = len(content)+1
        content.append(food)
    except:
        content = []
        content.append(food)
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent =1)
    file.close()
    return "Success"
    
def read_food(file_json):
    file = open("food.json","r")
    content = json.load(file)
    print("Menu:")
    for i in range(len(content)):
        print(f"ID {content[i]['id']}")
        print(f"Name--------------> {content[i]['food_name']}")
        print(f"Quantity ---------> {content[i]['no_plates']} plates")
        print(f"price(INR)--------> {content[i]['price']}")
        print(f"discount(INR)-----> {content[i]['discount']}")
    file.close()

def view_food(file_json):
    file = open("food.json","r")
    content = json.load(file)
    print("Menu:")
    for i in range(len(content)):
        print(f"ID {content[i]['id']}")
        print(f"Name--------------> {content[i]['food_name']}")
        print(f"Quantity ---------> {content[i]['no_plates']} plates")
        print(f"price(INR)--------> {content[i]['price']}")
        print(f"discount(INR)-----> {content[i]['discount']}")
        print(f"Stock(INR)-----> {content[i]['stock']}")
    file.close()

def update_food(file_json, food_id):
    file = open("food.json","r+") 
    content = json.load(file)
    key = int(input("Please Select 1 if you want to update the price \n Please Select 2 if you want to update the Quantity \n Please Select 3 if you want to update the Stock \n Please Select 4 if you want to update the discount given "))
    for i in range(len(content)):
        if content[i]['id'] == food_id:
            if key == 1:
                content[i]["price"] = float(input("Enter the revised price: "))
            if key == 2:
                content[i]["no_plates"] = int(input("Enter the Quantity: "))
            if key == 3:
                content[i]["stock"] += int(input("Enter the amount of food added or removed: "))#if food removed then input should be in negative
            if key == 4:
                content[i]["discount"] = float(input("Enter the revised discount: "))
            else:
                print("Please Enter a Valid Option")
            break
    else:
        print("Please Enter a Valid id")
    file.seek(0)
    file.truncate()
    json.dump(content,file, indent =1)
    file.close()
    return "Success" 

def remove_food(food_json, food_id):
    file = open(food_json,"r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]['id'] == food_id:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content,file, indent =1)
            file.close()
            break
    else:
        print("Enter a Valid id")
        
    return "Success"

print("Annyeonghaseyo! Welcome to Zomati")           
val = input("Do you Want to order Food Y/n: ") 
while val.lower() == "y":
    print("Menu: ")
    print("1) Register")
    print("2) Login")
    print("3) Exit")
    val1 = input("Choose one value from the above: ")
    
    if val1 == "1": # register
        print("NEW USER SIGN UP")
        name = input("Enter the name: ")
        password = input("Enter the password: ")
        age = int(input("Enter your Age"))
        phn = input("Enter the Phn number")
        register_user("user.json", name, age, password, phn)   
    if val1 == "2":
        print("Please Log in to continue:")
        while True:
            print("1) User")
            print("2) Admin")
            print("3) Exit")
            val2 = input("Choose one value from above: ")
            if val2 == "1":
                print("-------USER------")
                user = input("Enter name: ")
                password = input("Enter Password: ")
                file = open("user.json", "r+")
                content = json.load(file)
                for i in range(len(content)):
                    if content[i]["name"] == user:
                        user_id = content[i]["id"]
                        if content[i]["password"] == password:
                            while True:
                                print()
                                print("1) View Menu")
                                print("2) Place New Order")
                                print("3) Show History of order")
                                print("4) Update Profile")
                                print("5) Exit")
                                val3 = input("Please select a value from above :")
                                if val3 == "1":
                                    read_food("food.json")
                                elif val3 == "2":
                                    user_placeOreder("user.json", "food.json", user_id)
                                elif val3 == "3":
                                    order_history("user.json",user_id)
                                elif val3 == "4":
                                    key = input("Enter the field you want to change: ")
                                    val = input("Enter the new value")
                                    update_user("user.json", key, val, user_id)
                                elif val3 == "5":
                                    print("Have a GOOD FOOD day!!")
                                    break
                                else:
                                    print("please select a valid option")
                                    break
                        else:
                            print("Incorrect Password")
                    else:
                        print("Incorrect user name")
                file.close()
                
            if val2 == "2":
                admin = input("enter your user name")
                password = input ("Enter your password : ")
                file = open("admin.json", "r+")
                content = json.load(file)
                for i in range(len(content)):
                    if content[i]["name"] == admin:
                        if content[i]["Password"] == password:
                            while True:
                                print("-------ADMIN-----")
                                print("1) Add New Food")
                                print("2) Edit Food")
                                print("3) View Food")
                                print("4) Remove Food") 
                                print("5) Exit")
                                val3 = input("Enter Your Choice Admin!!")
                                if val3 == "1":
                                    food_name = input("Enter Food Name: ")
                                    no_plates = int(input("Enter the no_plates Value: "))
                                    price = int(input("Enter the price: "))
                                    stock = int(input("Enter the stock: "))
                                    discount = float(input("Enter the discount: "))
                                    add_food("food.json", food_name, no_plates, stock, price, discount)
                                elif val3 == "2":
                                    food_id = int(input("Enter Food ID: "))
                                    update_food("food.json", food_id)
                                elif val3 == "3":
                                    view_food("food.json")
                                elif val3 == "4":
                                    food_id = int(input("Enter Food ID: "))
                                    remove_food("food.json", food_id)
                            
                                elif val == 5:
                                    print("%%%%Bye Bye%%%%%")
                                    break
                                else:
                                    print("Select a valid Choice")
                                    break
                        else:
                            print("Incorrect Password")
                           
                    else:
                        print("incorrect user name")
            file.close()
    if val1 == "3":
        print("BYE BYE")
        break  
        
    