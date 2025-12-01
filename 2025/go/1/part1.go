package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Move struct {
	Dir  string
	Dist int
}

func main() {
	file, err := os.Open("input.dat")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var l []Move
	
	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())	

		dir := string(parts[0][0])

		move, err := strconv.Atoi(string(parts[0][1:]))
		if err != nil {
			fmt.Println("Error converting move:", err)
			return
		}

		l = append(l, Move{dir, move})
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	count := 0
	dial := 50
	for _, m := range l {
		if m.Dir == "L" {
			dial = (dial - m.Dist) % 100
		} else if m.Dir == "R" {
			dial = (dial + m.Dist) % 100
		}

		if dial == 0 {
			count++
		}
	}

	fmt.Println(count)
}
