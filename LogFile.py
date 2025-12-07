import datetime
import matplotlib.pyplot as plt
import copy
from Container import Container, Location
import time

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

    if totalmoves == 0 or len(path) == 0:
        file = open(filename, "a")
        file.write("Ship already balanced. No moves required.\n")
        file.close()
        print("Ship already balanced. No moves required.\n")
        return

    # make fake container object for parked crane (9,1)
    park_container = Container(Location(9,1), "{00000}", "Crane")

    file = open(filename, "a")
    input_str = ""
    for i in range(len(path) + 1):
        format = GetDateFormatted()
        if i < len(path):
            src = path[i][0]
            dst = path[i][1]
            crane_logic = path[i][3]
        if (i == 0):
            # populates first move when operator is ready
            input_str = input("Hit ENTER when ready for first move \n")
            if (input_str == ""):
                print(f"{i+1} of {totalmoves}: Move crane from park to [{str(path[i][1].location.x).zfill(2)}, {str(path[i][1].location.y).zfill(2)}]. \n")
                src_label = "PARK"
                dst_label = f"[{dst.location.x:02d},{dst.location.y:02d}]"
                src_for_highlight = park_container

                step_label = f"Step {i+1}: {src_label} → {dst_label}"
                dst_for_highlight = dst

                # figure code
                # create new plotting window
                plt.close('all')
                plt.ion()

                fig, ax = plt.subplots(figsize=(7, 6))
                globals()['g_fig'] = fig
                globals()['g_ax'] = ax

                # deep copy so original matrix not modified
                working = copy.deepcopy(path[0][4])
                # draw before the next move
                draw_matrix(working, src=src_for_highlight, dst=dst_for_highlight, title=step_label + " (Before)", current_step=i, overall_path=path)     
                      
            # adds a comment if operator needs to
            input_str = input("Hit C to make a comment if needed \n")
            if (input_str == "C" or input_str == "c"):
                comment = input("Enter your comment: ")
                comment = "'" + comment + "'."
                WriteComment(filename, comment)
            
            input_str = input("Hit ENTER when done \n")
            if (input_str == ""):
                action_time_str = str(len(path[i][2]))
                if (action_time_str == "1"):
                    action_time_str += " minute"
                else:
                    action_time_str += " minutes"
                crane_move_input = f"Moved from PARK to [{str(path[i][1].location.x).zfill(2)}, {str(path[i][1].location.y).zfill(2)}], {action_time_str}. \n"
                WriteCraneAction(filename, crane_move_input)

                # apply the move to the matrix copy
                working = apply_move(working, src, dst, crane_logic)

                # draw after the move is made (no highlight needed for the after step is done shown)
                draw_matrix(working, title=step_label + " (After)", current_step=i+1, overall_path=path)
                time.sleep(1.5)

        elif(i == len(path)):
            # populates next move when operator is ready
            input_str = input("Hit ENTER when done or C to make a final commment \n")
            if (input_str == ""):
                # apply the move to the matrix copy
                working = apply_move(working, src, dst, crane_logic)

                # draw after the move is made (no highlight needed for the after step is done shown)
                draw_matrix(working, title=step_label + " (After)")
                break
            
            # adds a comment if operator needs to
            elif (input_str == "C" or input_str == "c"):
                comment = input("Enter your comment: ")
                comment = "'" + comment + "'."
                WriteComment(filename, comment)
        else:
            # populates next move when operator is ready
            if (input_str == ""):
                if (i == len(path) - 1):
                    src_label = f"[{src.location.x:02d},{src.location.y:02d}]"
                    dst_label = "PARK"
                    src_for_highlight = src

                    step_label = f"Step {i+1}: {src_label} → {dst_label}"
                    dst_for_highlight = park_container
                    # draw before the next move
                    draw_matrix(working, src=src_for_highlight, dst=dst_for_highlight, title=step_label + " (Before)", current_step=i, overall_path=path)
                    
                    print(f"{i+1} of {totalmoves}: Move crane from [{str(path[i][0].location.x).zfill(2)}, {str(path[i][0].location.y).zfill(2)}] to park. \n")
                    action_time_str = str(len(path[i][2]))
                    if (action_time_str == "1"):
                        action_time_str += " minute"
                    else:
                        action_time_str += " minutes"
                    crane_move_input = f"Moved from [{str(path[i][0].location.x).zfill(2)}, {str(path[i][0].location.y).zfill(2)}] to PARK, {action_time_str}. \n"
                    
                    # adds a comment if operator needs to
                    input_str = input("Hit C to make a comment if needed \n")
                    if (input_str == "C" or input_str == "c"):
                        comment = input("Enter your comment: ")
                        comment = "'" + comment + "'."
                        WriteComment(filename, comment)
                    
                    input_str = input("Hit ENTER when done \n")
                    if (input_str == ""):
                        WriteCraneAction(filename, crane_move_input)
                        # apply the move to the matrix copy
                        working = apply_move(working, src, dst, crane_logic)

                        # draw after the move is made (no highlight needed for the after step is done shown)
                        draw_matrix(working, title=step_label + " (After)", current_step=i+1, overall_path=path)
                        time.sleep(1.5)
                else:
                    src_label = f"[{src.location.x:02d},{src.location.y:02d}]"
                    dst_label = f"[{dst.location.x:02d},{dst.location.y:02d}]"
                    src_for_highlight = src

                    step_label = f"Step {i+1}: {src_label} → {dst_label}"
                    dst_for_highlight = dst
                    # draw before the next move
                    draw_matrix(working, src=src_for_highlight, dst=dst_for_highlight, title=step_label + " (Before)", current_step=i, overall_path=path)
                    
                    action_time_str = str(len(path[i][2]))
                    if (action_time_str == "1"):
                        action_time_str += " minute"
                    else:
                        action_time_str += " minutes"
                    if (crane_logic == True):
                        print(f"{i+1} of {totalmoves}: Move crane from [{str(path[i][0].location.x).zfill(2)}, {str(path[i][0].location.y).zfill(2)}] to [{str(path[i][1].location.x).zfill(2)}, {str(path[i][1].location.y).zfill(2)}]. \n")
                        crane_move_input = f"Crane was moved from [{str(path[i][0].location.x).zfill(2)}, {str(path[i][0].location.y).zfill(2)}] to [{str(path[i][1].location.x).zfill(2)}, {str(path[i][1].location.y).zfill(2)}], {action_time_str}. \n"
                    else:
                        print(f"{i+1} of {totalmoves}: Move container in [{str(path[i][0].location.x).zfill(2)}, {str(path[i][0].location.y).zfill(2)}] to [{str(path[i][1].location.x).zfill(2)}, {str(path[i][1].location.y).zfill(2)}]. \n")
                        crane_move_input = f"Container in [{str(path[i][0].location.x).zfill(2)}, {str(path[i][0].location.y).zfill(2)}] was moved to [{str(path[i][1].location.x).zfill(2)}, {str(path[i][1].location.y).zfill(2)}], {action_time_str}. \n"                        
                    # adds a comment if operator needs to
                    input_str = input("Hit C to make a comment if needed \n")
                    if (input_str == "C" or input_str == "c"):
                        comment = input("Enter your comment: ")
                        comment = "'" + comment + "'."
                        WriteComment(filename, comment)

                    input_str = input("Hit ENTER when done \n")
                    if (input_str == ""):
                        WriteCraneAction(filename, crane_move_input)
                        # apply the move to the matrix copy
                        working = apply_move(working, src, dst, crane_logic)

                        # draw after the move is made (no highlight needed for the after step is done shown)
                        draw_matrix(working, title=step_label + " (After)", current_step=i, overall_path=path)
                        time.sleep(1.5)
    plt.close()
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

