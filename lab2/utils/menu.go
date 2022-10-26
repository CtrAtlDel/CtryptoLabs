package utils

import (
	encrMode "lab2/mode"
	"lab2/mode/algorythms"
)

func Menu(key, mode, initVector, filePath string, encryption, decryption, debug bool) {
	if encryption {
		if mode == encrMode.Ecb {
			algorythms.EncryptionEcb(key, initVector, ReadFile(filePath))
		} else if mode == encrMode.Cbc {
			algorythms.EncryptionCbc(key, initVector, ReadFile(filePath))
		}
	} else if decryption {
		if mode == encrMode.Ecb {
			algorythms.DecrtyptionEcb(key, initVector, ReadFile(filePath))
		} else if mode == encrMode.Cbc {
			algorythms.DecrtyptionCbc(key, initVector, ReadFile(filePath))
		}
	}
}
