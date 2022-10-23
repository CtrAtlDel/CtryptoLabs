package algorythm

import (
	"bufio"
	"golang.org/x/text/encoding"
	"golang.org/x/text/transform"
	"hash"
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
	scanner.Split(bufio.ScanLines)
	defer inputFile.Close()

	const maxCapacity int = maxCapacityForInputFile
	buf := make([]byte, maxCapacity)
	scanner.Buffer(buf, maxCapacity)
	scanner.Split(bufio.ScanLines)

	outputFile, err := os.OpenFile(outPath, os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatal(err)
	}

	hashFunc := stuff.GetHashFunction(stuff.HashFunctions(hf))
	encode := stuff.GetStringInEncode(stuff.Encodings(enc))

	i := 0
	for scanner.Scan() {
		if i < counter {
			line := scanner.Text()
			byteLine := getByte(hashFunc, encode, line)
			outputFile.WriteString(string(byteLine) + "\n")
		} else {
			outputFile.WriteString(getRandomStr())
		}
		i++
	}
	defer outputFile.Close()
}

func getByte(hash hash.Hash, encodings *encoding.Encoder, str string) []byte {
	enc := encodings
	hasher := hash
	t := transform.NewWriter(hasher, enc)
	_, err := t.Write([]byte(str))
	if err != nil {
		log.Fatal(err)
	}
	return hasher.Sum(nil)
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
