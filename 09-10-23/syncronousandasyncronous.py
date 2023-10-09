# sychronous functionaloty
# in this functionality it excute one after one function. if we call one,two and tree functions at a time using main
# function it excutes first one after finish then excute two based on a line we placed the functions in main function

def one():
    print('i am gointo interview')

def two():
    print('my name is venkat')
    
def three():
    print('i got a job ')
    
def main():
    two()
    one()
    three()

main()

##################################################################################

# asyncronous functionality
# in this same senario what we did in above function but in this it excutes at time all functions 
# but excution output based time what we mention in that but it calling the all functions at a time 
import asyncio

async def taskRoutine():
    print('my name is venkat')
    await asyncio.sleep(2)
    print('iam going to interview')
    
async def main():
    TR = taskRoutine()
    task = asyncio.create_task(TR)
    await asyncio.sleep(5)
    print(' i got a job')
    await task
asyncio.run(main())