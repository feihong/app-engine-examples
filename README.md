# app-engine-examples

A collection of examples for Google App Engine

## Installation

[Download the ZIP file](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python), unzip it to ~/dev/google_appengine, and add that directory to your PATH.

## Running

To run the helloworld app locally:

```
dev_appserver.py helloworld/
```

To run in the cloud:

- Visit [Google Cloud Platform Console](https://console.cloud.google.com) and choose "Create a project..." from the menu.
- Note the project ID of the newly-created project (let's say it's hello-world-1234).
- Run the following command: `appcfg.py -A hello-world-1234 update helloworld/`
- Visit http://hello-world-1234.appspot.com to view your app.
