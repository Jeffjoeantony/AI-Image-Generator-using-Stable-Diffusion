# ---------------------------------
# MULTIPLICATION TABLE

# num = int(input("Enter number:"))

# i=1
# while i <= 10:
#     result = num * 1
#     print(f"{i} * {num} = {result}")
#     i = i+1




# -----------------------------------
# TO DO LIST

# tasks = []

# while True:
#     task = input("Add a task (or type 'done' to finish)")

#     if(task.lower() == "done"):
#         break

#     tasks.append(task)

# print("Your Todo List: ")

# for t in tasks:
#     print("*",t)





# -----------------------------------
# RULE BASED CHATBOT

name = input("Enter name: ")
print("Hi ",name)


while(True):
    question = input("You: ")
    question = question.lower()

    if(question == "what is your name"):
        print("Bot: My name is Bot V1.2")

    elif(question == "Good Morning"):
        print("Bot: Good Morning Sir")
    
    elif("morning" in question):
        print("Bot: Good Morning Sir")

    else:
        print("Bot: I didn't get you sir")
        print("Thank You")
        break
