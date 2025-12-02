package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func invalidID(id string) bool {
	if len(id)%2 != 0 {
		return false
	}

	h := int(len(id) / 2)
	fh := id[:h]
	sh := id[h:]

	return fh == sh
}

func main() {
	file, err := os.Open("input.dat")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var inters []string
	var sum int

	for scanner.Scan() {
		ranges := strings.Fields(scanner.Text())

		inters = strings.Split(ranges[0], ",")
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	for _, inter := range inters {
		splitInter := strings.Split(inter, "-")
		start, err := strconv.Atoi(splitInter[0])
		if err != nil {
			fmt.Println("Error converting start:", err)
			return
		}
		end, err := strconv.Atoi(splitInter[1])
		if err != nil {
			fmt.Println("Error converting end:", err)
			return
		}
		for i := start; i <= end; i++ {
			if invalidID(strconv.Itoa(i)) {
				sum += i
			}
		}
	}

	fmt.Println(sum)
}
