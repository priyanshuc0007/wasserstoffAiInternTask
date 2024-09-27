# Create a data structure to store mapped data for each object
def map_data_to_objects(segmented_images, extracted_text, summaries):
    data_map = {}

    # Assuming each segmented image has the same index in segmented_images, extracted_text, summaries lists
    for idx, image_path in enumerate(segmented_images):
        data_map[idx + 1] = {
            "image_path": image_path,
            "description": summaries[idx],
            "extracted_text": extracted_text[idx]
        }

    return data_map
