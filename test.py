import os, json, unittest, subprocess

libraries = [
        "./mapbox-polyline",
        "./jieter-leaflet-encoded",
        "./joshuaclayton-polylines",
        "./frederickjansen-polyline"
]

fixtures = json.load(open('./fixtures/canon.json'))

class TestPolylineMethods(unittest.TestCase):

    def test_encode(self):
        for library in libraries:
            for fixture in fixtures:
                self.assertEqual(
                    subprocess.check_output([
                        os.path.join(library, "encode"),
                        json.dumps(fixture["input"])]),
                    fixture["output"],
                    "encode %s against %s" % (library, fixture["source"]))

    def test_decode(self):
        for library in libraries:
            for fixture in fixtures:
                self.assertEqual(
                    json.loads(subprocess.check_output([
                        os.path.join(library, "decode"),
                        fixture["output"]])),
                    fixture["input"],
                    "decode %s against %s" % (library, fixture["source"]))

if __name__ == '__main__':
    unittest.main()
