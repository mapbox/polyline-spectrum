import os, json, subprocess, pytest

libraries = [
        "./mapbox-polyline",
        "./jieter-leaflet-encoded",
        "./joshuaclayton-polylines",
        "./frederickjansen-polyline"
]

fixtures = json.load(open('./fixtures/canon.json')) + json.load(open('./fixtures/google.json'))

def test_encode():
    for library in libraries:
        for fixture in fixtures:
            assert subprocess.check_output([
                    os.path.join(library, "encode"),
                    json.dumps(fixture["input"])]) == fixture["output"], ("encode %s against %s" % (library, fixture["source"]))

def test_decode():
    for library in libraries:
        for fixture in fixtures:
            assert json.loads(subprocess.check_output([
                    os.path.join(library, "decode"),
                    fixture["output"]])) == fixture["input"], ("decode %s against %s" % (library, fixture["source"]))
