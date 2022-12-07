# tools-page-clicks-view

A small script that reads the data exported as CSV and generates a preview of the webpage with an overlay of user clicks.

This script assumes that the Freenalytics application is using the [Official Web Template](https://freenalytics.github.io/official-templates/web-template/).

**This isn't a generic solution that you can plug and play directly to your application, it is merely a proof of concept
of what can be done with the data generated and uploaded to Freenalytics. You may use this as some sort of inspiration
for your own data treatment.**

## Installation

Clone this repository:

```text
git clone https://github.com/freenalytics/tools-page-clicks-view
```

You may create a virtual environment to run this script:

```text
python3 -m venv ./venv
```

And then activate it, (on `unix`):

```text
source ./venv/bin/activate
```

Install the dependencies (with or without virtual environment, up to you):

```text
pip install -r requirements.txt
```

## Usage

As mentioned before, this isn't a generic solution. If you with to try this yourself you should:

1. Export your own CSV from your application page on Freenalytics (under the **Data Entries** page).
2. Add the CSV into the folder where your script is located.
3. Update the `URL`, `DATA_AS_CSV` and the `pages` array inside the `main.py` file to fit your needs.
4. Run the script with `python main.py`.

> You may need to install Google Chrome. Check out the [Install Drivers](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) page
> on the Selenium website.
