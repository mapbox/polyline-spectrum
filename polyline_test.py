import os, json, subprocess

libraries = [
        "./mapbox-polyline",
        "./jieter-leaflet-encoded",
        "./joshuaclayton-polylines",
        "./frederickjansen-polyline"
]

debug = os.environ.get('DEBUG', False)

fixtures = json.load(open('./fixtures/canon.json')) + json.load(open('./fixtures/google.json'))

def roundCoords(coords):
    out = []
    for coord in coords:
        out.append([round(coord[0], 4), round(coord[1], 4)])
    return out

for library in libraries:
    correct = 0
    print "## Library %s\n" % library
    for fixture in fixtures:
        observedOutput = subprocess.check_output([
            os.path.join(library, "encode"),
            json.dumps(fixture["input"])])
        observedInput = roundCoords(json.loads(subprocess.check_output([
            os.path.join(library, "decode"),
            fixture["output"]])))
        if observedOutput != fixture["output"]:
            print "* FAIL ~~encode %s against %s~~" % (library, fixture["source"])
            if debug:
                print "found %s" % observedOutput
                print "wanted %s" % fixture["output"]
        else:
            print "* PASS encode %s against %s" % (library, fixture["source"])
            correct = correct + 1
        if observedInput != fixture["input"]:
            print "* FAIL ~~decode %s against %s~~" % (library, fixture["source"])
            if debug:
                print "found %s" % observedInput
                print "wanted %s" % fixture["input"]
        else:
            print "* PASS decode %s against %s" % (library, fixture["source"])
            correct = correct + 1
    print "\nScore: %s\n\n" % (100.0 * correct / (len(fixtures) * 2.0))
