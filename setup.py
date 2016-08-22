from setuptools import setup

setup(
    name="learning_journal",
    description="A learning journal site using Pyramid.",
    version=0.1,
    author="Derek Hewitt",
    author_email="derekmhewitt@gmail.com",
    license="MIT",
    py_modules=[""],
    package_dir={"": "src"},
    install_requires=[],
    extras_requires={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
)
