import os

language_dic = {
    'python': '🐍 Python'
}

def get_problem_title(year, day, lang_dir):
    """Reads the first line of the problem.txt file to get the problem title."""
    problem_file_path = os.path.join(year, lang_dir, str(day), "problem.txt")
    try:
        with open(problem_file_path, 'r') as file:
            return file.readline().strip().split('--- ')[1].split(' ---')[0]  # Read the first line and remove leading/trailing spaces
    except FileNotFoundError:
        return f"Problem for Day {day} not found"

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
            readme_content += f"### Solutions for Advent of Code {year}\n\n"

            # Iterate through each programming language subdirectory
            for lang_dir in sorted(os.listdir(year)):
                lang_path = os.path.join(year, lang_dir)
                if os.path.isdir(lang_path):  # Ensure it's a directory
                    readme_content += f"#### {language_dic.get(lang_dir, lang_dir.capitalize())} Solutions\n\n"
                    readme_content += "| Day | Problem | Solution (Part 1) | Solution (Part 2) |\n"
                    readme_content += "|-----|---------|-------------------|-------------------|\n"

                    # Iterate through each day directory inside the language directory
                    for day in sorted(os.listdir(lang_path)):
                        if os.path.isdir(os.path.join(lang_path, day)) and day.isdigit():
                            problem_title = get_problem_title(year, day, lang_dir)  # Get the problem title
                            problem_url = f"https://adventofcode.com/{year}/day/{day}"
                            
                            # Assuming the solution files are named like `part1.py`, `part2.py` (or appropriate extensions for the language)
                            part1_solution = f"./{year}/{lang_dir}/{day}/part1.{lang_dir.lower()}"
                            part2_solution = f"./{year}/{lang_dir}/{day}/part2.{lang_dir.lower()}"
                            
                            # Add row for this day
                            readme_content += f"| {day} | [{problem_title}]({problem_url}) | [Part 1 Solution]({part1_solution}) | [Part 2 Solution]({part2_solution}) |\n"
            
            # Close the details section for the current year
            readme_content += "\n</details>\n"
    
    # Save the generated README content to a file
    with open("README.md", "w") as f:
        f.write(readme_content)
    print("README.md generated successfully!")

if __name__ == "__main__":
    generate_readme()