def WriteCraneAction(filename, input):
    format = GetDateFormatted()
    file = open(filename, "a")
    file.write(f"{format} {input}")
    file.close()

#10 18 2023: 01:14 Program was started.

#month day year: time


# using the functions below we are able to have the visuals for each step be populated as the user performs each step

def draw_matrix(matrix, src=None, dst=None, title="", current_step=0, overall_path=None):
    # use global fig and axes to create only one window
    global g_fig, g_ax
    ax = g_ax
    fig = g_fig
    ax.clear()

    rows = len(matrix)
    cols = len(matrix[0])

    # set up grid size and remove ticks
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows + 1)  # +1 because crane cell is above row 8
    ax.invert_yaxis()         # this just flips the columns so it goes row 1 bottom to row 8 top
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=12)

    # use to check if matrix cell matches a specific container location
    def same(cell, cont):
        return (cont and cell.location.x == cont.location.x and cell.location.y == cont.location.y)

    # crane cell
    crane_color = "gray"  # default color
    if src and src.description == "Crane": crane_color = "green"  # highlight green if crane is source
    if dst and dst.description == "Crane": crane_color = "red"    # highlight red if crane

    ax.add_patch(plt.Rectangle((0, 0), 1, 1, facecolor=crane_color, edgecolor="black", linewidth=0.6))

    if (current_step == 0) or (current_step == len(overall_path)):
        ax.text(0.5, 0.5, "Crane", ha="center", va="center", fontsize=8)

    # draw all 8 ship container rows
    for r in range(rows):
        draw_y = rows - r  # vertical flip for display
        for c in range(cols):
            cell = matrix[r][c]
            desc = cell.description

            # base color depending on kind of cell
            if desc == "NAN":
                color = "black"
            elif desc == "UNUSED":
                color = "white"
            else:
                color = "lightgray"

            # highlights for source and destination containers
            if same(cell, src): color = "green"
            if same(cell, dst): color = "red"

            # draw rectangle for cell
            ax.add_patch(plt.Rectangle((c, draw_y), 1, 1, facecolor=color, edgecolor="black", linewidth=0.6))

            # Draw label text inside cell
            if desc not in ("NAN", "UNUSED", "Crane"):
                ax.text(c + 0.5, draw_y + 0.5, desc, ha="center", va="center", fontsize=8, color="black")

    # update the window
    fig.canvas.draw()
    fig.canvas.flush_events()
    fig.canvas.manager.set_window_title('Container Movements')
    plt.pause(0.05)


def apply_move(matrix, src, dst, crane_logic):

    # ignore crane only moves
    if src.description == "Crane" or dst.description == "Crane":
        return matrix

    # ignore matching location
    if (src.location.x, src.location.y) == (dst.location.x, dst.location.y):
        return matrix

    # find source/destination in actual matrix
    s_i = s_j = d_i = d_j = None
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if (matrix[i][j].location.x, matrix[i][j].location.y) == (src.location.x, src.location.y):
                s_i, s_j = i, j
            if (matrix[i][j].location.x, matrix[i][j].location.y) == (dst.location.x, dst.location.y):
                d_i, d_j = i, j

    # skip if something unexpected happens
    if s_i is None or d_i is None:
        return matrix

    # move the container from source to destination
    dst_cell = matrix[d_i][d_j]
    src_cell = matrix[s_i][s_j]

    if (crane_logic == False):
        dst_cell.description = src_cell.description
        dst_cell.weight = src_cell.weight

        # clear the old source location
        src_cell.description = "UNUSED"
        src_cell.weight = "{00000}"

    return matrix