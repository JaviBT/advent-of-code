package main

import (
	"bufio"
	"fmt"
	"os"
)

func parseInput(file *os.File) ([][]string, error) {
	scanner := bufio.NewScanner(file)

	var grid [][]string

	for scanner.Scan() {
		strLine := scanner.Text()
		newLine := make([]string, len(strLine))
		for i := range strLine {
			newLine[i] = string(strLine[i])
		}
		grid = append(grid, newLine)
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return nil, err
	}

	return grid, nil
}

func checkKAdjacent(grid [][]string, x int, y int, k int) bool {
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}}
	khits := 0
	for _, dir := range dirs {
		nx, ny := x + dir[0], y + dir[1]
		if 0 <= nx && nx < len(grid) && 0 <= ny && ny < len(grid[0]) && grid[nx][ny] == "@" {
			khits++
		}
	}
	return khits >= k
}

func main() {
	file, err := os.Open("input.dat")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	lines, err := parseInput(file)
	if err != nil {
		fmt.Println("Error parsing input:", err)
		return
	}

	var total int
	lastIter := -1

	for lastIter != 0 {
		lastIter = 0
		for i := range lines {
			for j := range lines[i] {
				if lines[i][j] == "@" && !checkKAdjacent(lines, i, j, 4) {
					lines[i][j] = "."
					lastIter++
					total++
				}
			}
		}
	}

	fmt.Println(total)
}
