from setuptools import setup
from setuptools import find_packages
import os
import pyrfuniverse

VERSION = pyrfuniverse.__version__
here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="pyrfuniverse",
    version=VERSION,
    description="RFUniverse python interface",
    url="https://github.com/mvig-robotflow/rfuniverse",
    author="Robotflow AI Team",
    author_email="robotflow@sjtu.edu.cn",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    zip_safe=False,
    install_requires=[
        "cloudpickle",
        "grpcio>=1.11.0",
        "numpy>=1.14.1",
        "Pillow>=4.2.1",
        "protobuf==3.19.0",
        "pyyaml>=3.1.0",
        "pybullet",
        "gym==0.21.0",
        # "stable-baselines3"
        "opencv-python"
    ],
    python_requires=">=3.6.1",
)
