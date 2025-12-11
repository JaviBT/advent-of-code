package main

import (
	"bufio"
	"fmt"
	"os"
)

type GuardPosition rune

type Situation struct {
	guard GuardPosition
	x, y  int
}

const (
	GUA_UP    GuardPosition = '^'
	GUA_DOWN  GuardPosition = 'v'
	GUA_LEFT  GuardPosition = '<'
	GUA_RIGHT GuardPosition = '>'

	OBS = '#'
	EMP = '.'
)

func main() {
	file, err := os.Open("input.dat")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}

	scanner := bufio.NewScanner(file)

	// Load the grid
	grid := make([][]rune, 0)
	for scanner.Scan() {
		line := scanner.Text()

		grid = append(grid, []rune(line))
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Locate the guard's initial position
	guard := GUA_UP
	var guardX, guardY int
	for y, row := range grid {
		for x, cell := range row {
			if cell == rune(guard) {
				guardX, guardY = x, y
			}
		}
	}

	cnt := 0
	for y, row := range grid {
		for x, cell := range row {
			if cell == EMP {
				grid[y][x] = OBS
				if checkLoop(guard, guardX, guardY, grid) {
					cnt += 1
				}
				grid[y][x] = EMP
			}
		}
	}

	fmt.Println(cnt)
}

func checkLoop(guard GuardPosition, guardX, guardY int, grid [][]rune) bool {
	var visited map[Situation]bool = make(map[Situation]bool)
	for inbounds(guardX, guardY, len(grid[0]), len(grid)) {
		if visited[Situation{guard, guardX, guardY}] {
			return true
		}
		visited[Situation{guard, guardX, guardY}] = true

		newX, newY := moveGuard(guard, guardX, guardY)
		if inbounds(newX, newY, len(grid[0]), len(grid)) && grid[newY][newX] == OBS {
			guard = rotateGuard(guard)
			continue
		}
		guardX, guardY = newX, newY
	}

	return false
}

func rotateGuard(guard GuardPosition) GuardPosition {
	switch guard {
	case GUA_UP:
		return GUA_RIGHT
	case GUA_RIGHT:
		return GUA_DOWN
	case GUA_DOWN:
		return GUA_LEFT
	case GUA_LEFT:
		return GUA_UP
	}
	panic(fmt.Sprintf("Invalid guard position: %c", guard))
}

func moveGuard(guard GuardPosition, x, y int) (int, int) {
	switch guard {
	case GUA_UP:
		return x, y - 1
	case GUA_DOWN:
		return x, y + 1
	case GUA_LEFT:
		return x - 1, y
	case GUA_RIGHT:
		return x + 1, y
	}
	panic(fmt.Sprintf("Invalid guard position: %c", guard))
}

func inbounds(x, y, maxX, maxY int) bool {
	return x >= 0 && x < maxX && y >= 0 && y < maxY
}
