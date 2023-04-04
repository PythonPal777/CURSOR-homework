from datetime import datetime, timezone, timedelta
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/datetime')
def datetime_default():
    """Returns current date and time with server's timezone."""
    server_time = datetime.now(timezone.utc)
    return f"Server time: {server_time.strftime('%Y-%m-%d %H:%M:%S %Z')}"

@app.route('/datetime/')
def datetime_with_timezone():
    """Returns current date and time with the specified timezone."""
    timezone_arg = request.args.get('tz', '0')
    try:
        timezone_hours = int(timezone_arg)
        timezone_offset = timedelta(hours=timezone_hours)
        requested_time = datetime.now(timezone.utc) + timezone_offset
        return f"Requested time: {requested_time.strftime('%Y-%m-%d %H:%M:%S %Z')}"
    except ValueError:
        abort(406, description="Timezone not found")

@app.route('/datetime/<int:timezone_hours>')
def datetime_with_specific_timezone(timezone_hours):
    """Returns current date and time with the specified timezone."""
    timezone_offset = timedelta(hours=timezone_hours)
    requested_time = datetime.now(timezone.utc) + timezone_offset
    return f"Requested time: {requested_time.strftime('%Y-%m-%d %H:%M:%S %Z')}"

@app.route('/')
def index():
    """Returns short documentation with usage examples."""
    return """
    <h1>Usage examples:</h1>
    <ul>
        <li><a href="/datetime">/datetime</a> - returns current date and time with server's timezone</li>
        <li><a href="/datetime/?tz=0">/datetime/?tz=0</a> - returns current date and time with timezone at UTC+0</li>
        <li><a href="/datetime/+2">/datetime/+2</a> - returns current date and time with timezone at UTC+2</li>
        <li><a href="/datetime/-5">/datetime/-5</a> - returns current date and time with timezone at UTC-5</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)