package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
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

	var list1 []int
	var list2 []int

	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())

		num1, err := strconv.Atoi(parts[0])
		if err != nil {
			fmt.Println("Error converting number:", err)
			return
		}

		num2, err := strconv.Atoi(parts[1])
		if err != nil {
			fmt.Println("Error converting number:", err)
			return
		}

		list1 = append(list1, num1)
		list2 = append(list2, num2)
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	sort.Ints(list1)
	sort.Ints(list2)

	diff := 0
	for i := 0; i < len(list1); i++ {
		diff += int(math.Abs(float64(list1[i] - list2[i])))
	}

	fmt.Println(diff)
}
