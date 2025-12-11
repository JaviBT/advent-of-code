package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, err := os.Open("input.dat")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	matrix := [][]rune{}
	for scanner.Scan() {
		parts := scanner.Text()
		runeSlice := []rune(parts)
		matrix = append(matrix, runeSlice)
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	var cnt int
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if matrix[i][j] == 'A' {
				cnt += checkX(matrix, i, j)
			}
		}
	}

	fmt.Println(cnt)
}

func checkX(matrix [][]rune, i int, j int) int {
	var cnt int
	if !((i-1 >= 0) && (j-1 >= 0) && (i+1 < len(matrix)) && (j+1 < len(matrix[i]))) {
		return 0
	}
	// X - MAS
	if (((matrix[i-1][j-1] == 'M') && (matrix[i+1][j+1] == 'S')) || ((matrix[i-1][j-1] == 'S') && (matrix[i+1][j+1] == 'M'))) &&
		(((matrix[i+1][j-1] == 'M') && (matrix[i-1][j+1] == 'S')) || ((matrix[i+1][j-1] == 'S') && (matrix[i-1][j+1] == 'M'))) {
		cnt += 1
	}
	return cnt
}
