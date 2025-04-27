from setuptools import setup, find_packages

setup(
    name="platform-python-base",
    version="0.1.0",
    description="Base Python framework for scalable microservices",
    author="Subrahmanya Hegde",
    author_email="subbu.v.h.234@gmail.com",
    packages=find_packages(exclude=("tests", "logs")),
    install_requires=[
        "fastapi>=0.100.0",
        "pydantic>=1.10.0",
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0",
        "aiobreaker>=0.4.0"
    ],
    python_requires=">=3.8",
)
