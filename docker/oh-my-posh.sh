#!/bin/bash

# Add local installations
mkdir -p ~/.local/bin
mkdir -p ~/.local/lib

# Add terminal config
curl -s https://ohmyposh.dev/install.sh | bash -s -- -d ~/.local/bin
# Config Oh-my-posh
oh-my-posh font install FiraCode
echo 'eval "$(oh-my-posh init bash --config ~/themes/clean-detailed.omp.json)"' >> ~/.bashrc
