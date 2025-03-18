package main

import (
	"bufio"
	"fmt"
	"math"
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
	defer file.Close()

	scanner := bufio.NewScanner(file)

	cnt := 0
	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())
		copyParts := make([]string, len(parts))
		copy(copyParts, parts)

		safe := isSafe(parts)
		if safe {
			cnt++
			continue
		}

		for i := 0; i < len(parts); i++ {
			newParts := make([]string, len(parts))
			copy(newParts, copyParts)
			newParts = append(newParts[:i], newParts[i+1:]...)

			safe = isSafe(newParts)
			if safe {
				cnt++
				break
			}
		}
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	fmt.Println(cnt)
}

func isSafe(report []string) bool {
	monotoneus := ""
	for i := 1; i < len(report); i++ {
		num1, err := strconv.Atoi(report[i-1])
		if err != nil {
			fmt.Println("Error converting number:", err)
			return false
		}

		num2, err := strconv.Atoi(report[i])
		if err != nil {
			fmt.Println("Error converting number:", err)
			return false
		}

		if (int(math.Abs(float64(num1-num2))) == 0 || int(math.Abs(float64(num1-num2))) > 3) ||
			(monotoneus == "asc" && num1 > num2) ||
			(monotoneus == "desc" && num1 < num2) {
			return false
		}

		if monotoneus == "" {
			if num1 < num2 {
				monotoneus = "asc"
			} else {
				monotoneus = "desc"
			}
		}
	}

	return true
}

func printList(list []string) {
	for _, num := range list {
		fmt.Printf("%s ", num)
	}
	fmt.Println()
}
