import random
from colorama import Fore, Style

TIPS = [
    "💻 Run sqlmap while you are waiting.",
    "📂 Look for simple files that may seem obvious.",
    "🔑 Have you tried admin:admin yet?",
    "🕵️‍♂️ Check for hidden directories using DirBuster.",
    "🤖 Always review robots.txt for hidden paths.",
    "✨ Sometimes the easiest solutions are the best.",
    "🔐 Test default credentials; they might surprise you.",
    "📥 Check the server response headers for hints.",
    "📜 Try fuzzing parameter values for unexpected results.",
    "💬 Look for comments in the page source; they may reveal hints.",
    "📂 Check if the site is vulnerable to directory traversal.",
    "🔍 Have you enumerated all open ports yet?",
    "🔑 Try brute-forcing login pages with common credentials.",
    "🛠️ Use Burp Suite's intruder to test inputs.",
    "🌐 Don't forget to check for subdomains.",
    "🔒 Scan for SSL/TLS vulnerabilities using sslscan.",
    "🌐 Always test HTTP and HTTPS separately.",
    "🔎 Review the page source for hidden or disabled form fields.",
    "🗂️ Use gobuster or dirbuster for brute-forcing paths.",
    "📂 Check for backup files like .bak or .old.",
    "🔍 Enumerate hidden parameters with tools like Arjun.",
    "📦 Scan for default CMS installations like WordPress or Joomla.",
    "🛠️ Review JavaScript files for exposed API keys.",
    "🍪 Test for weak session cookies with predictable values.",
    "🌐 Try manipulating URL parameters to bypass restrictions.",
    "🖥️ Use Nmap scripts to scan for vulnerabilities.",
    "📡 Search for exploits based on software versions.",
    "💾 Check for database dumps left exposed on the server.",
    "📝 Look for writable directories to upload payloads.",
    "📤 Test file uploads for bypassing extensions or MIME types.",
    "🛡️ Check for weak or missing Content Security Policies.",
    "⏳ Try timing attacks to uncover blind SQLi vulnerabilities.",
]

COLORS = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.YELLOW, Fore.WHITE]

def get_random_tip_with_color():
    tip = random.choice(TIPS)
    color = random.choice(COLORS)
    return f"{color}{tip}{Style.RESET_ALL}"