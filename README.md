# markdown2maildir

Convert folders full of Markdown (.md) files into emails in a target Maildir directory.

ChatGPT wrote most of this, because it would have taken me a week of cursing doing it myself.

There are two scripts here:

`markdown2maildir.py` is a Python scripts that converts a Markdown file to Maildir format.

`markdowndir2emails.sh` is a bash script that loops through a folder and calls `markdown2maildir.py` on each file.

A few things are hard-coded, so be aware of that.


