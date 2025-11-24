#[01,01], {00000}, NAN
#[01,02], {00000}, UNUSED
#[01,03], {00101}, Fish for Wendys

from Container import Container

def FileRead(filename):
    file = open(filename)
    listContainers = []

    while True:
        line = file.readline()
        if (line != ""):
            splitLine = line.split(", ")
            if (len(splitLine) == 3):
                try:
                    location = splitLine[0]
                    weight = splitLine[1]
                    description = splitLine[2]
                    container = Container(location, weight, description)
                    listContainers.append(container)
                except:
                    print("File in wrong format")
                    exit()
            else:
                print("File in wrong format")
                exit()
        else:
            break

    # Once we are done with the file we need to close it    
    file.close()

    # If list of containers remains empty, then we know the input file is empty
    if (listContainers == []):
        print("File is empty")
        exit()

    # The ship grid is allowed a maximum of 96 points
    if (len(listContainers) > 96):
        print("Number of locations in file is greater than maximum number of spots in 8 by 12 ship grid")
        exit()
    
    # This function returns the list of containers array which contains object container
    return listContainers