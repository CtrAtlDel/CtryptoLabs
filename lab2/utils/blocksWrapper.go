package utils

import (
	"lab2/mode"
	"math"
)

func GetBlocks(str string) [][]byte {
	dataArray := []byte(str)
	data := dataArray[:] //slice
	numberOfBlocks := int(math.Ceil(float64(len(data) / mode.BlockSize)))
	result := make([][]byte, numberOfBlocks)
	var begin, end int
	for i := 0; i < numberOfBlocks; i++ {
		begin = i * mode.BlockSize
		end = begin + mode.BlockSize
		result = append(result, data[begin:end])
	}
	return result
}
