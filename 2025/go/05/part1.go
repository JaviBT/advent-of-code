package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseInput(file *os.File) ([][]int, []int, error) {
	scanner := bufio.NewScanner(file)

	var ranges [][]int
	var ingredients []int

	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}
		parts := strings.Split(line, "-")
		start, err := strconv.Atoi(parts[0])
		if err != nil {
			fmt.Println("Error converting start:", err)
			return nil, nil, err
		}
		end, err := strconv.Atoi(parts[1])
		if err != nil {
			fmt.Println("Error converting end:", err)
			return nil, nil, err
		}
		ranges = append(ranges, []int{start, end})
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading ranges from file:", err)
		return nil, nil, err
	}

	for scanner.Scan() {
		ingredient, err := strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Println("Error converting ingredient:", err)
			return nil, nil, err
		}
		ingredients = append(ingredients, ingredient)
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading ingredients from file:", err)
		return nil, nil, err
	}

	return ranges, ingredients, nil
}

func checkFreshness(ingredient int, ranges [][]int) bool {
	for _, r := range ranges {
		if ingredient >= r[0] && ingredient <= r[1] {
			return true
		}
	}
	return false
}

func main() {
	file, err := os.Open("input.dat")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	ranges, ingredients, err := parseInput(file)
	if err != nil {
		fmt.Println("Error parsing input:", err)
		return
	}

	var total int
	for _, ingredient := range ingredients {
		if checkFreshness(ingredient, ranges) {
			total++
		}
	}

	fmt.Println(total)
}
