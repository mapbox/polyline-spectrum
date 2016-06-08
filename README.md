# polyline-spectrum

[![CircleCI](https://circleci.com/gh/mapbox/polyline-spectrum/tree/master.svg?style=svg)](https://circleci.com/gh/mapbox/polyline-spectrum/tree/master)

A spectrum test for implementations of the [Google Encoded Polyline](https://developers.google.com/maps/documentation/utilities/polylinealgorithm)
algorithm. This test compares multiple implementations across multiple languages:

* Each implementation has a command-line utility called `encode` that takes a JSON
  string of a coordinate array in `[latitude, longitude]` order and transforms
  it into an encoded polyline, which it prints to stdout without any newlines
  or other information.
* Each implementation has a command-line utility called `decode` that takes an
  encoded polyline string and prints a JSON-encoded coordinate array
  to stdout without any newlines
  or other information.
* `test.py` runs each `encode`, `decode` pair against canonical test cases
  and compares the results.

## Currently-tracked implementations

* **Ruby**
* https://github.com/joshuaclayton/polylines 
* **JavaScript**
* https://github.com/mapbox/polyline
* https://github.com/jieter/Leaflet.encoded
* **Python**
* https://github.com/frederickjansen/polyline

## Contributing a new implementation

1. If the implementation uses a package manager like pip or npm,
   add the dependency to one of the dependency documents, like package.json.
   a. If that introduces a new dependency manager to the mix, add the install
     command to setup.py
2. Create a directory in the format `organization-reponame`. For instance,
   the repository `mapbox/polyline` lives in `mapbox-polyline`.
3. Create `encode` and `decode` CLI commands in that directory. The files
   should be executable (`chmod +x`), and have hashbang lines that find
   the correct interpreter for them to run
4. Add the new implementation to the list of implementations in `test.py`
5. Test the new implementation by running `python test.py`

## Contributing a new test case

1. Confirm that the test case is absolutely true. [The Google polyline utility](https://developers.google.com/maps/documentation/utilities/polylineutility)
   is our authoritative implementation.
2. Add the pair of `input` and `output` to `fixtures/canon.json`
3. Run `python test.py` to confirm behavior

## How do I post an issue?

This is a [pull requests for everything](https://gist.github.com/ryanflorence/8a62abea562ca2896dee) repository:
if you need a new implementation covered, please follow the guide above
to add it. Same if you find a bug, or need an additional test.
