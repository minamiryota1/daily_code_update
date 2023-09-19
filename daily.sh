#!/bin/bash

# Check if a directory path is provided as a command-line argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <directory_path>"
  exit 1
fi

# Get the directory path from the command-line argument
target_dir="$1"

# Get the current date in MM-DD format
current_date=$(date +%m-%d)

# Define the directory name based on the current date
dir_name="$current_date"

# Create the main directory with the current date under the specified target directory
mkdir -p "$target_dir/$dir_name"

# Create subdirectories (output, chanchu, and data) under the main directory
mkdir "$target_dir/$dir_name/output"
mkdir "$target_dir/$dir_name/chanchu"
mkdir "$target_dir/$dir_name/data"

# List all directories using one ls -d command
ls -d "$target_dir/$dir_name" "$target_dir/$dir_name"/*
