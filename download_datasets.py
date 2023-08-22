import requests
import os
import zipfile


def get_latest_sweden_pbf():
    res = requests.get("https://download.geofabrik.de/europe/sweden-latest.osm.pbf")
    with open("sweden.pbf", "wb") as f:
        f.write(res.content)


def get_trafiklab_gtfs():
    res = requests.get(
        "https://api.resrobot.se/gtfs/sweden.zip?key=a58e6560-4123-4760-a9e0-a350371bad4a",
        headers={"Accept-Encoding": "compress, gzip"},
    )
    with open("sweden.zip", "wb") as f:
        f.write(res.content)
    os.mkdir("gtfs")
    # extract sweden.zip to gtfs folder
    with zipfile.ZipFile("sweden.zip", "r") as zip_ref:
        zip_ref.extractall("gtfs")


# get_latest_sweden_pbf()
# get_trafiklab_gtfs()


def get_mock_data():
    with open("sweden.pbf", "wb") as f:
        f.write("THIS IS MOCKDATA 123123123")


get_mock_data()
