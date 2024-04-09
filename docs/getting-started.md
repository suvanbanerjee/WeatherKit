
## Getting Started

The easy way to get WeatherKit is from pip:

```bash
pip install weatherkit
```

## Dependencies
[geopy](https://pypi.org/project/geopy/) - For getting latitude and longitude of the location if the location is given in address or city format.

## Installing from source
Download the source code by cloning the repository or by clicking [here](https://github.com/suvanbanerjee/weatherkit/archive/refs/heads/main.zip)

```
git clone https://github.com/suvanbanerjee/weatherkit.git
cd weatherkit
```
Build the package using the following command:
```
python setup.py sdist bdist_wheel
```
Install the package using the following command:
```
pip install dist/*.whl
```
