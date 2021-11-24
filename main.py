from fastapi import FastAPI
import requests
import schedule
import time

app = FastAPI()

# from the section we can see that pizzas = 3 , desserts = 4 , drinks = 5 
Pizzas = 3
Desserts = 4
Drinks = 5

def sort_data(category_num, data):
    filtering_data = data['Data']['categoriesList'][category_num]['dishList']
    data_list = []
    for index in filtering_data:
        dic = {}
        dic['id'] = index['dishId']
        dic['name'] = index['dishName']
        dic['description'] = index['dishDescription']
        dic['price'] = index['dishPrice']
        data_list.append(dic)
    return data_list


def update():
    global pizzas, desserts, drinks
    url = "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup"
    response = requests.get(url)
    json_respone = response.json()
    pizzas = sort_data(Pizzas,json_respone)
    desserts = sort_data(Desserts,json_respone)
    drinks = sort_data(Drinks,json_respone)


update()


@app.get("/")
def index():
    return "Shlomy Yosef Assignment"


@app.get("/pizzas")
def get_pizzas():
    return pizzas


@app.get("/pizza/{pizza_id}")
def get_pizza(pizza_id: int):
    return pizzas[pizza_id]

@app.get("/desserts")
def get_desserts():
    return desserts


@app.get("/dessert/{dessert_id}")
def get_pizza(dessert_id: int):
    return desserts[dessert_id]


@app.get("/drinks")
def get_drinks():
    return drinks


@app.get("/drink/{drink_id}")
def get_drink(drink_id: int):
    return drinks[drink_id]


@app.post("/order")
def get_sum():
    order = {
    "drink": [2055839,2055844],
    "dessert":[2055835],
    "pizza": [2055830,2055833]
    }
    sum = 0  
    for drink in drinks:
        if drink['id'] in order['drink']:
            sum += drink['price']
    for dessert in desserts:
        if dessert['id'] in order['dessert']:
            sum += dessert['price']
    for pizza in pizzas:
        if pizza['id'] in order['pizza']:
            sum += pizza['price']

    return {"price": sum}


#schedule.every().day.at("10:00").do(update)