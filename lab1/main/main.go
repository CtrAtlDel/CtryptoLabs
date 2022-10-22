package main

import (
	"flag"
	"fmt"
	//"crypto/md5"
)

func main() {
	inputPath := flag.String("input", "0", "input file path")
	outPath := flag.String("output", "", "output file path")
	encoding := flag.String("e", "UTF-16-LE", "encoding for passwords")
	hashFunction := flag.String("hash", "SHA-256", "encoding for file")
	wordCounter := flag.Int("n", 0, "count of words in out file")
	flag.Parse()
	fmt.Println(*inputPath)
	fmt.Println(*outPath)
	fmt.Println(*encoding)
	fmt.Println(*hashFunction)
	fmt.Println(*wordCounter)
}
