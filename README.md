# strategy-configs

The idea behind [strategy-configs](https://github.com/hacbs-release/strategy-configs) is to offer an up-to-date repository with Release Strategies' configuration files examples and workflows to validate them.

To include this repository as part of your workflow and keep adding new files, [fork this repository](https://github.com/hacbs-release/strategy-configs/fork) and use the [example config file](example.yaml) as a starting point.

## Validation

This repository defines a [GitHub workflow](.github/workflows/schema_validation.yaml) that runs every single time a new Pull Request is opened. This workflow will get all the new configuration files, added or modified, and will ensure that they follow the [specification](.github/schema.json).

In case that the validation of any of the new files fails, the CI will show an error and a small description of the problem.

## Getting the latest changes

From time to time, the HACBS Release team will update the [schema](.github/schema.json) that validates the configuration files in this repository. This could be an update to fix errors in the current schema, or the addition of a new feature.

To get the latest changes into your repo, [sync your fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) either [from the UI](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork#syncing-a-fork-from-the-web-ui) or [from the command line](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork#syncing-a-fork-from-the-command-line).

## Configuration examples

This repository contains an [example configuration](example.yaml) file with all the features that can be used in HACBS Release Strategies. For more information on the values you can set for each field, we recommend taking a look at the [schema](.github/schema.json) used to validate configuration files.
