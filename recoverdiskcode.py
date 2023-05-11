import os
import shutil

def recover_disk(source_path, destination_path):
    try:
        # Check if the source path exists
        if not os.path.exists(source_path):
            print("Source path does not exist.")
            return
        
        # Check if the destination path exists
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
        
        # Iterate over files in the source directory
        for root, dirs, files in os.walk(source_path):
            for file in files:
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_path, file)
                
                try:
                    # Copy the file to the destination path
                    shutil.copy2(source_file_path, destination_file_path)
                    print(f"Recovered file: {destination_file_path}")
                except Exception as e:
                    print(f"Failed to recover file: {source_file_path}")
                    print(f"Error: {str(e)}")
    
    except Exception as e:
        print(f"An error occurred during disk recovery: {str(e)}")

# Example usage
source_path = "/path/to/corrupted_disk"
destination_path = "/path/to/recovered_files"

recover_disk(source_path, destination_path)
