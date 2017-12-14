@echo off

echo Clearing previous configuration...
REG delete HKCU\Environment /F /V GOOGLE_APPLICATION_CREDENTIALS

echo Logging in to the Google Cloud SDK...
call gcloud auth application-default login

echo Reading the settings file...
for /f "delims== tokens=1,2" %%G in (settings.conf) do set %%G=%%H

echo Setting working project...
call gcloud config set project %PROJECT_ID%

echo Creating the service account...
call gcloud iam service-accounts create %SERVICE_ACCOUNT_NAME%

echo Binding the service account to the project...
call gcloud projects add-iam-policy-binding %PROJECT_ID% ^
  --member "serviceAccount:%SERVICE_ACCOUNT_NAME%@%PROJECT_ID%.iam.gserviceaccount.com" ^
  --role "roles/owner"

echo Creating a service account JSON file to be used by the client libraries...
call gcloud iam service-accounts keys create service-account.json ^
  --iam-account %SERVICE_ACCOUNT_NAME%@%PROJECT_ID%.iam.gserviceaccount.com

echo Setting the location of the service account to an environment variable...
setx GOOGLE_APPLICATION_CREDENTIALS "%cd%\service-account.json"
