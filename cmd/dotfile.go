package cmd

import (
	"errors"
	"fmt"
	"io/fs"
	"log"
	"os"
	"path"
	"path/filepath"
	"strings"

	"github.com/redxiiikk/butler-cli/context"
	"github.com/redxiiikk/butler-cli/utils"
	"github.com/spf13/cobra"
)

const (
	repoLocalPathConfig = "dotfile.repo.local"
)

var (
	dotfileCmd = &cobra.Command{
		Use:   "dotfile",
		Short: "Sync your dotfile",
		Args:  cobra.MaximumNArgs(1),
		Run: func(cmd *cobra.Command, args []string) {
			configContext := context.NewConfigOperation()
			isNeedUpdate := false

			var dotfileRepoPath = ""
			if len(args) == 0 {
				dotfileRepoPath, _ = configContext.Get(repoLocalPathConfig)
			} else {
				dotfileRepoPath = args[0]
				isNeedUpdate = true
			}

			if dotfileRepoPath == "" {
				log.Fatal("need input dotfile repo path")
			}

			if !path.IsAbs(dotfileRepoPath) {
				currentDir, _ := os.Getwd()
				dotfileRepoPath = path.Join(currentDir, dotfileRepoPath)
			}

			if err := checkRepoPath(dotfileRepoPath); err != nil {
				_ = fmt.Errorf("repo path is wrong, place check args: %s", dotfileRepoPath)
				return
			}

			if err := doHandleDotfileRepo(dotfileRepoPath); err != nil {
				_ = fmt.Errorf("dotfile sync error: %s", err)
			}

			if isNeedUpdate {
				configContext.Set(repoLocalPathConfig, dotfileRepoPath)
			}
		},
	}
)

func checkRepoPath(dotfileRepoPath string) error {
	stat, err := os.Stat(dotfileRepoPath)

	if os.IsNotExist(err) || !stat.IsDir() {
		return errors.New("dotfile repo is not existed or not a dir, place check args")
	}

	return nil
}

func doHandleDotfileRepo(dotfileRepoPath string) error {
	return filepath.WalkDir(dotfileRepoPath, func(dotfilePath string, d fs.DirEntry, err error) error {
		if d.Name()[0] == '.' {
			if d.IsDir() {
				return filepath.SkipDir
			}
			return nil
		}

		if !isInDotfileRepo(dotfileRepoPath, dotfilePath) {
			return nil
		}

		symlinkPath := os.Getenv("HOME") + "/." + dotfilePath[len(dotfileRepoPath)+1:]

		if d.IsDir() {
			if _, err := os.Stat(symlinkPath); os.IsNotExist(err) {
				_ = os.Mkdir(symlinkPath, 0755)
			}
			return nil
		}

		if stat, err := os.Lstat(symlinkPath); err == nil {
			if utils.IsSymlink(stat.Mode()) {
				symlinkRealPath, _ := filepath.EvalSymlinks(symlinkPath)
				if symlinkRealPath == dotfilePath {
					return nil
				} else {
					_ = os.Remove(symlinkRealPath)
				}
			} else {
				_ = os.Remove(symlinkPath)
			}
		}

		fmt.Printf("CREATE: %60s -> %s\n", symlinkPath, dotfilePath)
		return os.Symlink(dotfilePath, symlinkPath)
	})
}

func isInDotfileRepo(repo, dotfile string) bool {
	if repo == dotfile {
		return false
	}

	if !strings.HasPrefix(dotfile, repo) {
		return false
	}

	return true
}
