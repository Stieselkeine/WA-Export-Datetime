### The Problem
What's App has no way known to me to export media from chat that wasn't previously saved to the gallery with the "creation time" (or the time sent) preserved.
### My (hacky and largely untested) Solution
This script reads the chat protocoll, extracts all lines that contain media, parses the datetime of the message and changes the creation and modification date of the Media-files
### How to use
1. Place the script in the same folder as the extracted chat protocoll and the according media files
2. Run the script with the name of the chat-protocoll as the first argument
