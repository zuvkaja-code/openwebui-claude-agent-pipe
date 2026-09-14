# Valves Documentation

This document describes all the valves available for the Open WebUI Claude Agent Pipe function.

## General Valves

- **CLAUDE_CODE_OAUTH_TOKEN**: The OAuth token for accessing the Claude Code API.
- **WORKDIR_ROOT**: The root directory where working directories for each chat are created.
- **CLAUDE_CONFIG_DIR**: The directory where the Claude Code CLI stores session transcripts.
- **PERMISSION_MODE**: The permission mode for the function, which can be `bypassPermissions` (default) or `restricted`.
- **ALLOWED_TOOLS**: A list of tools that are allowed to be used by the agent.
- **MODELS**: A list of extra model IDs that can be used with the function.

## Advanced Valves

- **SETTING_SOURCES**: A comma-separated list of sources for loading settings and instructions. Options include `user`, `project`, and `local`.
- **REPO_MAP**: A mapping of repository names to their paths, used for `#repo:` chats.
- **SCAN_TMP_ARTIFACTS**: A boolean flag to enable scanning of artifacts in `/tmp`.
- **EFFORT_LEVEL**: The effort level for the agent, which can be `low`, `medium`, or `high`.
- **FALLBACK_MODEL**: The fallback model to use if the primary model is unavailable.

## Security Valves

- **REDACTION_PATTERNS**: Additional patterns to use for redaction of sensitive information.
- **IS_SANDBOX**: A boolean flag to enable sandbox mode for the CLI.

## Usage Valves

- **USAGE_WINDOWS**: A list of usage windows for tracking API usage.
- **USAGE_LIMITS**: A list of usage limits for different models.

Each valve is described in detail in the code, and this document is generated from the code to ensure it is always current.