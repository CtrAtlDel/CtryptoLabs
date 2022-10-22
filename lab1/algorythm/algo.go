package algorythm

import (
	"bufio"
	"fmt"
	"lab1/stuff"
	"math/rand"
	"os"
	"time"
)

const strLength = 20
const maxCapacityForInputFile = 100

func Algorythm(inputPath, outPath, enc, hf string, counter int) {
	inputFile, _ := os.Open(inputPath)
	scanner := bufio.NewScanner(inputFile)
	defer inputFile.Close()

	const maxCapacity int = maxCapacityForInputFile
	buf := make([]byte, maxCapacity)
	scanner.Buffer(buf, maxCapacity)

	outputFile, _ := os.OpenFile(outPath, os.O_APPEND|os.O_WRONLY, 0600)
	defer outputFile.Close()

	var line string
	hashFunc := stuff.GetHashFunction(stuff.HashFunctions(hf))
	i := 0
	for scanner.Scan() {
		if i < counter {
			line = scanner.Text()
			fmt.Println(string(hashFunc.Sum([]byte(line))))
			outputFile.WriteString(string(hashFunc.Sum([]byte(line))) + "\n")
		}
		i++
	}
}

func writeFile(file *os.File, line string) {
	file.WriteString(line + "\n")
}

func getRandomStr() string {
	rand.Seed(time.Now().UnixNano())
	digits := "0123456789"
	specials := "~=+%^*/()[]{}/!@#$?|"
	alphabet := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	alphabetUpper := "abcdefghijklmnopqrstuvwxyz"
	all := alphabet + alphabetUpper + digits + specials
	buf := make([]byte, strLength)
	buf[0] = digits[rand.Intn(len(digits))]
	buf[1] = specials[rand.Intn(len(specials))]
	for i := 2; i < strLength; i++ {
		buf[i] = all[rand.Intn(len(all))]
	}
	rand.Shuffle(len(buf), func(i, j int) {
		buf[i], buf[j] = buf[j], buf[i]
	})
	return string(buf) + "\n"
}
