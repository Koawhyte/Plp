import requests
import os 
from urllib.parse import urlparse

def main():
    print("Welcome to Ubuntu Image Fetcher")
    print("A tool for collecting images from the web")

    #Get URLs from user
    urls = input("Please enter the image URLs(seperated by commas):")
    urls = [url.strip() for url in urls.split(',')]

    #create directory if it does not exist
    os.makedirs("Fetched_Images, exist_ok=True")

    for url in urls:
        try:
            #Fetch the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            #Extract filename from url or generate one
            parsed_url =urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
               filename = "downloaded_image.jpg"

            #check for duplicates
            filepath = os.path.join("Fetched_Images", filename)
            if os.path.exists(filepath):
                print(f"Duplicate image: {filename}")
                continue
       
             #save the image 
        
            with open(filepath, "wb") as f:
               f.write(response.content)
               print(f" Successfully fetched: {filename}")
               print(f"image saved to {filepath}")

        except requests.exceptions.RequestException as err:
               print(f"connection error: {err}")
        except Exception as e:
               print(f"An error occurred: {e}")
    print("\nConnection Strenthened. Community enriched. ")


if __name__ == "__main__":
        main()