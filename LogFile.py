import datetime

def CreateLogFile():
    x = datetime.datetime.now()
    month = f"{x.strftime('%m')}"
    day = f"{x.strftime('%d')}"
    year = f"{x.strftime('%Y')}"
    time = f"{x.strftime('%X')}"
    time = time[0:5]
    format = f"{month} {day} {year}: {time}"
    filename = f"KeoghsPort{month}_{day}_{time[0:2]}{time[3:5]}.txt"
    with open(filename, "a") as file:
        file.write(f"{format} Program was started." + "\n")
        file.close()
    return filename  

def GetDateFormatted():
    x = datetime.datetime.now()
    month = f"{x.strftime('%m')}"
    day = f"{x.strftime('%d')}"
    year = f"{x.strftime('%Y')}"
    time = f"{x.strftime('%X')}"
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

def WritePathToFile(filename, path, totalmoves):
    if(len(path) == 0):
        return;
    file = open(filename, "a")
    comments = []
    for i in range(len(path) + 1):
        format = GetDateFormatted()
        if (i == 0):
            # populates first move when operator is ready
            input_str = input("Hit ENTER when ready for first move \n")
            if (input_str == ""):
                print(f"{i+1} of {totalmoves}: Move crane from park to [{str(path[i][1].location.x).zfill(2)}, {str(path[i][1].location.y).zfill(2)}]. \n")
                file.write(f"{format} Moved from PARK to [{str(path[i][1].location.x).zfill(2)}, {str(path[i][1].location.y).zfill(2)}]. \n")

            # adds a comment if operator needs to
            input_str = input("Hit C to make a comment if needed \n")
            if (input_str == "C" or input_str == "c"):
                comment = input("Enter your comment: ")
                comment = "'" + comment + "'."
                WriteComment(filename, comment)
        elif(i == len(path)):
            # populates next move when operator is ready
            input_str = input("Hit ENTER when done or C to make a final commment \n")
            if (input_str == ""):
                break
            
            # adds a comment if operator needs to
            elif (input_str == "C" or input_str == "c"):
                comment = input("Enter your comment: ")
                comment = "'" + comment + "'."
                WriteComment(filename, comment)
        else:
            # populates next move when operator is ready
            input_str = input("Hit ENTER when done \n")
            if (input_str == ""):
                if (i == len(path) - 1):
                    print(f"{i+1} of {totalmoves}: Move crane from [{str(path[i][0].location.x).zfill(2)}, {str(path[i][0].location.y).zfill(2)}] to park. \n")
                    file.write(f"{format} Moved from [{str(path[i][0].location.x).zfill(2)}, {str(path[i][0].location.y).zfill(2)}] to PARK. \n")
                else:
                    print(f"{i+1} of {totalmoves}: Move crane from [{str(path[i][0].location.x).zfill(2)}, {str(path[i][0].location.y).zfill(2)}] to [{str(path[i][1].location.x).zfill(2)}, {str(path[i][1].location.y).zfill(2)}]. \n")
                    file.write(f"{format} Container in [{str(path[i][0].location.x).zfill(2)}, {str(path[i][0].location.y).zfill(2)}] was moved to [{str(path[i][1].location.x).zfill(2)}, {str(path[i][1].location.y).zfill(2)}]. \n")
            
            # adds a comment if operator needs to
            input_str = input("Hit C to make a comment if needed \n")
            if (input_str == "C" or input_str == "c"):
                comment = input("Enter your comment: ")
                comment = "'" + comment + "'."
                WriteComment(filename, comment)
    file.close()

def WriteCycleFinished(filename, manifestname):
    format = GetDateFormatted()
    file = open(filename, "a")
    file.write(f"{format} Finished a Cycle. Manifest {manifestname} was written to desktop, and a reminder pop-up to operator to send file was displayed. \n")
    file.close()
    print(f"I have written an updated manifest to the desktop as {manifestname} \nDon't forget to email it to the captain. \n")

def WriteComment(filename, input):
    format = GetDateFormatted()
    file = open(filename, "a")
    file.write(f"{format} Operator notices {input} \n")
    file.close()
        

#10 18 2023: 01:14 Program was started.

#month day year: time