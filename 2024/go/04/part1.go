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
			if matrix[i][j] == 'X' {
				cnt += checkAll(matrix, i, j)
			}
		}
	}

	fmt.Println(cnt)
}

func checkHorizontal(matrix [][]rune, i int, j int) int {
	var cnt int
	// Check Left
	if (j-3 >= 0) && (matrix[i][j-1] == 'M') && (matrix[i][j-2] == 'A') && (matrix[i][j-3] == 'S') {
		cnt += 1
	}
	// Check Right
	if (j+3 < len(matrix[i])) && (matrix[i][j+1] == 'M') && (matrix[i][j+2] == 'A') && (matrix[i][j+3] == 'S') {
		cnt += 1
	}
	return cnt
}

func checkVertical(matrix [][]rune, i int, j int) int {
	var cnt int
	// Check Up
	if (i-3 >= 0) && (matrix[i-1][j] == 'M') && (matrix[i-2][j] == 'A') && (matrix[i-3][j] == 'S') {
		cnt += 1
	}
	// Check Down
	if (i+3 < len(matrix)) && (matrix[i+1][j] == 'M') && (matrix[i+2][j] == 'A') && (matrix[i+3][j] == 'S') {
		cnt += 1
	}
	return cnt
}

func checkDiagonal(matrix [][]rune, i int, j int) int {
	var cnt int
	// Check Up Left
	if (i-3 >= 0) && (j-3 >= 0) && (matrix[i-1][j-1] == 'M') && (matrix[i-2][j-2] == 'A') && (matrix[i-3][j-3] == 'S') {
		cnt += 1
	}
	// Check Up Right
	if (i-3 >= 0) && (j+3 < len(matrix[i])) && (matrix[i-1][j+1] == 'M') && (matrix[i-2][j+2] == 'A') && (matrix[i-3][j+3] == 'S') {
		cnt += 1
	}
	// Check Down Left
	if (i+3 < len(matrix)) && (j-3 >= 0) && (matrix[i+1][j-1] == 'M') && (matrix[i+2][j-2] == 'A') && (matrix[i+3][j-3] == 'S') {
		cnt += 1
	}
	// Check Down Right
	if (i+3 < len(matrix)) && (j+3 < len(matrix[i])) && (matrix[i+1][j+1] == 'M') && (matrix[i+2][j+2] == 'A') && (matrix[i+3][j+3] == 'S') {
		cnt += 1
	}
	return cnt
}

func checkAll(matrix [][]rune, i int, j int) int {
	var cnt int
	cnt += checkHorizontal(matrix, i, j)
	cnt += checkVertical(matrix, i, j)
	cnt += checkDiagonal(matrix, i, j)
	return cnt
}
