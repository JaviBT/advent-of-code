package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input.dat")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}

	scanner := bufio.NewScanner(file)

	adjMatrix := make(map[int][]int)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}
		nums := strings.Split(line, "|")
		adjMatrix[toInt(nums[1])] = append(adjMatrix[toInt(nums[1])], toInt(nums[0]))
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	var cnt int
	for scanner.Scan() {
		line := scanner.Text()
		order := strings.Split(line, ",")

		if isValidOrder(order, adjMatrix) {
			mid := int(len(order) / 2)
			cnt += toInt(order[mid])
		}
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	fmt.Println(cnt)
}

func isValidOrder(order []string, adjMatrix map[int][]int) bool {
	for i := 0; i < len(order); i++ {
		for _, dep := range adjMatrix[toInt(order[i])] {
			if contains(order[i+1:], dep) {
				return false
			}
		}
	}
	return true
}

func toInt(s string) int {
	num, err := strconv.Atoi(s)
	if err != nil {
		fmt.Println("Error converting string to int:", err)
		return -1
	}
	return num
}

func contains(s []string, e int) bool {
	for _, a := range s {
		if toInt(a) == e {
			return true
		}
	}
	return false
}
