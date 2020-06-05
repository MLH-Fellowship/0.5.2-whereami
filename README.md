![](logo.png)
![](whereami.gif)

# Where Am I?

## Installation

### General Setup (1/4)
You'll need to setup the main `whereamigeo` python package first. Both the web and cli depend on it.
1. Create a virtualenv and initialize it. This may vary depending on your operating system. Setup this virtualenv in the root of the project.

       $ virtualenv env && source env/bin/activate

2. Install dependencies for the entire project.

        $ pip install -r requirements.txt

3. Install the pre-commit hooks. This runs linting before every commit.
        
        $ pre-commit install

3. `cd` into the `whereamigeo` directory.

        $ cd whereamigeo
        
4. Install the package locally.

        $ pip install .


### Web (2/4)
Make sure you've completed the general setup before starting this.

1. `cd` into the `web` directory. This is where the files for the web app live.

        $ cd web

2. Run the app with the following:

        $ export FLASK_APP=main.py && flask run

This should start Flask. You can then view the website at localhost:5000.


### CLI (3/4)
Make sure you've completed the general setup before starting this.

1. `cd` into the `cli` directory. This is where the files for the CLI live.

        $ cd cli
    
    
2. For development, run the CLI as a package by using the `-m` flag when executing `python`. You'll first need to `cd` out of the `cli` directory. 

        $ cd ..
        
    Then, run the CLI package using Python.
    
        $ python -m cli.main <args>

### whereamigeo (4/4)
If you've done the general setup, then this should be setup properly. 

Keep in mind, every time you make a change to the files under `whereamigeo/`, you'll need to reinstall the package for the changes to take place.
        
    $ cd whereamigeo
    $ pip install .
        
