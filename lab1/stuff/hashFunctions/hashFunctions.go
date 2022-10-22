package hashFunctions

type HashFunction string

const (
	Md4    HashFunction = "md4"
	Md5                 = "md5"
	Sha1                = "sha1"
	Sha256              = "sha256"
	Sha512              = "sha512"
)

func CheckHashFunctions(hf HashFunction) bool {
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
