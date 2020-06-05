![](logo.png)
![](whereami.gif)

# Where Am I?

## Motivation
Communicating your location can be hard, and can only be so accurate. Longitude and latitude can be used to relay ones location to a tee, but remembering exact longtitude and latitude values is hard enough, and to pass them to someone else would prove to be even harder.  
  
The [Open Location Code](https://en.wikipedia.org/wiki/Open_Location_Code) system is a geocode system that can also be used to identify an area *anywhere on earth*. This system provides codes that can narrow a location down to 3.5m by 3.5m distances. However, one pitfall to this system is the hard to remember strings - for example, **849VCWC8+R9**.  
  
*Where Am I* aims to solve this problem by converting the strings into a memorable four-to-five word phrase.

tl;dr - need to relay your location? ~~longitude and latitude~~, ~~Open Location Code~~, Where Am I :heavy_check_mark:

## Installation

### General Setup (1/5)
First, you'll need to setup the main `whereamigeo` Python package first as both the web application and CLI tool depend on it.
1. Create a virtualenv and initialize it; this may vary depending on your operating system. Setup the virtualenv in the root of the project.

       $ virtualenv env && source env/bin/activate

2. Install dependencies for the project.

        $ pip install -r requirements.txt

3. Install the pre-commit hooks. This runs linting before every commit.
        
        $ pre-commit install

3. `cd` into the `whereamigeo` directory.

        $ cd whereamigeo
        
4. Install the package locally.

        $ pip install .


### Web (2/5)
Make sure you've completed the general setup before starting this!

1. `cd` into the `web` directory. This is where the files for the web app live.

        $ cd web

2. Run the app with the following:

        $ export FLASK_APP=main.py && flask run

This should start Flask. You can then view the website at localhost:5000!


### CLI (3/5)
Make sure you've completed the general setup before starting this!
    
1. Run the CLI as a package by using the `-m` flag when executing `python`. You'll first need to `cd` out of the `cli` directory. 

        $ cd ..
        
2. Then, run the CLI package using Python.
    
        $ python -m cli.main <args>

### whereamigeo (4/5)
If you've done the general setup, then this should be setup properly. 

1. Keep in mind, every time you make a change to the files under `whereamigeo/`, you'll need to reinstall the package for the changes to take place.
        
        $ cd whereamigeo
        $ pip install .
        
### Discord bot (5/5)
Not much setup is needed for the Discord functionality to work - as long as you ran the requirements.txt file earlier, you'll have the dependencies needed.

1. On line 27, replace the `INSERT-TOKEN-HERE` with your Discord token. Run the command and it'll start up!

        $ python bot.py

## Contributors
[Kai Chen](https://github.com/kx-chen)  
[Yanlam Ko](https://github.com/YKo20010)  
[Christopher Nguyen](https://github.com/chrisngyn)
