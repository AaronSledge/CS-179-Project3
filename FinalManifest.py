import os

# takes in an array of tuples that shows each move performed
# The first item of each tuple is the parent_matrix or the initial state for that step before moving a container
# The second item of each tuple is the child_matrix or the final state for that step after moving a container
# The third item of each tuple is the action_list which states what actions must be performed
def CreateFinalManifest(file_name, final_matrix):
    # create file name here
    with open(file_name, "a") as file:
        # get the info for each container
        for row in range(len(final_matrix)):
            for col in range(len(final_matrix[0])):
                container = final_matrix[row][col]
                container_row = container.location.x
                container_col = container.location.y
                container_wg = container.weight
                container_desc = container.description
                
                # write the information for each container to the manifest file in the correct format
                output_line = f"[{str(container_row).zfill(2)},{str(container_col).zfill(2)}], {str(container_wg).zfill(5)}, {str(container_desc)}"
                if (row == len(final_matrix) and col == len(final_matrix[0])):
                    file.write(output_line)
                else:
                    file.write(output_line + "\n")