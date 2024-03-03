# open-doener
Open Data Day 2024 Project for mapping and comparing kepab restaurants

## Usage
- Load the python venv
- Install the dependencies with pip
- create a `data.db` file for storage
- run app.py to start the webserver
- launch `http://127.0.0.1:5000` to open the site
- run the `eval.ipynb` notebook to evaluate the data

## Known Issues
- This tool is currently a WIP and *not production ready*.
- Currently, multiple entries with slightly diffent spelling are possible and can interfere with evaluation

## ToDo
- Make Input Site more secure
- Create a function to quantizise multiple entries that are near each other
    - otherwise have a list of known places to select from and a button to request/add a new place to the list
- Besides simple kebap price there are other factors interesting:
    - Different meat and vegetarian options
    - Weight
    - Taste on a 5 star system (or perhaps more defined)
    - Waiting time
- Add multiple language options
- Display the results somewhere publicly