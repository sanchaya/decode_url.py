import os
import urllib.parse

def decode_filenames(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through files in the input folder
    for filename in os.listdir(input_folder):
        # Decode the filename
        decoded_filename = urllib.parse.unquote(filename)

        # Define full file paths
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, decoded_filename)

        # Copy the file to the new location with the decoded filename
        with open(input_file_path, 'rb') as f_in:
            with open(output_file_path, 'wb') as f_out:
                f_out.write(f_in.read())

    print("Files have been decoded and saved to the new folder.")

# Example usage
input_folder = './'
output_folder = './decoded_files'
decode_filenames(input_folder, output_folder)
