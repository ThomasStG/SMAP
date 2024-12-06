import os


def get_path(path_nodes):
    relevant_images = []
    images_folder = './static/BoldedMap'
    images_folder = './static/BoldedMap'
    for i in range(len(path_nodes) - 1):
        start_node = path_nodes[i]
        end_node = path_nodes[i + 1]

        # Construct filenames for both directions
        forward_filename = f"{start_node}-{end_node}.png"
        backward_filename = f"{end_node}-{start_node}.png"

        # Check if the image exists in either direction
        forward_path = os.path.join(images_folder, forward_filename)
        backward_path = os.path.join(images_folder, backward_filename)
        if os.path.isfile(forward_path):
            forward_path = forward_path.removeprefix('./static/')
            relevant_images.append(forward_path)
        elif os.path.isfile(backward_path):
            backward_path = backward_path.removeprefix('./static/')
            relevant_images.append(backward_path)
        else:
            print(
                f"Warning: Image not found for path between {start_node} and {end_node}"
            )

    return relevant_images


# Example usage
#path_nodes = [2, 0, 1, 3, 5, 8, 29]

#relevant_images = get_path(path_nodes)
#print(relevant_images)