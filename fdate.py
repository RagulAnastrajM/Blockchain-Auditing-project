import os.path
import time


def get_file_datetime(file_path):
    # Get the creation time
    creation_time = os.path.getctime(file_path)

    # Get the modification time
    modification_time = os.path.getmtime(file_path)

    # Get the access time
    access_time = os.path.getatime(file_path)

    # Convert timestamps to readable date and time
    creation_time_str = time.ctime(creation_time)
    modification_time_str = time.ctime(modification_time)
    access_time_str = time.ctime(access_time)

    return {

        modification_time_str

    }


if __name__ == "__main__":
    file_path = "static/upload/211sad.png"  # Replace with the path to your file
    file_datetime = get_file_datetime(file_path)
    print("File datetime details:")
    for key, value in file_datetime.items():
        print(f"{key}: {value}")
