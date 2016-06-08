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
                    json.dumps(fixture["input"])]), fixture["output"])

    def test_decode(self):
        for library in libraries:
            for fixture in fixtures:
                self.assertEqual(
                    json.loads(subprocess.check_output([
                        os.path.join(library, "decode"),
                    fixture["output"]])), fixture["input"])

if __name__ == '__main__':
    unittest.main()
