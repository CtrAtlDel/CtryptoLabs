package algorythms

import (
	"fmt"
	"lab2/mode/keyGen"
	"os"
)

func EncryptionEcb(key []byte, initVector string, file *os.File, debug bool) {
	key0 := key
	key1 := keyGen.GetKey1(key0)
	key2 := keyGen.GetKey2(key0, key1)
	if debug {
		fmt.Println("Key0: ", key0)
		fmt.Println("Key1: ", key1)
		fmt.Println("Key2: ", key2)
	}
	
}

func DecryptionEcb(key []byte, initVector string, file *os.File, debug bool) {

}
