# Copyright (c) 2024 Suvan Banerjee <banerjeesuvan@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

#Imports

import re
import subprocess
import sys

def check_args() -> str:
    '''
    Check if the user has provided a valid argument

    Returns:
    str: The argument provided by the user
    '''
    arg: str = sys.argv[1]
    if arg == 'patch':
        return 'patch'
    elif arg == 'minor':
        return 'minor'
    elif arg == 'major':
        return 'major'
    else:
        print('Invalid argument')
        sys.exit(1)

def get_version() -> str:
    '''
    Get the current version of the package

    Returns:
    str: The current version of the package
    '''
    with open('setup.py', 'r') as f:
        setup: str = f.read()
    version: str = re.search(r"VERSION = '([^']+)'", setup).group(1)
    return version

def increment_version_setup(version: str) -> None:
    '''
    Increment the version in the setup.py file

    Args:
    version (str): The new version
    '''

    with open('setup.py', 'r') as f:
        setup: str = f.read()
    setup = re.sub(r"VERSION = '([^']+)'", f"VERSION = '{version}'", setup)
    with open('setup.py', 'w') as f:
        f.write(setup)

def get_API_key() -> str:
    '''
    Get the API key

    Returns:
    str: The API key
    '''
    with open('API_KEY.env', 'r') as f:
        API_key: str = f.read()
    return API_key

def get_new_version(arg: str) -> str:
    '''
    Get the new version based on the argument provided by the user

    Args:
    arg (str): The argument provided by the user

    Returns:
    str: The new version
    '''
    version: str = get_version()
    if arg == 'patch':
        version = version.split('.')
        version[2] = str(int(version[2]) + 1)
        version = '.'.join(version)
    elif arg == 'minor':
        version = version.split('.')
        version[1] = str(int(version[1]) + 1)
        version[2] = '0'
        version = '.'.join(version)
    elif arg == 'major':
        version = version.split('.')
        version[0] = str(int(version[0]) + 1)
        version[1] = '0'
        version[2] = '0'
        version = '.'.join(version)
    return version

def main() -> None:
    '''
    Main function
    '''
    arg = check_args()
    version: str = get_new_version(arg)
    increment_version_setup(version)
    print(f'Releasing version {version}')
    subprocess.run(['git', 'tag', f'v{version}'])
    subprocess.run(['git', 'push', 'origin', '--tags'])
    subprocess.run(['python', 'setup.py', 'sdist', 'bdist_wheel'])
    print(get_API_key())
    subprocess.run(['twine', 'upload', 'dist/*','-u', '__token__','-p', get_API_key()])
    subprocess.run(['rm', '-rf', 'dist'])
    subprocess.run(['rm', '-rf', 'build'])
    subprocess.run(['rm', '-rf', 'pycryp.egg-info'])

if __name__ == '__main__':
    main()
