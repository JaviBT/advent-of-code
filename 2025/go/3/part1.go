package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func parseInput(file *os.File) ([][]int, error) {
	scanner := bufio.NewScanner(file)

	var lines [][]int
	var err error

	for scanner.Scan() {
		strLine := scanner.Text()
		newLine := make([]int, len(strLine))
		for i := range strLine {
			newLine[i], err = strconv.Atoi(string(strLine[i]))
			if err != nil {
				fmt.Println("Error converting line:", err)
				return nil, err
			}
		}
		lines = append(lines, newLine)
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return nil, err
	}

	return lines, nil
}

func joinDigits(digits []int) int {
	result := 0
	for _, digit := range digits {
		result = result*10 + digit
	}
	return result
}

func maxKDigitsNumber(line []int, k int) int {
	n := len(line)
	resultDigits := []int{}
	currentIndex := 0
	currentK := k

	for i := 0; i < k; i++ {
		max_digit := -1
		max_index := -1
		for j := currentIndex; j < n-currentK+1; j++ {
			if line[j] > max_digit {
				max_digit = line[j]
				max_index = j
			}
		}
		resultDigits = append(resultDigits, max_digit)
		currentIndex = max_index + 1
		currentK--
	}

	return joinDigits(resultDigits)
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
	for _, line := range lines {
		total += maxKDigitsNumber(line, 2)
	}

	fmt.Println(total)
}
