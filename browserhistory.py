from queue import LifoQueue

backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

NoOfVisists = int(input("Enter the number of url history: "))
print("Enter URLsto visit: ")
for i in range(NoOfVisists):
    url = input("URL: ")
    print(f"Visiting {url}")
    backward_history.put(current_page)
    current_page= url

print(f"Current page: {current_page}")
while input("Do you want to go forward? (yes/no): ").lower() == 'yes':
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"Going forward to {current_page}")
    else:
        print("No forward available")
        

