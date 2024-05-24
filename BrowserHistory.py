from queue import LifoQueue
backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

noofvisits = int(input("enter no. of url history:"))
print ("enter url to visit:")
for i in range (noofvisits):
    url = input("url:")
    print(f"visiting {url}")
    backward_history.put(current_page)
    current_page = url
print (f"current page:{current_page}")
while input("do you want to go back?(yes/no)").lower() == "yes" :
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"going back to {current_page}")
    else:
        print ("no previous page available")
