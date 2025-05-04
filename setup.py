from setuptools import setup, find_packages

def load_requirements(filename="requirements.txt"):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="platform-python-base",
    version="0.1.0",
    description="Base Python framework for scalable microservices",
    author="Subrahmanya Hegde",
    author_email="subbu.v.h.234@gmail.com",
    packages=find_packages(exclude=("tests", "logs")),
    install_requires=load_requirements(),
    python_requires=">=3.8",
)
