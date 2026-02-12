import pandas as pd
df = pd.read_csv("world_cup.csv")

year = df["year"].tolist()
date = df["date"].tolist()
home_team = df["home_team"].tolist()
away_team = df["away_team"].tolist()
home_goals = df["home_goals"].tolist()
away_goals = df["away_goals"].tolist()
match_id = df["match_id"].tolist()
winner = df["winner"].tolist()

def aasta_summa():
    syear=int(input("Kirjuta aasta (1974-2022) ja ma ütlen, mitu väravat sellel aastal jalgpalli MM-i raames löödi: "))
    goals_per_year = 0
    for i in range(len(year)):
        if syear==year[i]:
            goals_per_year += + home_goals[i] + away_goals[i]

print (syear,"aastal löödi", goals_per_year, "väravat.")

def aasta_riik():
    print("Vali aasta ja riik. Saadan tabeli selle riigi mängudega tollel aastal.")
    ssyear=int(input("Vali aasta (1974-2022): "))
    scountry=input("Vali riik: ")
    indexes = []
    for j in range(len(year)):
        if ssyear==year[j]:
            if home_team[j]==scountry or away_team[j]==scountry:
                indexes.append(j)

print(f"{'Date':<15} {'Home':<15} {'Away':<15} {'HomeGoals':<10} {'AwayGoals':<10} {'Winner':<10}")
print("-" * 75)
for i in indexes:
    print(f"{date[i]:<15} {home_team[i]:<15} {away_team[i]:<15} {home_goals[i]:<10} {away_goals[i]:<10} {winner[i]:<10}")
