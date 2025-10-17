# build docker file - build frontend
build_image:
	@echo "Building Docker image ..."
	docker build -t calint-web .

# run docker container
run_container:
	@echo "Running Docker container ..."
	docker run -d -p 5000:5000 --name calint-web-container calint-web

# stop and remove docker container
stop_container:
	@echo "Stopping and removing Docker container ..."
	docker stop calint-web-container
	docker rm calint-web-container