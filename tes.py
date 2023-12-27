import requests
import pymongo
from random import randint
print("Hello, How can I help you today?")
client = pymongo.MongoClient("mongodb://localhost:27017")
DB = client['User_complaints']
coll1 = DB['December']
coll2 = DB['December_complaints']
rasa_server_url = "http://localhost:5005" 
conversationid = "default"
def handleComplain(order_id):
    product = coll1.find_one({"order_id":order_id})['product_name']
    if product:
          print("We found a product with that order id, your product is "+ str(product))
          complaint = input("Please Type out your complaint: ")
          k = randint(10000000,20000000)
          coll2.insert_one({"ticket_num":k, "complaint":complaint})
          print("Thank you, your complaint has been successfully registered, your ticket number is "+str(k))
    else:
          print("Sorry, it seems like that order ID is invalid")

def rasa_call(user_message):
    user_input_url = f"{rasa_server_url}/webhooks/rest/webhook"
    payload = {
                        "sender": conversationid,
                        "message": user_message
                        }
    response = requests.post(user_input_url, json=payload)
    bot_responses = response.json()
    response_message=""
    for bot_response in bot_responses:
                bot_response['text'] = bot_response['text'] + "\n"
                for i in bot_response['text']:
                    response_message+=i
    if "order ID" in response_message:
          oid = int(input())
          handleComplain(oid)
    return(response_message)
    
    