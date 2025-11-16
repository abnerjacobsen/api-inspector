import requests
import json
import sys

def send_multipart_request(filepath):
    """
    Reads a sample multipart request from a JSON file and sends it to the API inspector.
    """
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        body = data.get('body')
        headers = data.get('headers', {})

        # Prepare the request headers from the JSON file
        # The requests library expects a dict of strings, but the JSON has lists of strings.
        # We'll take the first item from each list.
        request_headers = {key: value[0] for key, value in headers.items()}

        # Ensure the Content-Length is not set by requests automatically, as it's in the original headers
        # However, requests will calculate it based on the body, so we can remove it to avoid conflicts.
        request_headers.pop('Content-Length', None)
        
        url = "http://localhost:8000/capture/test-multipart"

        print(f"Sending POST request to {url}...")
        print("Headers being sent:")
        for key, value in request_headers.items():
            print(f"  {key}: {value}")
        
        response = requests.post(url, data=body.encode('utf-8'), headers=request_headers)

        print(f"Status Code: {response.status_code}")
        print("Response JSON:")
        print(response.json())

    except FileNotFoundError:
        print(f"Error: {filepath} not found. Make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test-multipart.py <path_to_json_file>")
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    send_multipart_request(json_file_path)
