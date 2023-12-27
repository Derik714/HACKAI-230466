
flag=0


from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
from termcolor import colored

import sys,time
OWN_ADDRESS = "agent1q26g9xju28xapnamtd5rk9smwrsfn54uhz39n844vzzyzd5qv92yxac8chm"
SERVER_ADDRESS = "agent1qfdknfw4wem9nkv629ef6tvp48fz8hx47g6879d0mak4zm36rtxdjkwt3nq" 
user_agent = Agent(name="User",port=8000,seed="Customer ",endpoint=["http://127.0.0.1:8000/submit"])#Similar to client_agent and the alert agent, we are defining another agent here
fund_agent_if_low(user_agent.wallet.address())
print("User address: ", user_agent.address)

class Message(Model):
    Query:str
    Choice: int


@user_agent.on_interval(period = 8) #This function iterates the below starter function after every 8 seconds
async def continue_conversation(ctx:Context):
    global flag
    if flag ==0:
        flag =1
        mess = colored("1. Text Search 2. Image Search\n","blue")
        # for i in log_message:
        #     sys.stdout.write(i)
        #     time.sleep(0.02)
        #     sys.stdout.flush()
        choice =-1
        query = "Dummy"
        choice = input(mess)
        choice = int(choice)  
        print(choice)
        if choice == 1:
            query = input("Enter the text query to search: ")
            # send to rasa
        elif choice == 2:
            query = input("Enter image link : ")  
        await ctx.send(SERVER_ADDRESS,Message(Query =query , Choice = choice ))#Sending the comma-separated message to the Client address
    else:
        pass
    


@user_agent.on_message(model=Message) #Recieving the result message from Server agent
async def output(ctx:Context, sender:str, msg:Message): 
    size = len(msg.Query)
    global flag
    if size > 0:
        print(msg.Query)
        ans2 = input ('\nWant to ask something else (No to end convo else type your question) :' )
        if(ans2 == 'No'):
            flag =0
        else:
            await ctx.send(SERVER_ADDRESS,Message(Query =ans2 , Choice = 1 ))

    else:
        flag =0

if __name__ == "__main__":
    user_agent.run()
    