package algorythm

import (
	"bufio"
	"lab1/stuff"
	"log"
	"math/rand"
	"os"
)

const minLengthString = 10
const maxLengthString = 20
const maxCapacityForInputFile = 100

func Algorythm(inputPath, outPath, hf string, enc stuff.Encodings, counter int) {
	inputFile, err := os.Open(inputPath)
	if err != nil {
		log.Fatal(err)
	}
	scanner := bufio.NewScanner(inputFile)
	defer inputFile.Close()

	const maxCapacity int = maxCapacityForInputFile
	buf := make([]byte, maxCapacity)
	scanner.Buffer(buf, maxCapacity)

	outputFile, err := os.OpenFile(outPath, os.O_APPEND|os.O_WRONLY, 0600)
	if err != nil {
		log.Fatal(err)
	}

	var line string
	hashFunc := stuff.GetHashFunction(stuff.HashFunctions(hf))

	i := 0
	for scanner.Scan() {
		if i < counter {
			line = scanner.Text()
			lineEnc := stuff.GetStringInEncode(line, enc)
			outputFile.WriteString(string(hashFunc.Sum([]byte(lineEnc))) + "\n")
		} else {
			outputFile.WriteString(getRandomStr())
		}
		i++
	}
	defer outputFile.Close()
}

func getRandomStr() string {
	strLength := rand.Intn(maxLengthString-minLengthString) + minLengthString
	var letters = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
	s := make([]rune, strLength)
	for i := range s {
		s[i] = letters[rand.Intn(len(letters))]
	}
	return string(s) + "\n"
}
