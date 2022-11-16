package algorythms

import (
	"fmt"
	"io"
	"lab2/mode"
	"lab2/mode/keyGen"
	"log"
	"os"
)

func EncryptionEcb(key []byte, filePath string, debug bool) {
	key0 := key
	key1 := keyGen.GetKey1(key0)
	key2 := keyGen.GetKey2(key0, key1)
	if debug {
		fmt.Println("Key0: ", key0)
		fmt.Println("Key1: ", key1)
		fmt.Println("Key2: ", key2)
	}
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
	buffer := make([]byte, mode.BlockSize)
	//add padding check
	for {
		data, err := file.Read(buffer)
		fmt.Println(data)
		if err == io.EOF {
			break
		}
	}
}

//roundEcryption ...
func roundEncryption(block, key []byte) {
}

// encryptBlock ...
func encryptBlock(block, key []byte) {

}

func DecryptionEcb(key []byte, filePath string, debug bool) {

}
