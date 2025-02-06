import sys
import os
import email
import email.policy
import email.utils
import markdown
import yaml
from datetime import datetime

SENDER = "jack+blog@baty.net"
RECIPIENT = "jack@baty.net"
DEFAULT_MAILDIR_PATH = os.path.expanduser("~/Mail/blog")

def markdown_to_maildir(markdown_file, maildir_path=DEFAULT_MAILDIR_PATH):
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract YAML front matter
    if content.startswith('---'):
        parts = content.split('---', 2)
        front_matter = yaml.safe_load(parts[1])
        md_content = parts[2].strip()
    else:
        front_matter = {}
        md_content = content
    
    subject = front_matter.get('title', 'No Subject')
    
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)
    
    # Create email message
    msg = email.message.EmailMessage(policy=email.policy.SMTPUTF8)
    msg['From'] = SENDER
    msg['To'] = RECIPIENT
    msg['Subject'] = subject
    msg['Date'] = email.utils.format_datetime(datetime.now())
    msg.set_content(md_content)  # Plain text version
    msg.add_alternative(html_content, subtype='html')
    
    # Ensure maildir structure exists
    for subfolder in ['cur', 'new', 'tmp']:
        os.makedirs(os.path.join(maildir_path, subfolder), exist_ok=True)
    
    # Save to Maildir
    filename = f'{datetime.now().timestamp()}.{os.getpid()}@localhost'
    filepath = os.path.join(maildir_path, 'new', filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(msg.as_string())
    
    print(f"Message saved to {filepath}")

if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python script.py <markdown_file> [maildir_path]")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    maildir_path = sys.argv[2] if len(sys.argv) == 3 else DEFAULT_MAILDIR_PATH
    markdown_to_maildir(markdown_file, maildir_path)
