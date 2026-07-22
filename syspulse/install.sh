#!/usr/bin/env bash

set -e

REPO_URL="https://github.com/YOUR_GITHUB_USERNAME/syspulse.git"
INSTALL_DIR="$HOME/.syspulse"
VENV_DIR="$HOME/.syspulse_env"
BIN_LINK="/usr/local/bin/syspulse"

echo -e "\e[34m[+] Installing SysPulse...\e[0m"

# 1. Clone or update repository
if [ -d "$INSTALL_DIR" ]; then
    echo -e "\e[33m[*] Updating existing SysPulse installation...\e[0m"
    git -C "$INSTALL_DIR" pull
else
    echo -e "\e[32m[+] Cloning repository...\e[0m"
    git clone "$REPO_URL" "$INSTALL_DIR"
fi

# 2. Set up virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo -e "\e[32m[+] Creating virtual environment...\e[0m"
    python3 -m venv "$VENV_DIR"
fi

# 3. Install dependencies and SysPulse package
echo -e "\e[32m[+] Installing package dependencies...\e[0m"
"$VENV_DIR/bin/pip" install --upgrade pip > /dev/null
"$VENV_DIR/bin/pip" install "$INSTALL_DIR" > /dev/null

# 4. Create symlink in /usr/local/bin for global access
echo -e "\e[32m[+] Linking binary globally to $BIN_LINK...\e[0m"
if [ -w "/usr/local/bin" ]; then
    ln -sf "$VENV_DIR/bin/syspulse" "$BIN_LINK"
else
    sudo ln -sf "$VENV_DIR/bin/syspulse" "$BIN_LINK"
fi

echo -e "\n\e[32m[✔] SysPulse successfully installed! Run 'syspulse' in your terminal.\e[0m\n"
