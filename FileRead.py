#[01,01], {00000}, NAN
#[01,02], {00000}, UNUSED
#[01,03], {00101}, Fish for Wendys

from Container import Container
from Container import Location

def FileRead(filename):
    file = open(filename)
    listContainers = set()

    while True:
        line = file.readline()
        if (line != ""):
            splitLine = line.split(", ")
            if (len(splitLine) == 3):
                try:
                    loc_line = splitLine[0]

                    if(loc_line[1] == "0"):
                        x = int(loc_line[2])
                    else:
                        print("Locations in wrong fromat in manifest exit")
                        exit()

                    if(loc_line[4] == "0"):
                        y = int(loc_line[5])
                    elif(loc_line[4] == "1"):
                        y = int(loc_line[4]+loc_line[5])
                    else:
                        print("Locations in wrong fromat in manifest exit")
                        exit()

                    c_loc = Location(x, y)
                    weight = splitLine[1]
                    description = splitLine[2]
                    container = Container(c_loc, weight, description)
                    listContainers.add(container)
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
