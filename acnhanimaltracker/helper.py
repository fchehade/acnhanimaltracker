import os


def check_folder_structure(root_directory: str):
    """Checks if the required folder structure is in tact. If not it's going
    to create the necessary folders.

    Args:
        root_directory (str): Root project file
    """
    pickle_fish = f"{root_directory}/acnhanimaltracker/animals/animals/fish"
    pickle_bugs = f"{root_directory}/acnhanimaltracker/animals/animals/bugs"
    pickle_sea_creatures = (
        f"{root_directory}/acnhanimaltracker/animals/animals/sea_creatures"
    )
    images_fish = f"{root_directory}/acnhanimaltracker/animals/images/fish"
    images_bugs = f"{root_directory}/acnhanimaltracker/animals/images/bugs"
    images_sea_creatures = (
        f"{root_directory}/acnhanimaltracker/animals/images/sea_creatures"
    )
    file_list = [
        pickle_fish,
        pickle_bugs,
        pickle_sea_creatures,
        images_fish,
        images_bugs,
        images_sea_creatures,
    ]
    for file_path in file_list:
        if not os.path.exists(file_path):
            print(f"Found missing directory: {file_path}. Creating directory")
            os.makedirs(file_path)