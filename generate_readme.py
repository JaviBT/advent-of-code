import os

def get_problem_title(year, day):
    """Reads the first line of the problem.txt file to get the problem title."""
    problem_file_path = os.path.join(year, str(day), "problem.txt")
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
            readme_content += "| Day | Problem | Solution (Part 1) | Solution (Part 2) |\n"
            readme_content += "|-----|---------|-------------------|-------------------|\n"
            
            # Iterate through each day inside the year folder
            for day in sorted(os.listdir(year)):
                if os.path.isdir(os.path.join(year, day)) and day.isdigit():
                    problem_title = get_problem_title(year, day)  # Get the problem title from the problem.txt file
                    problem_url = f"https://adventofcode.com/{year}/day/{day}"
                    
                    # Assuming the solution files are named like `part1.py`, `part2.py`
                    part1_solution = f"./{year}/{day}/part1.py"
                    part2_solution = f"./{year}/{day}/part2.py"
                    
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
