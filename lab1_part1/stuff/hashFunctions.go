package stuff

import (
	"crypto/md5"
	"crypto/sha1"
	"crypto/sha256"
	"crypto/sha512"
	"golang.org/x/crypto/md4"
	"hash"
)

type HashFunctions string

const (
	Md4    HashFunctions = "md4"
	Md5                  = "md5"
	Sha1                 = "sha1"
	Sha256               = "sha256"
	Sha512               = "sha512"
)

func CheckHashFunctions(hf HashFunctions) bool {
	switch hf {
	case Md4:
		return true
	case Md5:
		return true
	case Sha1:
		return true
	case Sha256:
		return true
	case Sha512:
		return true
	}
	return false
}

func GetHashFunction(hf HashFunctions) hash.Hash {
	switch hf {
	case Md4:
		return md4.New()
	case Md5:
		return md5.New()
	case Sha1:
		return sha1.New()
	case Sha256:
		return sha256.New()
	case Sha512:
		return sha512.New()
	}
	return sha256.New()
}
