import os
import shutil
from pathlib import Path

DRY_RUN = True

INCOMING = Path("/mnt/e/Downloads")
DEST_BASE = Path("/mnt/e/Downloads")

count = 0

# Get target folder
# target_directory = "../../../../mnt/e/Downloads"

# Walk all the files and extract zip files to move into mnt/e/Downloads/zip_files
for root, dirs, files in os.walk(INCOMING):
    dirs.clear()  # don't recurse
    root = Path(root)

    for filename in files:
        src = root / filename

        # skip non-files just in case
        if not src.is_file():
            continue

        ext = src.suffix_lower().lstrip(".")  # "jpg", "pdf", "", (no extension)

        bucket = f"{ext}_files" if ext else "no_extension_files"
        dst_dir = DEST_BASE / bucket
        dst = dst_dir / src.name

        count += 1

        if DRY_RUN:
            print(f"Would have moved: {src} -> {dst}")
        else:
            dst_dir.mkdir(parents=True, exist_ok=True) # auto-create folder
            shutil.move(str(src), str(dst))

print(f"Total files considered: {count}")



