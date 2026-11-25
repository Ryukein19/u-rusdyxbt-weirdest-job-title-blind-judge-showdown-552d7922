import os
# Job-title entry, max 60 chars: the line below is the entire submission.
# Output goes to /output/entry.txt.
LINE = "Chief Officer of Untangling Headphone Cables"
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
