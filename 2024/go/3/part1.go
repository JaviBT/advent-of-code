package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	file, err := os.Open("input.dat")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	reg := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	res := 0

	for scanner.Scan() {
		line := scanner.Text()
		matches := reg.FindAllStringSubmatch(line, -1)

		for _, match := range matches {
			res += toInt(match[1]) * toInt(match[2])
		}
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	fmt.Println(res)
}

func toInt(s string) int {
	num, err := strconv.Atoi(s)
	if err != nil {
		fmt.Printf("Error converting '%s' to int: %v\n", s, err)
		return 0
	}
	return num
}
