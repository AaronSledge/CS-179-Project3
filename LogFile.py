import datetime

def CreateLogFile():
    x = datetime.datetime.now()
    month = f"{x.strftime("%m")}"
    day = f"{x.strftime("%d")}"
    year = f"{x.strftime("%Y")}"
    time = f"{x.strftime("%X")}"
    time = time[0:5]
    format = f"{month} {day} {year}: {time}"
    filename = f"KeoghsPort{month}_{day}_{time[0:2]}{time[3:5]}"
    with open(filename, "a") as file:
        file.write(f"{format} Program was started." + "\n")
        file.close()
    return filename  

def GetDateFormatted():
    x = datetime.datetime.now()
    month = f"{x.strftime("%m")}"
    day = f"{x.strftime("%d")}"
    year = f"{x.strftime("%Y")}"
    time = f"{x.strftime("%X")}"
    time = time[0:5]
    format = f"{month} {day} {year}: {time}"
    return format

def WriteManifestNameToFile(filename, manifestname, numcontainers):
    format = GetDateFormatted()
    file = open(filename, "a")
    file.write(f"{format} Manifest {manifestname} is opened, there are {numcontainers} containers on the ship. \n")
    file.close()

def WriteTotalMoveTimeToFile(filename, nummoves, numtime):
    format = GetDateFormatted()
    file = open(filename, "a")
    file.write(f"{format} Balance solution found, it will require {nummoves} moves/{numtime} minutes. \n")
    file.close()

def WritePathToFile(filename, path, totalcontainers):
    file = open(filename, "a")
    for i in range(len(path)):
        format = GetDateFormatted()
        if (i == 0):
            input("Hit ENTER when ready for first move \n")
            print(f"{i} of {totalcontainers}: Move crane from park to [{str(path[i][1].location.x).zfill(2)}, {str(path[i][1].location.y).zfill(2)}]. \n")
        else:
            input("Hit ENTER when done \n")
            print(f"{i} of {totalcontainers}: Move crane from [{str(path[i][0].location.x).zfill(2)}, {str(path[i][0].location.y).zfill(2)}] to [{str(path[i][1].location.x).zfill(2)}, {str(path[i][1].location.y).zfill(2)}]. \n")
        file.write(f"{format} [{str(path[i][0].location.x).zfill(2)}, {str(path[i][0].location.y).zfill(2)}], was moved to [{str(path[i][1].location.x).zfill(2)}, {str(path[i][1].location.y).zfill(2)}]. \n")
    file.close()

def WriteCycleFinished(filename, manifestname):
    format = GetDateFormatted()
    file = open(filename, "a")
    file.write(f"{format} Finished a Cycle. Manifest {manifestname} was written to desktop, and a reminder pop-up to operator to send file was displayed. \n")
    file.close()

def WriteComment(filename, input):
    format = GetDateFormatted()
    file = open(filename, "a")
    file.write(f"{format} {input} \n")
    file.close()
        

#10 18 2023: 01:14 Program was started.

#month day year: time