question = ["which language was used  to create face book",
"python","french","javascript","pnp","none",4]

["which language was used  to create face book",
"python","french","javascript","pnp","none",4]

["which language was used  to create face book",
"python","french","javascript","pnp","none",4]

["which language was used  to create face book",
"python","french","javascript","pnp","none",4]

["which language was used  to create face book",
"python","french","javascript","pnp","none",4]
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
many = 0 
i = 0
for i in range(0,len(question)):

    questions = question[i]
    print(f"\n\nqoestion for rs.{levels[i]}")
    print(f"a. {questions[1]}        b. {questions[2]}")
    print(f"c. {questions[3]}        d. {questions[4]}")
    reply = int(input("Enter your answer(1-4) or 0 to quit:\n"))
    if reply == 0 :
        many = levels[i-1]
    if (reply==question[-1]):
        print(f"correct answer , you have won Rs. {levels[i]}")
        if (i==4):
            many = 10000
        elif(i==9):
            many = 320000
    else:
        print("worng answer")
        break
print(f"your take home mony is {many}")
