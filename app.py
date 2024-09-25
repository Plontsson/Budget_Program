budget_posts = {} #dictionary with all budget posts and its values

print("Välkommen till ditt budgetprogram") # Start of program
while True:
    salary = input("Vad är din lön?")
    try:
        salary = float(salary)
    except ValueError:
        print("Du måste skriva en siffra!")

while True: #Main loop
    print("Val 1: Lägg till kategori.")
    print("Val 2: Ändra Kategori.")
    print("Val 3: Skriv ut budget.")
    print("Val 4: Avsluta program.")
    svar = input("Välj vad du vill göra: ")

    if svar == "Val 1": #Add a budget post
        key = input("Vilken kategori skulle du vilja lägga till? ") #ask for the budgetpost/key
        if key in budget_posts:#checks if the budget post already  exists
            print ("Den kategorin finns redan!")
        else:
            value = float(input("Vad kostar denna kategori? "))
            budget_posts[key] = value

    elif svar == "Val 2": # Change budgetpost
        key = input("Vilken kategori skulle du vilja ändra? ")
        if key in budget_posts: #checks if budget post already exists
            value = float(input("Hur mycket kostar kategorin? "))
            budget_posts[key] = value
        else:
            print("Den budgetposten finns inte!") 
        
    elif svar == "Val 3": # Val 3 loop
        costs = sum(budget_posts.values())
        excess = salary - costs
        print(budget_posts)
        print("Summan av alla dina kostnader är: ", costs)
        print("Du har såhär mycket pengar kvar: ", excess)
        break
    elif svar == "Val 4": #Avslutar programmet
        ("Avslutar...")
        break
    else:
        print("Du måste välja ett av dom fyra valen!")
    