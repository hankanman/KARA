#!/bin/bash

# Export environment variables
export API_KEY="your_api_key"
export PATH_TO_DIR="/path/to/your/directory"

# Run the assistant
python3 /path/to/your/assistant.py

# Check if the assistant ran successfully
if [ $? -eq 0 ]
then
  echo "Assistant ran successfully."
else
  echo "Assistant encountered an error." >&2
fi