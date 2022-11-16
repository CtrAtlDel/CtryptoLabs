package utils

import (
	"flag"
	"fmt"
	encrMode "lab2/mode"
	"os"
)

func Parser() (string, string, string, string, bool, bool, bool) {
	key := flag.String("k", "", "key in hex")
	mode := flag.String("m", "", "mode (ecb or cbc)")
	initVector := flag.String("i", "", "key in hex")
	file := flag.String("f", "", "file with text")
	encryption := flag.Bool("e", true, "flag for operation in encryption mode")
	decryption := flag.Bool("d", false, "flag for operation in decryption mode")
	debug := flag.Bool("g", false, "flag for operation in debug mode")
	flag.Parse()
	encrMode.CheckMode(encrMode.Mode(*mode))
	checkInitVector(*initVector)
	return *key, *mode, *initVector, *file, *encryption, *decryption, *debug
}

func checkInitVector(initVector string) {
	if initVector == "" {
		fmt.Println("Empty init vector...")
		os.Exit(1)
	}
}

func checkKey(key []byte) {
	if len(key) != 4 {
		fmt.Println("Key size is not 32 bits...")
		os.Exit(1)
	}
}
