package main

import (
	"flag"
	"fmt"
	"lab1/algorythm"
	"lab1/stuff"
	"os"
)

func main() {
	inputPath := flag.String("input", "./", "input file path")
	outPath := flag.String("output", "./", "output file path")
	encoding := flag.String("e", "utf8", "encoding")
	hashFunction := flag.String("h", "sha256", "hash function")
	wordCounter := flag.Int("n", 1, "count of words in out file")
	flag.Parse()
	checkArgs(*hashFunction, *encoding)
	algorythm.Algorythm(*inputPath, *outPath, *hashFunction,
		*hashFunction, *wordCounter)
}

func checkArgs(hf string, enc string) {
	if !(stuff.CheckHashFunctions(stuff.HashFunctions(hf)) &&
		stuff.CheckEncodings(stuff.Encodings(enc))) {
		fmt.Println("Hash function or encoding is incorrect or not supported...")
		os.Exit(1)
	}
}
