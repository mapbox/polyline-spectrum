import os
import unittest
import subprocess

libraries = [
        "./mapbox-polyline",
        "./jieter-leaflet-encoded"
]

class TestPolylineMethods(unittest.TestCase):

    def test_forward(self):
        for library in libraries:
            self.assertEqual(
                subprocess.check_output([
                    os.path.join(library, "forward"),
                "[[1,2],[3,4]]"]), "_ibE_seK_seK_seK")

    def test_reverse(self):
        for library in libraries:
            self.assertEqual(
                subprocess.check_output([
                    os.path.join(library, "reverse"),
                "_ibE_seK_seK_seK"]), "[[1,2],[3,4]]")

if __name__ == '__main__':
    unittest.main()
