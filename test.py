import itertools
import json
import os
import subprocess

import pytest

libraries = [
    "./mapbox-polyline",
    "./jieter-leaflet-encoded",
    "./joshuaclayton-polylines",
    "./frederickjansen-polyline"
]

fixtures = json.load(open('./fixtures/canon.json'))

testdata = list(itertools.product(libraries, fixtures))

@pytest.mark.parametrize("library, fixture", testdata)
def test_encode(library, fixture):
    result = subprocess.check_output(
        [os.path.join(library, "encode"), json.dumps(fixture["input"])])

    assert fixture["output"] == result


@pytest.mark.parametrize("library, fixture", testdata)
def test_decode(library, fixture):
    result = subprocess.check_output(
        [os.path.join(library, "decode"), fixture["output"]])

    assert fixture["input"] == json.loads(result)


if __name__ == '__main__':
    pytest.main(['-v', __file__])
