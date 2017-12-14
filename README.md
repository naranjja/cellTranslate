# excel-translate

### Pre-requisites
- Create a [Google Cloud Platform account](https://console.cloud.google.com/)
- Create a [project](https://console.cloud.google.com/projectcreate) and take note of the project ID
- [Enable the Cloud Translate API](https://console.cloud.google.com/apis/api/translate.googleapis.com/) for the project

### Software requirements
This service depends on:
  - [Python3](https://www.python.org/downloads/)
  - [Google Cloud SDK](https://cloud.google.com/sdk/)
  - [Microsoft Excel](https://products.office.com/en/excel) (or [any other spreadsheet program](https://www.libreoffice.org/discover/calc/))
  - A list of [Python requirements]('./requirements.txt')

You can install all requirements by running [`setup.cmd`](./setup.cmd)

### Usage
Open [`settings.conf`](./settings.conf) and type in:
  - The project ID (e.g. `PROJECT_ID=happy-panda-1234`)
  - The name of the spreadsheet file (e.g. `FILENAME=sample`)
  - The name of the column to translate (e.g. `COLUMN=C`)
  - The [source language](https://cloud.google.com/translate/docs/languages) (e.g. `SOURCE_LANG=es`)
  - The [target language](https://cloud.google.com/translate/docs/languages) (e.g. `TARGET_LANG=en`)

Place the spreadsheet file inside the `input/` folder

Run [`translate.cmd`](./translate.cmd)

Check the `output/` folder for a new spreadsheet with the translated column
