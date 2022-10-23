package stuff

import (
	"golang.org/x/text/encoding"
	"golang.org/x/text/encoding/unicode"
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

func GetStringInEncode(enc Encodings) *encoding.Encoder {
	switch enc {
	case Utf16le:
		return unicode.UTF16(unicode.LittleEndian, unicode.IgnoreBOM).NewEncoder()
	case Utf16be:
		return unicode.UTF16(unicode.BigEndian, unicode.IgnoreBOM).NewEncoder()
	}
	return unicode.UTF8.NewEncoder()
}
