from pathlib import Path

from setuptools import setup

from vecked import get_version

version = get_version()

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.11",
    "Typing :: Typed",
]

if "a" in version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="Vector calculations",
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="vecked",
    packages=[
        "vecked",
        "vecked.region2",
        "vecked.vector2",
    ],
    package_data={
        "vecked": ["py.typed"],
        "vecked.region2": ["py.typed"],
        "vecked.vector2": ["py.typed"],
    },
    python_requires=">=3.11",
    url="https://github.com/cariad/vecked",
    version=version,
)
