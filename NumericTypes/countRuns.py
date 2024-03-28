def countRuns():
    validValue=True
    runtimes = []
    while validValue:
            userInputStr = input("Enter the 10 km run time:")
            if userInputStr:
                runtimes.append(float(userInputStr))
            validValue = userInputStr
    print(f'Average of {sum(runtimes)/len(runtimes)} over,{len(runtimes)} runs')

countRuns()