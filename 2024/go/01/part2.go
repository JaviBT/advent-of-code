package main

import (
	"bufio"
	"fmt"
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

	map2 := make(map[int]int)
	for _, num := range list2 {
		map2[num]++
	}

	sc := 0
	for _, num := range list1 {
		sc += num * map2[num]
	}

	fmt.Println(sc)
}
