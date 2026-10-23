# AI File Organizer 📁🤖

An AI-powered file organization tool built with Python that automatically categorizes files into folders based on their extensions. For unfamiliar file types, it uses a locally running Gemma 3 model through Ollama to suggest a category.

The application previews the proposed file movements and asks for user confirmation before moving files.

## ✨ Features

- **Automatic File Categorization:** Organizes files into Documents, Images, Media, Code, and Other files.
- **AI-Powered Suggestions:** Uses Gemma 3 through Ollama to suggest categories for unfamiliar file extensions.
- **AI Response Validation:** Accepts only predefined category names and falls back to `Other files` when the response is invalid or AI is unavailable.
- **File Preview:** Displays the proposed destination of each file before moving it.
- **User Confirmation:** Asks for confirmation before organizing files.
- **Duplicate Filename Handling:** Preserves existing files by choosing an available filename, such as `report_1.pdf` or `report_2.pdf`.
- **Safe Cancellation:** Allows users to cancel the operation without moving files.
- **Local AI Processing:** Uses a locally running Ollama model rather than requiring a cloud-based AI API.

## 🛠️ Technologies Used

- Python
- Ollama
- Gemma 3 (`gemma3:1b`)
- `os` — file and directory operations
- `shutil` — moving files

## 📂 Project Structure

```text
AI-File-Organizer/
│
├── MyFiles/             # Folder containing files to organize
├── Documents/           # Organized documents
├── Images/              # Organized images
├── Media/               # Organized audio and video files
├── Code/                # Organized source code files
├── Other files/         # Other and unrecognized files
│
├── app.py               # Main file organization application
├── test_ai.py           # AI category suggestion and validation tests
├── requirements.txt     # Python dependencies
└── README.md             # Project documentation
```

## 📋 File Categories

| Category | Example extensions |
|---|---|
| Documents | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`, `.csv` |
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg` |
| Media | `.mp3`, `.mp4`, `.wav`, `.mov`, `.flac`, `.avi` |
| Code | `.py`, `.java`, `.js`, `.html`, `.css`, `.cpp`, `.php`, `.go`, `.rb` |
| Other files | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, and other unrecognized types |

The extension lists can be expanded as needed.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AI-File-Organizer
```

Replace `<your-repository-url>` with your actual GitHub repository URL.

### 2. Install Python dependencies

Make sure Python is installed, then install the dependencies:

```bash
python -m pip install -r requirements.txt
```

The project uses the official Ollama Python client.

### 3. Install Ollama

Download and install Ollama from:

https://ollama.com/

### 4. Download the Gemma 3 model

Open a terminal and run:

```bash
ollama pull gemma3:1b
```

Ensure Ollama is running before launching the application.

### 5. Prepare the input folder

Place the files you want to organize inside the `MyFiles` folder.

If the folder does not exist, create it in the project directory.

### 6. Run the application

```bash
python app.py
```

## ▶️ How It Works

1. The application scans the `MyFiles` folder.
2. It identifies files and extracts their extensions.
3. Known extensions are categorized using predefined Python rules.
4. For unrecognized extensions, Gemma 3 suggests a category through Ollama.
5. The application validates the AI response against the permitted categories.
6. It determines destination paths and handles duplicate filenames.
7. It displays a preview of the planned file movements.
8. The user enters `yes` to proceed or `no` to cancel.
9. If confirmed, files are moved to their destination folders.

## 💻 Example Output

```text
Folder exists!
archive.zip -> Other files\archive.zip
code.py -> Code\code.py
report.pdf -> Documents\report.pdf
song.mp3 -> Media\song.mp3

Do you want to organize these files? (yes/no):
```

Enter `yes` to organize the files or `no` to cancel.

For an unfamiliar extension, the application may display the category suggested by the AI before showing the destination.

## 🧪 Testing

Test the AI suggestion function separately:

```bash
python test_ai.py
```

Run the complete organizer:

```bash
python app.py
```

Test with a variety of files, including known extensions, unfamiliar extensions, and duplicate filenames. Use sample files first to verify the behavior safely.

## ⚠️ Limitations

- AI categorization depends on the model's response and may not always be semantically correct.
- The AI uses filenames and extensions for suggestions; it does not inspect file contents.
- Invalid AI responses fall back to `Other files`.
- Ollama and the selected model must be available for AI suggestions. If AI is unavailable, the application falls back to `Other files`.
- File types not covered by the predefined extension rules may be categorized incorrectly by the AI.

## 🚀 Future Improvements

- AI-powered file renaming suggestions.
- Support for more file formats and customizable categories.
- A graphical user interface.
- File content analysis for more accurate categorization.
- Logging and undo support for file movements.
- Automated tests for categorization and duplicate handling.

## 👩‍💻 Author

Created as a Python and local-AI project to explore file automation, AI-assisted categorization, and safe file management.
