# Leonardo.ai Automation Bot

An automation script for Leonardo.ai that can create accounts and scrape generated pictures, ideal for bulk creation.

## Instructions

1. **Download Files:**
   - Access the files in the [Releases](https://github.com/nxbvu/Leonardo.ai-Bot/releases) section.

2. **Download ChromeDriver:**
   - Obtain the ChromeDriver corresponding to your Chrome version [here](https://googlechromelabs.github.io/chrome-for-testing/#stable).

3. **Organize Files:**
   - Place all files, including the ChromeDriver, into a single folder.

4. **Set Download Path:**
   - Open `pictures.py` and set your desired download path in the variable `download_path`.

5. **Install Dependencies:**
   - Create and activate a virtual environment (optional but recommended):
     ```
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```
   - Install the required Python packages using `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```

6. **Create Accounts:**
   - Run `main.py` to start account creation.
   - Adjust values like `quit` and `thread_count` to suit your preferences.

7. **Generate and Download Pictures:**
   - Run `pictures.py`, input your prompt, and the script will log in, generate pictures, and download them to your specified path.

8. **Access Used Accounts:**
   - Run `take.py` to retrieve a used account.

## File Descriptions

- **main.py**: This script is responsible for creating new accounts on Leonardo.ai. It uses a temporary email service to receive confirmation codes and complete the registration process.

- **pictures.py**: This script logs into Leonardo.ai using the credentials from `login.txt`, generates pictures based on a given prompt, and downloads the images to the specified download path.

- **take.py**: This script retrieves the last used account from `tr.txt` and prints the account details.

- **tipp.py**: A utility script that sets up a WebDriver for a typing test website, replacing characters on the screen with 'w'. This script is not directly related to Leonardo.ai but is included for additional functionality.

## Notes

- **Errors**: You may encounter errors if Leonardo.ai changes class names or other elements on their site.
- **Disclaimer**: I have a guilty conscience and do not use this script. It's better to purchase the premium service for unlimited use.

## Dependencies

Ensure you have the following dependencies installed:

- Selenium

These dependencies are listed in the `requirements.txt` file. You can install them using:

```
pip install -r requirements.txt
```

# Running the Scripts

## Set up your environment:

Make sure all necessary files and the ChromeDriver are in the same folder.
Update the download_path in `pictures.py`.

## Create accounts:

Run `main.py` to start creating accounts. Adjust the quit and thread_count values as needed.

## Generate and download pictures:

Run `pictures.py`, input your prompt, and the script will log in, generate pictures, and download them to your specified path.

## Retrieve used accounts:

Run `take.py` to get details of the last used account.

# How to run
- open `cmd.exe` non admin mode. `cd` file location. click enter then type below:

```
python main.py
python pictures.py
python take.py
```
