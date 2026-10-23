
import ollama

ALLOWED_CATEGORIES = {
    "Documents",
    "Images",
    "Media",
    "Code",
    "Other files"
}


def suggest_category(filename):
    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "user",
                "content": (
                    f"Classify this file: {filename}\n"
                    "Choose exactly one category based on the filename "
                    "and extension.\n"
                    "Allowed categories: Documents, Images, Media, Code, Other files.\n"
                    "Return only the category name."
                ),
            }
        ],
    )

    return response["message"]["content"].strip()


# Test the function when this file runs directly
if __name__ == "__main__":
    filename = "Archive"
    raw_response = suggest_category(filename)

    print("AI response:", repr(raw_response))

    if raw_response in ALLOWED_CATEGORIES:
        category = raw_response
    else:
        category = "Other files"

    print("Final category:", category)
