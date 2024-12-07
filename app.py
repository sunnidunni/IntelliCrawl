from flask import Flask, request, render_template, jsonify, send_from_directory
import json
import os
from crawler.client import CrawlerClient

app = Flask(__name__)

# Replace with your actual API key
API_KEY = "123456"

# Initialize the crawler client
client = CrawlerClient(apikey=API_KEY, use_dynamic=False)

# Create a directory for saving the JSON files
UPLOAD_FOLDER = 'downloads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def home():
    """Render the HTML form"""
    return render_template("form.html")

@app.route("/crawl", methods=["POST"])
def crawl():
    """Handle the form submission and perform the web crawl"""
    url = request.form.get("url")
    prompt = request.form.get("prompt")
    max_depth = request.form.get("max_depth", 0)

    if not url or not prompt:
        return "Missing URL or Prompt", 400

    try:
        # Use the crawler client to get information
        results = client.get_info(url, prompt, max_depth=int(max_depth))

        # Save results to a JSON file
        json_filename = f"{url.split('//')[1].split('/')[0]}_results.json"
        json_filepath = os.path.join(UPLOAD_FOLDER, json_filename)
        
        # Write results to the JSON file
        with open(json_filepath, 'w') as json_file:
            json.dump(results, json_file, indent=4)
            json_file.write('\n')

        # Return the results back to the form page
        return render_template("form.html", results=results, json_filename=json_filename)
    
    except Exception as e:
        return str(e), 500

@app.route("/download/<filename>")
def download(filename):
    """Route to download the generated JSON file"""
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
