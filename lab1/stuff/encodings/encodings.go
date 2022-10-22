package encodings

type Encodings string

const (
	Ascii   Encodings = "ascii"
	Utf8              = "utf8"
	Utf16le           = "utf-16-le"
	Utf16be           = "utf-16-be"
)

func CheckEncodings(enc Encodings) bool {
	switch enc {
	case Ascii:
		return true
	case Utf8:
		return true
	case Utf16le:
		return true
	case Utf16be:
		return true
	}
	return false
}
