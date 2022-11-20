package main

import (
	u "CryptoLabs/lab2/internal/app/utils"
	"flag"
)

var (
	key        string
	mode       string
	initVector string
	file       string
	encryption bool
	decryption bool
	debug      bool
)

func init() {
	flag.StringVar(&key, "k", "", "key in hex")
	flag.StringVar(&mode, "m", "", "mode (ecb or cbc)")
	flag.StringVar(&initVector, "i", "", "key in hex")
	flag.StringVar(&file, "f", "", "file with text")
	flag.BoolVar(&encryption, "e", true, "flag for operation in encryption mode")
	flag.BoolVar(&decryption, "d", false, "flag for operation in decryption mode")
	flag.BoolVar(&debug, "g", false, "flag for operation in debug mode")
}
func main() {
	flag.Parse()
	u.Menu(key, mode, initVector, file, encryption, decryption, debug)
}
