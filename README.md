# excel-translate
A simple service to translate an entire column from a spreadsheet.

---

### Pre-requisites
- Create a [Google Cloud Platform account](https://console.cloud.google.com/)
- Create a [project](https://console.cloud.google.com/projectcreate) and take note of the project ID
- [Enable the Cloud Translate API](https://console.developers.google.com/apis/library/translate.googleapis.com/) for the project
- Run [`auth.cmd`](./auth.cmd) to authorize this service to use the APIs
  - This will open a browser window for you to login to your Google Cloud Platform account
  - When finished, check if a file called `service-account.json` was created

Additionally, this service depends on:
  - [Python3](https://www.python.org/downloads/)
  - [Google Cloud SDK](https://cloud.google.com/sdk/)
  - [Microsoft Excel](https://products.office.com/en/excel) (or [any other spreadsheet program](https://www.libreoffice.org/discover/calc/))
  - A list of [Python requirements](./requirements.txt)

You can install these by running [`setup.cmd`](./setup.cmd) and following the instructions.

---

### Usage
- Place the spreadsheet file inside the `input` folder
- Open [`settings.conf`](./settings.conf) and type in:
  - The project ID (e.g. `PROJECT_ID=happy-panda-1234`)
  - The name of the spreadsheet file (e.g. `FILENAME=sample`)
  - The name of the column to translate (e.g. `COLUMN=title`)
  - The [source language](https://cloud.google.com/translate/docs/languages) (e.g. `SOURCE_LANG=en`)
  - The [target language](https://cloud.google.com/translate/docs/languages) (e.g. `TARGET_LANG=es`)
- Run `python `[`translate.py`](./translate.py) to perform translation
- Check the `output` folder for a new spreadsheet with the translated column
