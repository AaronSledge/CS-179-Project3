#[01,01], {00000}, NAN
#[01,02], {00000}, UNUSED
#[01,03], {00101}, Fish for Wendys

from Container import Container
from Container import Location

def FileRead(filename):
    try:
        file = open(filename)
    except:
        print("\nManifest does not exist.\n")
        return None
    listContainers = set()

    count = 1
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
                        print(f"\nLocations in wrong format in Manifest in line {count}.\n")
                        return None

                    if(loc_line[4] == "0"):
                        y = int(loc_line[5])
                    elif(loc_line[4] == "1"):
                        y = int(loc_line[4]+loc_line[5])
                    else:
                        print(f"\nLocations in wrong format in Manifest in line {count}.\n")
                        return None

                    c_loc = Location(x, y)
                    weight = splitLine[1]
                    description = splitLine[2]

                    if (len(description) >= 5):
                        if (description[0:4] == "NAN " or description[-5:] == " NAN\n"):
                            print(f"\nManifest is unclear if the location on the ship is NAN or not in line {count}.\n")
                            return None
                    
                    if (len(description) >= 8):
                        if (description[0:7] == "UNUSED " or description[-8:] == " UNUSED\n"):
                            print(f"\nManifest is unclear if the location on the ship is UNUSED or not in line {count}.\n")
                            return None
                    
                    if (description[-1] == "\n"):
                            description = description[:-1]

                    container = Container(c_loc, weight, description)
                    listContainers.add(container)
                except:
                    print(f"\nManifest in wrong format in line {count}.\n")
                    return None
            else:
                print(f"\nManifest in wrong format in line {count}.\n")
                return None
        else:
            break
        count += 1

    # Once we are done with the file we need to close it    
    file.close()

    # If list of containers remains empty, then we know the input file is empty
    if (listContainers == []):
        print("\nManifest is empty.\n")
        return None

    # The ship grid is allowed a maximum of 96 points
    if (len(listContainers) > 96):
        print("\nNumber of locations in Manifest is greater than maximum number of spots in 8 by 12 ship grid.\n")
        return None

    if (len(listContainers) < 96):
        print("\nNumber of locations in Manifest is less than maximum number of spots in 8 by 12 ship grid.\n")
        return None
    
    # This function returns the list of containers array which contains object container
    return listContainers
