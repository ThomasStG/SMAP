import os

def get_path(path_nodes):
    relevant_images = []
    images_folder = './static/tempMapStuff'
    for i in range(len(path_nodes) - 1):
        start_node = path_nodes[i]
        end_node = path_nodes[i + 1]

        # Construct filenames for both directions
        forward_filename = f"{start_node}-{end_node}.png"
        backward_filename = f"{end_node}-{start_node}.png"

        # Check if the image exists in either direction
        forward_path = os.path.join(images_folder, forward_filename)
        backward_path = os.path.join(images_folder, backward_filename)
        if os.path.exists(forward_path) and not os.path.isdir(forward_path):
            relevant_images.append(forward_path.removeprefix('./static/'))
        elif os.path.exists(backward_path) and not os.path.isdir(backward_path):
            relevant_images.append(backward_path.removeprefix('./static/'))
        else:
            print(f"Warning: Image not found for path between {start_node} and {end_node}")
    return relevant_images


# Example usage

# Now you can use relevant_images to display or process the necessary images
