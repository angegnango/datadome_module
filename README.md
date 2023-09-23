## DATADOME MODULE

Datadome module to intercept incomming http traffic

### DEPENDENCIES
  
  - [Python](https://www.python.org/downloads/) 
  - [Poetry](https://python-poetry.org/) 

### GETTINGS STARTED

  1 - Clone the repository
  ` git clone `

  2 - Install dependencies using Poetry
  ` poetry install `

  3 - Launch tests
  `  make test `

  4 - Buid your packahe and publlish to pypiserver

  Before build your python package, some configuration are required

  - Configure poetry using your pypi server token
  `  poetry config <your-pypi-token-here> `
  

  - Build your package
  `  poetry build `

  - Publish it
  `  poetry publish `


---
> POSSIBILITY TO USE THIS PACKAGE

- use it in your local environnment by adding as local dependencies
- use it as remote dependencies from github
- use as a third party library from pypi

In our case we will use it as local dependencies in our cart_api webservice