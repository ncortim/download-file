import os
import requests
from datetime import datetime
from dotenv import load_dotenv


def main():
    # load env vars
    load_dotenv()
    BASE_FILENAME = os.getenv("BASE_FILENAME")
    BASE_URL = os.getenv("BASE_URL")
    PATHNAME = os.getenv("PATHNAME")

    # Get today's date in YYYYMMDD format
    today = datetime.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    # Get time in HHMMSS format
    time = today.strftime("%H%M%S")

    target_filename = f"{BASE_FILENAME}_{year}{month}{day}.png"
    print(f"Target filename: {target_filename}")

    path = f"{PATHNAME}/{year}/{month}/{day}/"
    # Safely join URL paths
    # url = os.path.join(BASE_URL, path, target_filename)
    # This will join properly even if slashes exist
    url = f"{BASE_URL}/{path}/{target_filename}"
    # url = urljoin(BASE_URL, path + target_filename)
    print(f"Constructed URL: {url}")

    try:
        response = requests.get(url, stream=True)
        # Raise an error if the request was unsuccessful
        response.raise_for_status()

        new_filename = f"{target_filename.split('.')[0]}_{time}.png"

        with open(new_filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Download complete: {target_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e}")


if __name__ == "__main__":
    main()
