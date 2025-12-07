import matplotlib.pyplot as plt
import copy

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


def visualize_path(start_matrix, path):
    # no moves so nothing to visualize
    if not path:
        print("Already balanced. No visualization.\n")
        return

    # creat new plotting window
    plt.close('all')
    plt.ion()

    fig, ax = plt.subplots(figsize=(7, 6))
    globals()['g_fig'] = fig
    globals()['g_ax'] = ax

    # deep copy so original matrix not modified
    working = copy.deepcopy(start_matrix)
    print("\nVisualization window opened...\n")

    for i, (src, dst, moveList, crane_logic) in enumerate(path):

        # make fake container object for parked crane (9,1)
        park_container = type(src)(type(src.location)(9,1), "{00000}", "Crane")

        # instructions displayed above grid
        if i == 0 and (src.location.x == dst.location.x and src.location.y == dst.location.y):
            # first step starts with crane as source
            src_label = "PARK"
            dst_label = f"[{dst.location.x:02d},{dst.location.y:02d}]"
            src_for_highlight = park_container
        else:
            src_label = "PARK" if src.description == "Crane" else f"[{src.location.x:02d},{src.location.y:02d}]"
            dst_label = "PARK" if dst.description == "Crane" else f"[{dst.location.x:02d},{dst.location.y:02d}]"
            src_for_highlight = src

        step_label = f"Step {i+1}: {src_label} → {dst_label}"
    

        # if destination is crane highlight red as target
        if dst.description == "Crane":
            dst_for_highlight = park_container   # highlight (9,1)
        else:
            dst_for_highlight = dst

        # draw befpre the next move
        draw_matrix(working, src=src_for_highlight, dst=dst_for_highlight, title=step_label + " (Before)", current_step=i, overall_path=path)

        input("Press ENTER to perform this move\n")

        # apply the move to the matrix copy
        working = apply_move(working, src, dst, crane_logic)

        # draw after the move is made (no highlight needed for the after step is done shown)
        draw_matrix(working, title=step_label + " (After)")

        if i < len(path) - 1:
            input("Press ENTER for next step\n")

    # end of visual so close window
    input("\nVisualization complete. Press ENTER to close.\n")
    plt.close()