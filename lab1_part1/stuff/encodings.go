package stuff

import (
	"golang.org/x/text/encoding/unicode"
	"golang.org/x/text/transform"
	"unicode/utf8"
)

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

func GetStringInEncode(str string, enc Encodings) string {
	switch enc {
	case Ascii:
		some := make([]byte, utf8.RuneCountInString(str))
		i := 0
		for _, r := range str {
			some[i] = byte(r)
			i++
		}
		return string(some)
	case Utf16le:
		result, _, _ := transform.Bytes(unicode.UTF16(unicode.LittleEndian,
			unicode.IgnoreBOM).NewEncoder(), []byte(str))
		return string(result)
	case Utf16be:
		result, _, _ := transform.Bytes(unicode.UTF16(unicode.BigEndian,
			unicode.IgnoreBOM).NewEncoder(), []byte(str))
		return string(result)
	}
	return str
}
