import os
import urllib.request
import re

language_dic = {
    'python': '🐍 Python',
    'java': '☕ Java',
    'cpp': '💻 C++',
    'go': '🦫 Go',
    # Add more languages if necessary
}

def load_titles():
    titles = {}
    if os.path.exists("aoc_problem_titles.txt"):
        current_year = None
        with open("aoc_problem_titles.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("[") and line.endswith("]"):
                    current_year = line[1:-1]
                    titles[current_year] = {}
                elif line.startswith("Day ") and ":" in line and current_year:
                    parts = line.split(":", 1)
                    day_part = parts[0].strip()[4:] # Remove "Day "
                    title_part = parts[1].strip()
                    titles[current_year][day_part] = title_part
    return titles

problem_titles_cache = load_titles()

def get_problem_title(year, day, lang_dir):
    # Try to get from cache first
    year_str = str(year)
    day_str = str(day)
    if year_str in problem_titles_cache and day_str in problem_titles_cache[year_str]:
        return problem_titles_cache[year_str][day_str]
    
    # Fallback to default title
    return f"AoC {year} - Day {day}"

def find_solution_files(year, lang_dir, day):
    """Find the solution files in a specific directory and return their paths."""
    day_path = os.path.join(year, lang_dir, str(day))
    try:
        files = os.listdir(day_path)
        part1_file = next((f for f in files if "part1" in f.lower()), None)
        part2_file = next((f for f in files if "part2" in f.lower()), None)
        return part1_file, part2_file
    except FileNotFoundError:
        return None, None

def generate_readme():
    # Initialize the content of the README
    readme_content = """
# Advent of Code 🎄🎁
Welcome to my Advent of Code solutions!

## Years
"""
    
    # Iterate through each year directory (assuming the directory structure is like `2024`, `2023`, etc.)
    for year in sorted(os.listdir(".")):
        if os.path.isdir(year) and year.isdigit():
            readme_content += f"\n<details>\n<summary>{year}</summary>\n\n"

            # Iterate through each programming language subdirectory
            for lang_dir in sorted(os.listdir(year)):
                lang_path = os.path.join(year, lang_dir)
                if os.path.isdir(lang_path):  # Ensure it's a directory
                    readme_content += f"#### {language_dic.get(lang_dir, lang_dir.capitalize())} Solutions\n\n"
                    readme_content += "| Day | Problem | Solution (Part 1) | Solution (Part 2) |\n"
                    readme_content += "|-----|---------|-------------------|-------------------|\n"

                    # Iterate through each day directory inside the language directory
                for day in sorted((x for x in os.listdir(lang_path) if x.isdigit()), key=lambda x: int(x)):
                        if os.path.isdir(os.path.join(lang_path, day)) and day.isdigit():
                            problem_title = get_problem_title(year, day, lang_dir)  # Get the problem title
                            problem_url = f"https://adventofcode.com/{year}/day/{day}"
                            
                            # Find actual solution files
                            part1_file, part2_file = find_solution_files(year, lang_dir, day)

                            # Build paths to solution files if they exist
                            part1_solution = f"./{year}/{lang_dir}/{day}/{part1_file}" if part1_file else "Not Available"
                            part2_solution = f"./{year}/{lang_dir}/{day}/{part2_file}" if part2_file else "Not Available"
                            
                            # Add row for this day
                            readme_content += f"| {int(day)} | [{problem_title}]({problem_url}) | [Part 1 Solution]({part1_solution}) | {"[Part 2 Solution](" + part2_solution + ")" if part2_solution != "Not Available" else part2_solution} |\n"
            
                readme_content += "\n"

            # Close the details section for the current year
            readme_content += "\n</details>\n"
    
    # Save the generated README content to a file
    with open("README.md", "w") as f:
        f.write(readme_content)
    print("README.md generated successfully!")

if __name__ == "__main__":
    generate_readme()
