import os
import re
from pathlib import Path

def generate_year_gallery(year="2025"):
    root = Path(os.getcwd())
    assets_dir = root / "assets" / year
    target_readme = root / year / "README.md"
    
    if not assets_dir.exists():
        print(f"Assets dir {assets_dir} does not exist")
        return

    images = []
    for img_file in sorted(assets_dir.iterdir()):
        if img_file.suffix == '.webp' and 'day' in img_file.name.lower():
            images.append(img_file.name)
            
    # Sort by day
    def get_day(name):
        m = re.search(r'day(\d+)', name, re.IGNORECASE)
        return int(m.group(1)) if m else 999
    
    images.sort(key=get_day)
    
    # Grid configuration
    cols = 4
    
    content = f"# Advent of Code {year}\n\n"
    
    # HTML Table for the grid
    content += "<table>\n"
    
    for i in range(0, len(images), cols):
        content += "  <tr>\n"
        row_imgs = images[i:i+cols]
        
        # Row of Images
        for img in row_imgs:
            day_num = get_day(img)
            # Relative path from 2025/README.md to assets/2025/img.webp
            # 2025/README.md is in 2025/
            # assets/ is in ../assets/
            img_path = f"../assets/{year}/{img}"
            content += f'    <td align="center">\n      <img src="{img_path}" width="200" alt="Day {day_num}"><br>\n    </td>\n'
        
        # Fill empty cells if last row is incomplete
        if len(row_imgs) < cols:
            for _ in range(cols - len(row_imgs)):
                content += "    <td></td>\n"
                
        content += "  </tr>\n"

    content += "</table>\n"
    
    with open(target_readme, 'w') as f:
        f.write(content)
    
    print(f"Generated {target_readme} with {len(images)} images")

if __name__ == "__main__":
    generate_year_gallery()
