package keyGen

func GetKey1(key []byte) []byte {
	return byteInversion(key)
}

func GetKey2(key0, key1 []byte) []byte {
	return Xor(key0, key1)
}

func byteInversion(key []byte) []byte {
	for i, j := 0, len(key)-1; i < j; i, j = i+1, j-1 {
		key[i], key[j] = key[j], key[i]
	}
	return key
}

func Xor(array0, array1 []byte) []byte {
	var result []byte
	for i := range array0 {
		result[i] = array0[i] ^ array1[i]
	}
	return result
}
