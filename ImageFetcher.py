import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    try:
        #send a GET request to the URL
        response = requests.get(url)

        #check for HTTP errors
        response.raise_for_status()

        #Extract the file name from URL generate one if not available
        parsed_url =urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "image.jpg"

        #create the fetched_images directory if it doesn't exist
        directory = "Fetched_Images"
        os.makedirs(directory, exist_ok = True)

        #save the image to the  fetched_Images directory
        filepath = os.path.join(directory, filename)
        with open(filepath, "wb") as file:
            file.write(response.content)

            print(f"image saved to {filepath}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as connect_err:
        print(f"error connecting to the URL: {connect_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as err:
        print(f"something went wrong: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    url = input("Please Enter the URL of the Image")
    fetch_image(url)

if __name__ == "__main__":
        main()