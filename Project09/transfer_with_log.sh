#!/bin/bash

# Usage: ./transfer_with_log.sh /path/to/source/ /path/to/destination/

# Prompt user interactively if no arguments provided
if [ -z "$1" ]; then
  read -e -p "Enter source directory (e.g. /Volumes/InternalDrive/Folder): " SRC
else
  SRC="$1"
fi

if [ -z "$2" ]; then
  read -e -p "Enter destination directory (e.g. /Volumes/ExternalDrive/Folder): " DEST
else
  DEST="$2"
fi

# Validate source path
if [ ! -d "$SRC" ]; then
  echo "❌ Source directory does not exist: $SRC"
  exit 1
fi

# Log file with timestamp
LOGFILE=~/Desktop/rsync_transfer_$(date +"%Y-%m-%d_%H-%M-%S").log

echo "Starting transfer from:"
echo "📁 Source:      $SRC"
echo "📂 Destination: $DEST"
echo "📝 Log File:    $LOGFILE"
echo ""

# Time the operation
START=$(date +%s)

# Run rsync with progress and logging
rsync -ah --info=progress2 --log-file="$LOGFILE" "$SRC" "$DEST" && rm -rf "$SRC"


END=$(date +%s)
DURATION=$((END - START))
MIN=$((DURATION / 60))
SEC=$((DURATION % 60))

# macOS notification on completion
osascript -e "display notification \"Transfer complete in ${MIN}m ${SEC}s\" with title \"rsync Transfer\" subtitle \"Finished copying files\""

echo ""
echo "✅ Transfer complete in ${MIN}m ${SEC}s"
echo "📄 Log saved to $LOGFILE"
