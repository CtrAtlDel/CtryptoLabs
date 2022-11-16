package utils

import (
	"log"
	"os"
)

func ReadFile(filePath string) *os.File {
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatal(err)
	}
	defer func(file *os.File) {
		err := file.Close()
		if err != nil {
			log.Fatal(err)
		}
	}(file)
	return file
}
