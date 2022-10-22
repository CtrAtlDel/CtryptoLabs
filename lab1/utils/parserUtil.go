package parser

import (
	"flag"
	"fmt"
)

type Parser struct {
	InputPath    string
	OutPath      string
	Encoding     string
	HashFunction string
	WordCounter  int
}

func (p *Parser) Parser() *Parser {
	inputPath := flag.String("input", "./", "input file path")
	outPath := flag.String("output", "./", "output file path")
	encoding := flag.String("e", "UTF-16-LE", "encoding for passwords")
	hashFunction := flag.String("hash", "SHA-256", "encoding for file")
	wordCounter := flag.Int("n", 1, "count of words in out file")
	flag.Parse()
	p.OutPath = *outPath
	p.InputPath = *inputPath
	p.Encoding = *encoding
	p.HashFunction = *hashFunction
	p.WordCounter = *wordCounter
	fmt.Println(p.WordCounter)
	return p
}
