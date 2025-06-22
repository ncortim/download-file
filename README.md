# File Download Script

This is a small Python script that downloads a file from a specified URL. The URL needs to be specified in advance in a `.env` file. **No web scraping** is involved.

## Requirements

* Python 3.14
* [UV Python](https://docs.astral.sh/uv/) (used for virtual environment management)

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/ncortim/download-file.git
   cd download-file
   ```

2. Create and activate a virtual environment:

   ```bash
   uv venv --python 3.14  # Create a new virtual environment
   source .venv/bin/activate  # Activate the virtual environment
   ```

3. Install the dependencies:

   ```bash
   uv pip install -r requirements.txt
   ```

4. Create a `.env` file in the root of the project and add the following variables (see .env-template file:

   ```bash
   BASE_FILENAME=my-file
   BASE_URL=https://...
   PATHNAME=my/path/name
   ```


## How to Use

Once the environment is set up and the `.env` file is configured, simply run the script:

```bash
python main.py
```

The script will download the file from the specified URL and save it with the provided filename.

## Note

* No web scraping is involved in this script. The URL is directly specified in the `.env` file.
