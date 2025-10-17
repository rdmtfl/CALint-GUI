# CALint-web
A Flask based web interface that provides HTTP endpoints to interact with CALint, a linter designed to validate whether projects follows the clean architecture pattern.

# Installation
### Prequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Make](https://www.gnu.org/software/make/)

# Usage
### Clone this repository
```
$ git clone https://github.com/rdmtfl/CALint-web.git
```
### Navigate to folder
```
$ cd CAlint-web
```
### Build and run the container
```
$ make build_image
$ make run_container
```
### Access the application
Open `http://localhost:5000` in your browser.

# License
This project is licensed under the MIT License.