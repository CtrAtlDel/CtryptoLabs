package utils

import (
	encrMode "lab2/mode"
	"lab2/mode/algorythms"
)

func Menu(key, mode, initVector, filePath string, encryption, decryption, debug bool) {
	if encryption {
		if mode == encrMode.Ecb {
			algorythms.EncryptionEcb([]byte(key), initVector, ReadFile(filePath), debug)
		} else if mode == encrMode.Cbc {
			algorythms.EncryptionCbc([]byte(key), initVector, ReadFile(filePath), debug)
		}
	} else if decryption {
		if mode == encrMode.Ecb {
			algorythms.DecryptionEcb([]byte(key), initVector, ReadFile(filePath), debug)
		} else if mode == encrMode.Cbc {
			algorythms.DecryptionCbc([]byte(key), initVector, ReadFile(filePath), debug)
		}
	}
}
