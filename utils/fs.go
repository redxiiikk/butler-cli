package utils

import "io/fs"

func IsSymlink(mode fs.FileMode) bool {
	return mode&fs.ModeSymlink != 0
}
