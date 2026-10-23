import os
import shutil
from test_ai import suggest_category, ALLOWED_CATEGORIES

# Folder containing the files we want to organize
folder_path = "MyFiles"

# Check whether the source folder exists
if os.path.isdir(folder_path):
    print("Folder exists!")

    # Get the names of all items inside MyFiles
    items = os.listdir(folder_path)

    # Store the file movement plan before moving anything
    file_plan = []

    # Process each item one by one
    for item in items:

        # Build the complete path of the current item
        source_path = os.path.join(folder_path, item)

        # Continue only if the item is a file
        if os.path.isfile(source_path):

            # Separate the filename and its extension
            name, extension = os.path.splitext(item)
            extension = extension.lower()

            # Decide which category the file belongs to
            if extension in (
                ".pdf", ".doc", ".docx", ".txt",
                ".xls", ".xlsx", ".ppt", ".pptx", ".csv"
            ):
                category = "Documents"

            elif extension in (
                ".jpg", ".jpeg", ".png", ".gif",
                ".bmp", ".webp", ".svg"
            ):
                category = "Images"

            elif extension in (
                ".mp3", ".mp4", ".wav", ".mov",
                ".flac", ".avi", ".mkv"
            ):
                category = "Media"

            elif extension in (
                ".py", ".java", ".html", ".css",
                ".c", ".cpp", ".h", ".hpp", ".cs",
                ".js", ".ts", ".tsx", ".php", ".go",
                ".rb", ".r", ".rs", ".kt", ".kts",
                ".swift"
            ):
                category = "Code"

            elif extension in (".zip", ".rar", ".7z", ".tar", ".gz"):
                category = "Other files"

            else:
                # Ask AI only when the extension is unrecognized
                try:
                    raw_response = suggest_category(item).strip()
                    print("AI suggested:", repr(raw_response))

                    # Accept only an exact allowed category
                    if raw_response in ALLOWED_CATEGORIES:
                        category = raw_response
                    else:
                        print(
                            f"AI returned an invalid category for "
                            f"{item}: {raw_response!r}"
                        )
                        category = "Other files"

                except Exception as error:
                    # Continue safely if AI is unavailable
                    print(f"AI unavailable for {item}: {error}")
                    category = "Other files"

            # Build the destination folder path
            destination_folder = category

            # Create the folder before checking for duplicates
            # This happens only after confirmation, so for now
            # we prepare the plan and check existing destinations.
            destination_path = os.path.join(
                destination_folder, item
            )

            # Find an unused destination filename
            cnt = 1
            while os.path.exists(destination_path):
                destination_path = os.path.join(
                    destination_folder,
                    f"{name}_{cnt}{extension}"
                )
                cnt += 1

            # Save the source and destination paths
            file_plan.append((source_path, destination_path))

            # Display the proposed movement
            print(item, "->", destination_path)

    # Ask for confirmation only once
    if file_plan:
        answer = input(
            "Do you want to organize these files? (yes/no): "
        )

        if answer.strip().lower() == "yes":

            # Create all category folders after confirmation
            categories = [
                "Documents",
                "Images",
                "Media",
                "Code",
                "Other files"
            ]

            for category in categories:
                os.makedirs(category, exist_ok=True)

            # Recheck destination names before moving files
            for source_path, planned_path in file_plan:

                destination_folder = os.path.dirname(planned_path)

                # Use the original filename, not the planned filename
                original_filename = os.path.basename(source_path)
                name, extension = os.path.splitext(original_filename)

                destination_path = os.path.join(
                    destination_folder, original_filename
                )

                cnt = 1

                while os.path.exists(destination_path):
                    destination_path = os.path.join(
                        destination_folder,
                        f"{name}_{cnt}{extension}"
                    )
                    cnt += 1

                # Move the file to its destination
                shutil.move(source_path, destination_path)
                print("Moved to:", destination_path)

            print("File organization completed!")

        else:
            print("Operation cancelled. No files were moved.")

    else:
        print("No files found to organize.")

else:
    print("Folder not found!")