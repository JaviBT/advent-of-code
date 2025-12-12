import os
import sys
from pathlib import Path

def convert_png_to_webp(root_dir):
    try:
        from PIL import Image
    except ImportError:
        print("Pillow library is not installed. Please install it using: pip install Pillow")
        sys.exit(1)

    assets_path = Path(root_dir) / 'assets'
    if not assets_path.exists():
        print(f"Assets directory not found at {assets_path}")
        return

    print(f"Scanning {assets_path} for PNG files...")
    
    png_files = list(assets_path.rglob('*.png'))
    
    if not png_files:
        print("No PNG files found.")
        return

    print(f"Found {len(png_files)} PNG files. Starting conversion...")

    for png_path in png_files:
        try:
            webp_path = png_path.with_suffix('.webp')
            
            # Using context manager to ensure file is closed before removal
            with Image.open(png_path) as img:
                img.save(webp_path, 'WEBP')
            
            print(f"Converted: {png_path.name} -> {webp_path.name}")
            
            os.remove(png_path)
            print(f"Deleted: {png_path.name}")
            
        except Exception as e:
            print(f"Error converting {png_path}: {e}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    convert_png_to_webp(current_dir)
