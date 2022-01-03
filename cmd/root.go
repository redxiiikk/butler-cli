package cmd

import (
    "github.com/spf13/cobra"
)

var (
    rootCmd = &cobra.Command{
        Use:   "butler",
        Short: "Help You Managerment computer",
    }
)

func Execute() error {
    return rootCmd.Execute()
}

func init() {
    rootCmd.AddCommand(dotfileCmd)
}
