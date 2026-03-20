import os
import sys
import re

# 🌀 UNIVERSAL RENAME SCRIPT (V2.0)
# This script renames the project in all config files.

OLD_NAME_SLUG = "nomondays-web-app"
OLD_NAME_SNAKE = "nomondays_web_app"

FILES_TO_REPLACE = [
    "pyproject.toml",
    ".env",
    "docker-compose.yml",
    "Makefile",
    "web/config/settings/base.py",
    "web/config/settings/production.py",
    "web/config/settings/local.py",
    ".github/workflows/ci.yml",
    "README.md",
]

def rename_project(new_name):
    # Ensure name is snake_case for slug
    new_slug = new_name.replace("_", "-").lower()
    new_snake = new_name.replace("-", "_").lower()

    print(f"🌀 Renaming project to: {new_snake} ({new_slug})")

    for file_path in FILES_TO_REPLACE:
        if not os.path.exists(file_path):
            print(f"⚠️ Warning: File not found {file_path}")
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content.replace(OLD_NAME_SLUG, new_slug)
        new_content = new_content.replace(OLD_NAME_SNAKE, new_snake)

        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Updated {file_path}")
        else:
            print(f"ℹ️ No changes needed in {file_path}")

    print("\n🚀 RENAME COMPLETE!")
    print("👉 Next steps: RUN 'make build' and INITIALIZE A NEW GIT REPO.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/rename_project.py <new_project_name>")
        sys.exit(1)
    
    rename_project(sys.argv[1])
