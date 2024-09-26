budget_posts = {} #dictionary with all budget posts and its values

def calculated_costs():
    costs = sum(budget_posts.values()) #function to sum up all the costs
    return costs

def calculated_excess(salary): #function to calculated excess salary
    excess = salary - calculated_costs()
    return excess


print("Välkommen till ditt budgetprogram") # Start of program
while True:
    salary = input("Vad är din lön?")
    try:
        salary = float(salary)
        break
    except ValueError:
        print("Du måste skriva en siffra!")

while True: #Main loop
    print("Val 1: Lägg till kategori.")
    print("Val 2: Ändra Kategori.")
    print("Val 3: Skriv ut budget.")
    print("Val 4: Avsluta program.")
    svar = input("Välj vad du vill göra: ")

    if svar == "Val 1": #Add a budget post
        while True:
            key = input("Vilken kategori skulle du vilja lägga till? ") #ask for the budgetpost/key
            if key in budget_posts:#checks if the budget post already  exists
                print ("Den kategorin finns redan!")
            else:
                value = float(input("Vad kostar denna kategori? "))
                budget_posts[key] = value
                question = input("Vill du lägga till en kategori till? Ja/Nej ")
                if question == "Ja":
                    continue
                else:
                    break
    elif svar == "Val 2": # Change budgetpost
        key = input("Vilken kategori skulle du vilja ändra? ")
        if key in budget_posts: #checks if budget post already exists
            value = float(input("Hur mycket kostar kategorin? "))
            budget_posts[key] = value
        else:
            print("Den budgetposten finns inte!") 
        
    elif svar == "Val 3": # Val 3 loop
        print(budget_posts)
        print("Summan av alla dina kostnader är: ", calculated_costs())
        print("Du har såhär mycket pengar kvar: ", calculated_excess(salary))
        break
    elif svar == "Val 4": #Avslutar programmet
        ("Avslutar...")
        break
    else:
        print("Du måste välja ett av dom fyra valen!")
    