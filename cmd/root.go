package cmd

import (
	"github.com/spf13/cobra"
)

var (
	rootCmd = &cobra.Command{
		Use:   "butler",
		Short: "Help You Management computer",
	}
)

func Execute() error {
	return rootCmd.Execute()
}

func init() {
	rootCmd.AddCommand(dotfileCmd)
	rootCmd.AddCommand(updateCmd)
}
