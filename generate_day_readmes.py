import os
from pathlib import Path

def generate_readmes(root_dir):
    root = Path(root_dir)
    year = "2025"
    assets_dir = root / "assets" / year
    
    # Target languages
    langs = ["python", "go"]
    
    for lang in langs:
        lang_dir = root / year / lang
        if not lang_dir.exists():
            continue
            
        print(f"Processing {lang} directories...")
        for day_dir in lang_dir.iterdir():
            if not day_dir.is_dir() or not day_dir.name.isdigit():
                continue
                
            day_num = day_dir.name
            image_name = f"AoC25-day{day_num}.webp"
            image_path = assets_dir / image_name
            
            if image_path.exists():
                readme_path = day_dir / "README.md"
                
                # Check if README already exists to avoid overwriting custom content
                # For now, we'll overwrite or create if it doesn't exist, as requested.
                # But let's check if it has content other than what we'd write.
                # Actually, user asked "Should I add...", implying they don't have them.
                
                # Relative path from 2025/lang/day to assets/2025
                # 2025/python/01 -> ../../../assets/2025/AoC25-day01.webp
                rel_image_path = f"../../../assets/{year}/{image_name}"
                
                title = f"Day {day_num}"
                # content = f"# {title}\n\n![{title}]({rel_image_path})\n"
                # Using HTML for width control as per previous preference
                content = f"""# {title}

<img src="{rel_image_path}" width="400" alt="{title}">
"""
                
                try:
                    with open(readme_path, "w") as f:
                        f.write(content)
                    print(f"Created/Updated: {readme_path}")
                except Exception as e:
                    print(f"Failed to write {readme_path}: {e}")
            else:
                 # Image doesn't exist for this day
                 pass

if __name__ == "__main__":
    # Assumes script is run from project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    generate_readmes(current_dir)
