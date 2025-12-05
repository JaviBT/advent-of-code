package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func parseInput(file *os.File) ([][]int, error) {
	scanner := bufio.NewScanner(file)

	var ranges [][]int

	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}
		parts := strings.Split(line, "-")
		start, err := strconv.Atoi(parts[0])
		if err != nil {
			fmt.Println("Error converting start:", err)
			return nil, err
		}
		end, err := strconv.Atoi(parts[1])
		if err != nil {
			fmt.Println("Error converting end:", err)
			return nil, err
		}
		ranges = append(ranges, []int{start, end})
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading ranges from file:", err)
		return nil, err
	}

	return ranges, nil
}

func sortRanges(ranges [][]int) {
	sort.Slice(ranges, func(i, j int) bool {
		return ranges[i][0] < ranges[j][0]
	})
}

func sizeRanges(ranges [][]int) int {
	total := 0
	for _, r := range ranges {
		total += r[1] - r[0] + 1
	}
	return total
}

func mergeRanges(ranges [][]int) [][]int {
	var mergedRanges [][]int
	curStart := ranges[0][0]
	curEnd := ranges[0][1]

	for _, newRange := range ranges[1:] {
		newStart, newEnd := newRange[0], newRange[1]
		if newStart <= curEnd+1 {
			curEnd = max(curEnd, newEnd)
		} else {
			mergedRanges = append(mergedRanges, []int{curStart, curEnd})
			curStart, curEnd = newStart, newEnd
		}
	}
	mergedRanges = append(mergedRanges, []int{curStart, curEnd})

	return mergedRanges
}

func main() {
	file, err := os.Open("input.dat")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	ranges, err := parseInput(file)
	if err != nil {
		fmt.Println("Error parsing input:", err)
		return
	}

	sortRanges(ranges)

	mergedRanges := mergeRanges(ranges)
	total := sizeRanges(mergedRanges)

	fmt.Println(total)
}
