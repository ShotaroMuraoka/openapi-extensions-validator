from setuptools import setup, find_packages

with open("requirements.txt") as requirements_file:
    install_requirements = requirements_file.read().splitlines()
setup(
    name="apigw-openapi-yaml-validator",
    version="0.0.1",
    description="Amazon API Gateway extensions to OpenAPI validator.",
    author="ShotaroMuraoka",
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "apigw-openapi-yaml-validator=apigw_openapi_yaml_validator.core:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
    ],
)
