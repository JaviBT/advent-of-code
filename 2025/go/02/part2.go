package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func invalidID(id string) bool {
	for l := 1; l < len(id); l++ {
		if len(id)%l != 0 {
			continue
		}

		k := len(id) / l
		seq := id[:l]
		kseq := strings.Repeat(seq, k)

		if kseq == id {
			return true
		}
	}

	return false
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
