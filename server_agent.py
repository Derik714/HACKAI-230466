from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
import tes as Ts
import bingAPI as ba
from termcolor import colored
import sys,time
import requests
import pymongo
from random import randint
OWN_ADDRESS = "agent1qfdknfw4wem9nkv629ef6tvp48fz8hx47g6879d0mak4zm36rtxdjkwt3nq"
USER_ADDRESS = "agent1q26g9xju28xapnamtd5rk9smwrsfn54uhz39n844vzzyzd5qv92yxac8chm" #Address of the client_agent
server_agent = Agent(name="SERVER",port=3000,seed="Server ",endpoint=["http://127.0.0.1:3000/submit"])#Similar to client_agent and the alert agent, we are defining another agent here
fund_agent_if_low(server_agent.wallet.address())

out ="Can't reply to your query"
print("Server address: ", server_agent.address)
print("Hello, How can I help you today?")
class Message(Model):
	Query:str
	Choice: int


# @server_agent.on_interval(period = 8) #This function iterates the below starter function after every 8 seconds
# async def starter(ctx:Context):
#     message = colored("1. Text Search 2. Image Search\n","blue")
#     # for i in log_message:
#     #     sys.stdout.write(i)
#     #     time.sleep(0.02)
#     #     sys.stdout.flush()
#     choice =-1
#     query = "Dummy"
#     choice = input(message) #Taking input of City name from the user
#     print(choice)
#     if choice == 1:
#         print('dd')
#         query: input("Enter the text query to search")
#     elif choice == 2:
#         query = "image ka link dalna yaha pe"  
	
#     await ctx.send(SERVER_ADDRESS,Message(Query =query , Choice = choice ))#Sending the comma-separated message to the Client address
@server_agent.on_message(model=Message) #Recieving the result message from Server agent
async def output(ctx:Context, sender:str, msg:Message): 
	choice = msg.Choice
	print(choice)
	choice = int(choice)
	query = msg.Query
	print(query) 

	if choice == 1:
		
			result = Ts.rasa_call(query)
			ctx.logger.info(result)
			out = result
		# send it to chatbot and get the string reply store in output
	elif choice == 2:
		result = ba.func(query)
		out = result
		# send it to api server and get the string reply store in output
	ctx.logger.info(out) 
	await ctx.send(USER_ADDRESS ,Message(Query= out , Choice = 1))
if __name__ == "__main__":
	server_agent.run()
	