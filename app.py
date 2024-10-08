import os

budget_posts = {} #dictionary with all budget posts and its values

def load_file(): #function for loading previous budget
    if os.path.exists("budget.txt"): #checks if there is a budget file on system already
        with open("budget.txt", "r") as file: #opens file
            for line in file:
                if "Summan av dina kostnäder är: " in line or "Du har såhär mycket över: " in line:
                    continue #skips the sum costs and excess salary
                key, value = line.split(": ")#seperate budget post and value
                budget_posts[key] = float(value.replace("kr", "").strip())#convert value to float, remove "kr" and strip spaces
    print("Din tidigare budget har laddats in!")


def calculated_costs():
    costs = sum(budget_posts.values()) #function to sum up all the costs
    return costs

def calculated_excess(salary): #function to calculated excess salary
    excess = salary - calculated_costs()
    return excess

print("Välkommen till ditt budgetprogram") # Start of program

load_file()

while True:
    salary = input("Vad är din lön? ")
    try:
        salary = float(salary)
        break
    except ValueError:
        print("Du måste skriva en siffra!")

while True: #Main loop
    print("Val 1: Lägg till budgetpost.")
    print("Val 2: Ändra budgetpost.")
    print("Val 3: Skriv ut budget.")
    print("Val 4: Avsluta program.")
    svar = input("Välj vad du vill göra: ").lower()

    if svar == "val 1": #Add a budget post
        while True:
            key = input("Vilken budgetpost skulle du vilja lägga till? ").lower() #ask for the budgetpost/key
            if key in budget_posts:#checks if the budget post already  exists
                print ("Den budgetposten finns redan!")
            else:
                value = float(input("Vad kostar denna budgetpost? "))
                budget_posts[key] = value
            question = ""
            while True:
                question = input("Vill du lägga till en budgetpost till? Ja/Nej ").lower() #checks if user wants to add another budgetpost before returning to main loop
                if question == "ja":
                    break
                elif question == "nej":
                    break
                else:
                    print("Du måste skriva ja eller nej! ")
            if question == "nej":
                break
            
    elif svar == "val 2": # Change budgetpost
        while True:
            print("Du har dessa budgetposter redan: ")
            for key, value in budget_posts.items(): #print budget posts so you can which you already have
                print(f"{key}: {value}", "kr")
            key = input("Vilken kategori skulle du vilja ändra? ").lower()

            if key in budget_posts: #checks if budget post already exists
                print("Budgetposten kostar såhär mycket just nu:", budget_posts[key], "kr")
                value = float(input("Hur mycket kostar kategorin? "))
                budget_posts[key] = value
                question = input("Vill du ändra en budgetpost till? Ja/Nej").lower() #checks if user wants to add another budgetpost before returning to main loop
                if question == "ja":
                    continue
                elif question == "nej":
                    break
                else:
                    print("Du måste svara ja eller nej! ")
                    continue
            else:
                print("Den budgetposten finns inte!") 
        
    elif svar == "val 3": #Printing budgetpost
        for key, value in budget_posts.items():
            print(f"{key}: {value}", "kr")
        print("Summan av alla dina kostnader är: ", calculated_costs(), "kr")
        print("Du har såhär mycket pengar kvar: ", calculated_excess(salary), "kr")
        question = input("Vill du spara detta till en fil? ja/nej ").lower() #Question user if to create txt file of budget

        if question == "ja": 
            file = open("budget.txt", "w")
            for key, value in budget_posts.items():
                file.write(f"{key}: {value} kr\n")
            file.write(f"Summan av dina kostnader är: {calculated_costs()}\n") #write the calculated costs to the budget file
            file.write(f"Du har såhär mycket pengar över: {calculated_excess(salary)}")
            file.close()
            break
        elif question == "nej":
            break
        else:
            print("Du måste svara ja eller nej! ")
            continue



    elif svar == "val 4": #Quit program
        print("Avslutar...")
        break
    else:
        print("Du måste välja ett av dom fyra valen!")
    