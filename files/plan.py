with open('plan.txt','r') as plan:
    planLines = plan.readlines()
    planLines.sort()
    with open('plan_sorted.txt', 'w') as plan_sorted:
        for i in range(len(planLines)):
            plan_sorted.write(planLines[i])
print('Отсортированный список планет сохранен в файле plan_sorted.txt')