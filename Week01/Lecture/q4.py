top_scorers = [
      ["11 goal(s)", "Sebastien Haller", "Ajax"],
      ["8 goal(s)", "Mohamed Salah", "Liverpool"],
      ["14 goal(s)", "Karim Benzema", "Real Madrid"],
      ["7 goal(s)", "Christopher Nkunku", "Leipzig"],
      ["13 goal(s)", "Robert Lewandowski", "Bayern Munich"]
]

goals = []
for sublist in top_scorers:
    score = sublist[0]
    score = score.split(" ")
    goal = int(score[0])
    goals.append(goal)

maxGoal = max(goals)

for sublist in top_scorers:
    score = sublist[0]
    score = score.split(" ")
    goal = int(score[0])
    if goal == maxGoal:
        print(sublist[1], "-", sublist[2])