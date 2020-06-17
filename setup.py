# Copyright 2020 The CARSUITE Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import os
import unittest

from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README.mf file
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
  long_description = f.read()

setup(
    name="carsuite",
    version="0.0.1",
    description=
    "The carsuite is a tool for developing and testing driving agents on the CARLA simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oatml/carsuite",
    author="Oxford Applied and Theoretical Machine Learning Group",
    author_email="oatml@googlegroups.com",
    license="Apache-2.0",
    packages=find_packages(),
    install_requires=[
        "absl-py==0.9.0",
        "gym==0.17.1",
        "pygame==1.9.6",
        "matplotlib==3.0.3",
        "seaborn==0.9.1",
        "pandas==0.25.3",
        "scipy==1.4.1",
        "transforms3d==0.3.1",
        "tqdm==4.42.1",
        "wget==3.2",
        "networkx==2.4",
        "imageio==2.8.0",
        "tabulate==0.8.7",
    ],
    tests_require=[
        "pytest",
    ],
    # See carsuite/baselines/README.md for more information.
    extras_require={
        # Additional requirements for TensorFlow baselines.
        "tf": [
            "dm-sonnet==2.0.0",
            "tensorflow==2.2.0",
            "tensorflow_probability==0.9.0",
        ],
        # Additional requirements for PyTorch baselines.
        "torch": [
            "torch==1.5.0",
            "torchvision==0.6.0",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Researchers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache 2.0 License",
        "Programming Language :: Python :: 3.5",
    ],
)
