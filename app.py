from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
        
    # Get query parameters from the request
    slackname = request.args.get('slack_name')
    track_ = request.args.get('track')

    # Get current day of the week
    currentday = datetime.datetime.utcnow().strftime('%A')

    current_utc_time = datetime.datetime.utcnow()

    # Format the current time as a string in the desired format
    current_time = current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Get the GitHub URL of the file being run
    file_url = f'https://github.com/Nalito/hngx-task1/blob/main/app.py'

    # Get the GitHub URL of the full source code
    source_code_url = 'https://github.com/Nalito/hngx-task1'

    # Prepare the response JSON
    response = {
   'slack_name' : slackname,
   'current_day' : currentday,
   'utc_time' : current_time,
   'track' : track_,
   'github_file_url' : file_url,
   'github_repo_url' : source_code_url,
   'status_code' : 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
