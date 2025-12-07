import matplotlib.pyplot as plt

def runTime():
    numContainers = [1, 4, 8]
    timeUCS = [1, 236, 764]
    timeAstar = [21, 22, 23]

    plt.figure(figsize=(10, 6))
    plt.xticks(range(1,8))
    plt.plot(numContainers, timeUCS, label = "Uniform Cost runTime", color = "blue")
    plt.plot(numContainers, timeAstar, label = "A star Cost runTime", color = "red")
    plt.xlabel("Number Of Containers")
    plt.ylabel("Time (seconds)")
    plt.title("Time vs Number Of Containers")
    plt.legend()
    plt.grid(True)
    plt.show()

