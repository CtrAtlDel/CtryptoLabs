package utils

import "lab2/internal/app/mode"

func GetBlocks(str string) [][]byte { //without padding
	dataArray := []byte(str)
	data := dataArray[:] //slice
	numberOfBlocks := len(data) / mode.BlockSize
	result := make([][]byte, numberOfBlocks)
	var begin, end int
	for i := 0; i < numberOfBlocks; i++ {
		begin = i * mode.BlockSize
		end = begin + mode.BlockSize
		result = append(result, data[begin:end])
	}
	return result
}
