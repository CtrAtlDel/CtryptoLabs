package main

import (
	"flag"
	encrMode "lab2/mode"
)

func main() {
	menu(parser())
	flag.Parse()
}

func parser() (string, string, string, bool, bool, bool) {
	key := flag.String("k", "", "key in hex")
	mode := flag.String("m", "", "mode (ecb or cbc)")
	initVector := flag.String("i", "", "key in hex")
	encryption := flag.Bool("e", true, "flag for operation in encryption mode")
	decryption := flag.Bool("d", false, "flag for operation in decryption mode")
	debug := flag.Bool("g", false, "flag for operation in debug mode")
	flag.Parse()
	encrMode.CheckMode(encrMode.Mode(*mode))
	return *key, *mode, *initVector, *encryption, *decryption, *debug
}

func menu(key, mode, initVector string, encryption, decryption, debug bool) {
	if encryption {
		if mode == encrMode.Ecb {
			
		} else if mode == encrMode.Cbc {

		}
	} else if decryption {
		if mode == encrMode.Ecb {

		} else if mode == encrMode.Cbc {

		}
	}
}
