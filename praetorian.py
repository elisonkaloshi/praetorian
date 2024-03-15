import re
from flask import Flask, request, abort

app = Flask(__name__)

firewall_rules = {
    'sql_injection': re.compile(r'(union|select|insert|delete|update|drop|alter).*', re.IGNORECASE),
    'xss_attack': re.compile(r'(<script>|<iframe>).*', re.IGNORECASE),
    'path_traversal': re.compile(r'(\.\./|\.\.).*', re.IGNORECASE),
    'command_injection': re.compile(r';|\|\||&&|%0A|%0D|%08|%09', re.IGNORECASE),
    'directory_traversal': re.compile(r'\.\./|\.\\|\.\.\\|\.%2e/|\.%2e\\', re.IGNORECASE),
    'remote_file_inclusion': re.compile(r'(http|https):\/\/|ftp:\/\/', re.IGNORECASE),
    'xxe_injection': re.compile(r'<!ENTITY\s+.+SYSTEM', re.IGNORECASE),
    'csrf_attack': re.compile(r'token=|csrf=|nonce=', re.IGNORECASE)
}

@app.before_request
def praetorian_middleware():
    for attack_type, pattern in firewall_rules.items():
        if pattern.search(request.path) or pattern.search(request.query_string.decode()):
            abort(403, description=f'Request blocked by Praetorian: Detected {attack_type}')

@app.route('/')
def home():
    return 'Welcome!'

if __name__ == '__main__':
    app.run(port=9999)
