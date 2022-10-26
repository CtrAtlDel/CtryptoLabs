package mode

import (
	"fmt"
	"os"
)

type Mode string

const (
	Ecb = "ecb"
	Cbc = "cbc"
)

func CheckMode(mode Mode) bool {
	switch mode {
	case Ecb:
		return true
	case Cbc:
		return false
	}
	fmt.Println("Unsupported mode...")
	os.Exit(1)
	return false
}
