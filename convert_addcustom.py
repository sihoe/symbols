import re
import json

input_path = "addcustommarker.js"
output_path = "converted_custommarkers.json"

with open(input_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

pattern = re.compile(
    r"""addCustomMarker\(\s*      # start
    ["'](.+?)["']\s*,\s*          # title
    \[\s*([-+]?\d+\.\d+)\s*,\s*([-+]?\d+\.\d+)\s*\]\s*,\s*  # lat,lng
    ["'](.*?)["']\s*,\s*          # image url
    ["'](.*?)["']\s*\)""",        # symbol
    re.VERBOSE | re.IGNORECASE
)

results = []
for i, line in enumerate(lines, 1):
    match = pattern.search(line)
    if match:
        title, lat, lon, img, symbol = match.groups()
        results.append({
            "title": title.strip(),
            "latlng": [float(lat), float(lon)],
            "imageUrl": img.strip(),
            "symbolType": symbol.strip().lower()
        })
    else:
        print(f"[linje {i}] Ikke matchet: {line.strip()}")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"{len(results)} markører eksportert til {output_path}")
