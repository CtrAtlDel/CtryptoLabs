package utils

import (
	"CryptoLabs/lab2/internal/app/mode/algorythms"
	encrMode "lab2/internal/app/mode"
)

func Menu(key, mode, initVector, filePath string, encryption, decryption, debug bool) {
	if encryption {
		if mode == encrMode.Ecb {
			algorythms.EncryptionEcb([]byte(key), filePath, debug)
		} else if mode == encrMode.Cbc {
			algorythms.EncryptionCbc([]byte(key), initVector, filePath, debug)
		}
	} else if decryption {
		if mode == encrMode.Ecb {
			algorythms.DecryptionEcb([]byte(key), filePath, debug)
		} else if mode == encrMode.Cbc {
			algorythms.DecryptionCbc([]byte(key), initVector, filePath, debug)
		}
	}
}