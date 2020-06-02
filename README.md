# Hackathon Geography

## Initial Dev Environment Setup

### Web
1. `cd` into the `web` directory. This is where the files for the web app live.

    `$ cd web`

2. Create a virtualenv and initialize it. This may vary depending on your operating system.

    `$ virtualenv env && source env/bin/activate`

3. Install dependencies using `pip`.

    `$ pip install -r requirements.txt`

4. Run the app with the following:

    `$ export FLASK_APP=main.py && flask run`

This should start Flask. You can then view the website at localhost:5000.
