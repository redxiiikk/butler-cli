package cmd

import (
	"github.com/redxiiikk/butler-cli/context"
	"github.com/spf13/cobra"
	"os"
)

var (
	autoUpdateConfig = "update.auto"
)

var (
	updateCmd = &cobra.Command{
		Use:   "update",
		Short: "Sync your dotfile",
		Args:  cobra.NoArgs,
		Run: func(cmd *cobra.Command, args []string) {
			configContext := context.NewConfigOperation()
			isAutoUpdate, existed := configContext.Get(autoUpdateConfig)

			if !existed {
				os.Exit(0)
			}

			if isAutoUpdate == "false" {
				os.Exit(0)
			}

			// todo: need implement auto update self
		},
	}
)
