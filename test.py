import os, json, unittest, subprocess

libraries = [
        "./mapbox-polyline",
        "./jieter-leaflet-encoded",
        "./joshuaclayton-polylines"
]

class TestPolylineMethods(unittest.TestCase):

    def test_encode(self):
        for library in libraries:
            self.assertEqual(
                subprocess.check_output([
                    os.path.join(library, "encode"),
                "[[1,2],[3,4]]"]), "_ibE_seK_seK_seK")

    def test_decode(self):
        for library in libraries:
            self.assertEqual(
                json.loads(subprocess.check_output([
                    os.path.join(library, "decode"),
                "_ibE_seK_seK_seK"])), [[1,2],[3,4]])

if __name__ == '__main__':
    unittest.main()
