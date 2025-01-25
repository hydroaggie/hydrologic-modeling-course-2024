# Instructions for setting up and running Docker

## Prerequisites
- GitHub account. Sign up [here](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).
- Windows/Mac with git installed. See [Instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on how to install Git.

## Instructions

1. Download and install Docker Desktop. Go to [Docker](https://www.docker.com/products/docker-desktop/) and download Docker Desktop. Make sure you download the correct version based on your computer’s operating system and architecture. Follow the instructions to install Docker Desktop.
2. Launch Docker Desktop. The application should be running while you do the next steps. (You might need to create a Docker account and sign in if you don’t already have one.)
3. Download Docker image. Start a new terminal session (outside Docker). For example, open the Powershell on Windows or the Terminal on Mac. Copy and paste the following command into the terminal:

```bash
docker pull pshuai/jupyter-pflotran-multiplatform:latest
```

This will start downloading the docker image (~2G).

4. Download course repository. In the terminal/powershell, run the following command

```bash
git clone https://github.com/hydroaggie/hydrologic-modeling-course-2024.git 
```

5. Launch Docker. Run the following command in your terminal:
- On Mac. Use `$(pwd)` as your current working directory.

```bash
# navigate into the downloaded course folder
cd hydrologic-modeling-course-2024

# launch docker
docker run -it --rm -p 8888:8888  -v $(pwd):/home/aggie/work pshuai/jupyter-pflotran-multiplatform:latest jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.token=''
```
- On Windows, replace `$(pwd)` with the actual path to the course material folder, e.g., `C:\Users\USERNAME\hydrologic-modeling-course-2024` (where `USERNAME` is your Windows username).

```bash
# Navigate into the downloaded course folder
cd hydrologic-modeling-course-2024

# launch docker
docker run -it --rm -p 8888:8888  -v C:\Users\USERNAME\hydrologic-modeling-course-2024:/home/aggie/work pshuai/jupyter-pflotran-multiplatform:latest jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.token=''
```

6. Connect to the JupyterLab. If the above command is successful, you will see output like the following at the bottom of the screen.

```bash
[I 2025-01-22 05:49:28.562 ServerApp] Jupyter Server 2.15.0 is running at:
[I 2025-01-22 05:49:28.562 ServerApp] http://2f1be613bce1:8888/lab
[I 2025-01-22 05:49:28.562 ServerApp]     http://127.0.0.1:8888/lab
[I 2025-01-22 05:49:28.562 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

Copy and paste the URL: http://127.0.0.1:8888/lab into your browser and you should see the JupyterLab interface like below.

<img width="1608" alt="image" src="https://github.com/user-attachments/assets/2f7ab2a1-6e7b-4997-926e-5bbc8f327f48" />


7. Congratulations! You are all set!

## Troubleshoot

- If your Docker is running out of space, you might need to use [docker system prune](https://docs.docker.com/reference/cli/docker/system/prune/) with the appropriate options to clear out old containers and make space for the new one.

```bash
$ docker system prune
```

