import os
import sys

# 🌀 UNIVERSAL RENAME SCRIPT (V2.2)
# Standard Template Renamer: Replaces placeholders with your project name.

# The baseline identifier used in the template
TOKEN_DISPLAY = "BrandName"
TOKEN_SNAKE = "brandname_web_app"
TOKEN_SLUG = "brandname-web-app"
TOKEN_PLAIN = "brandname"

# Structural Exclusions
EXCLUDE_DIRS = {
    ".git", "__pycache__", ".venv", "venv", ".pytest_cache",
    "dbdata", "htmlcov", "node_modules", ".agent", ".agents"
}

EXCLUDE_FILES = {
    "poetry.lock", "package-lock.json", ".coverage", 
    "rename_project.py"
}

# Binary/Asset Exclusions
EXCLUDE_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".woff", ".woff2", ".ttf", ".eot",
    ".db", ".sqlite3", ".pyc", ".bin"
}

def rename_project(new_name):
    """
    Renames the template by replacing 'BrandName' tokens with the target name.
    """
    new_slug = new_name.replace("_", "-").lower()
    new_snake = new_name.replace("-", "_").lower()
    new_plain = new_name.lower()
    
    print(f"🌀 Renaming template to: '{new_name}'")
    print(f"   Slug:  {new_slug}")
    print(f"   Snake: {new_snake}")
    print(f"---")

    replacements = {
        TOKEN_SLUG: new_slug,
        TOKEN_SNAKE: new_snake,
        TOKEN_DISPLAY: new_name,
        TOKEN_PLAIN: new_plain,
    }

    updated_count = 0
    total_scanned = 0

    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            total_scanned += 1
            if file in EXCLUDE_FILES or any(file.endswith(ext) for ext in EXCLUDE_EXTENSIONS):
                continue

            file_path = os.path.join(root, file)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except (UnicodeDecodeError, PermissionError):
                continue

            new_content = content
            for old, new in replacements.items():
                new_content = new_content.replace(old, new)

            if content != new_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ Updated {file_path}")
                updated_count += 1

    print("\n🚀 RENAME COMPLETE!")
    print(f"📊 Files Scanned: {total_scanned} | Units Updated: {updated_count}")
    print("👉 Next: Run 'make build' to apply changes to containerized services.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/rename_project.py <NewProjectName>")
        print("Example: python scripts/rename_project.py MyAwesomeApp")
        sys.exit(1)
    
    # Run from project root
    rename_project(sys.argv[1])
