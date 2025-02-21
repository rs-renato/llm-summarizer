# 🗂️ Content
- [🚀 Leveraging LLM to summarize video content](#-leveraging-llm-to-summarize-video-content)
- [❗️Why This Matters](#️why-this-matters)
- [💻 How to run it in your own host (recommended)](#-how-to-run-it-in-your-own-host-recommended)
  - [⚡️ Ollama installation](#️-ollama-installation)
  - [⚡️ Conda installation](#️-conda-installation)
  - [⚡️ Install the application dependencies](#️-install-the-application-dependencies)
- [🧑🏻‍💻 Run CLI Mode](#-run-cli-mode)
- [🤩 Run UI Chat Mode](#-run-ui-chat-mode)
- [📦 How to run it in a Docker container](#-how-to-run-it-in-a-docker-container)
  - [🤩 UI Chat Mode in Docker](#-ui-chat-mode-in-docker)
- [🗑️ Uninstalling](#️-uninstalling)
  - [⚡️ Conda](#️-conda)
  - [⚡️ Application](#️-application)
  - [⚡️ Ollama](#️-ollama)
  - [⚡️ Docker](#️-docker)
- [🌍 Let's Connect & Collaborate!](#-lets-connect--collaborate)

==🎯 **TLDR;**==
This project helps you summarize video content using LLMs to save time on long recordings like KT sessions, meetings, and lectures.

✅ Video Source → Extracts audio → Transcribes → Generates summaries
✅ Transcription Source → Generates summaries
✅ CLI & UI modes available
✅ Runs on your host (recommended) or in Docker
✅ Supports multiple LLM models with Ollama

👉 Jump to the [installation steps](#-how-to-run-it-in-your-own-host-recommended) to get started!
👉 Connect with me on [LinkedIn](https://www.linkedin.com/in/renatorodriguesrs/)!

# 🚀 Leveraging LLM to summarize video content

Over the past few weeks, I faced a challenge that many of us can relate to: how to efficiently consume hours of Knowledge Transfer (KT) videos without spending days watching them. With about 20 hours of KT videos to review, I knew there had to be a better way than sitting through every minute of footage. That’s when I decided to leverage the power of Large Language Models (LLMs) to create a solution.

I built a PoC python-based application that automatically extracts audio from videos, transcribes the content, and generates detailed summaries using an LLM. The result? Instead of spending 20 hours watching videos, I was able to read the summaries in just 40 minutes. That’s a 97% reduction in time spent! Now, my team can quickly grasp the main topics from the summaries and only dive into the original video when more details are needed.

# ❗️Why This Matters

In today’s fast-paced work environment, time is one of our most valuable resources. This tool not only saves time but also ensures that key insights are captured in a structured, easy-to-read format. It’s perfect for anyone dealing with long videos, whether it’s KT sessions, meeting recordings, or lectures.

**Check the full article on Linkedin:** [Leveraging LLM to summarize video content](https://www.linkedin.com/pulse/leveraging-llm-summarize-video-content-renato-rodrigues-q5mpf/)

# 💻 How to run it in your own host (recommended)
First, let's install the dependencies for this project

## ⚡️ Ollama installation
Download and install [ollama](https://github.com/ollama/ollama) to integrate locally with the LLM tool. You can use the LLM as you want, however, it's nice to start with a lighther model such as  
`llama3.2:1b, qwen:1.8b, deepseek-r1:1.5b` or other that you want. If you have a big machine, go ahead and work with larger models. Be free to use Ollama in a docker container. If so, use the flag `-a http://custom-api-url` in the cli command.

```shell
$ ollama pull deepseek-r1:1.5b
pulling manifest 
pulling aabd4debf0c8... 100% ▕████████████████████████████████▏ 1.1 GB                         
pulling 369ca498f347... 100% ▕████████████████████████████████▏  387 B                         
pulling 6e4c38e1172f... 100% ▕████████████████████████████████▏ 1.1 KB                         
pulling f4d24e9138dd... 100% ▕████████████████████████████████▏  148 B                         
pulling a85fe2a2e58e... 100% ▕████████████████████████████████▏  487 B                         
verifying sha256 digest 
writing manifest 
success 
```

## ⚡️ Conda installation
Download and install [conda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) to isolate your host environment from what's being installated as dependencies, then run the commands bellow to create an environment. If you preffer, you can work with `Miniconda, Pvenv, Poetry, Virtualenv, Docker` or whatever you want to isolate your environment.

```shell
$ cd llm-summarizer
$ conda env create --file environment.yml
done
#
# To activate this environment, use
#
#     $ conda activate summarizer
#
# To deactivate an active environment, use
#
#     $ conda deactivate
$ conda activate summarizer
```

## ⚡️ Install the application dependencies
Clone this repo and run the command bellow. Basically it creates the `summarize` entrypoint in your host:

```shell
$ pip install -e . --use-pep517
Obtaining file:///Users/renatorodrigues/Documents/Initiatives/AI/llm-summarizer
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Building wheels for collected packages: summarizer
  Building editable for summarizer (pyproject.toml) ... done
  Created wheel for summarizer: filename=summarizer-0.1.dev0-0.editable-py3-none-any.whl size=4459 sha256=9e534f5ee2d8d5c2eea44fbadf434b49c05d835be84def3168f99e67203bd64c
  Stored in directory: /private/var/folders/7j/n57v19mx0d793jbj3j559lxh0000gn/T/pip-ephem-wheel-cache-zeeafes_/wheels/df/29/ec/7b9176cd8ff44c6e2d536a80eaafabeabeb1a5bf5ade8c3d48
Successfully built summarizer
Installing collected packages: summarizer
Successfully installed summarizer-0.1.dev0
```

## 🧑🏻‍💻 Run Cli Mode!
Bellow are some examples of how to run it, you can also check `summarize --help` in order to see all available options. Eg.:

```shell
# Summarize with a transcription file and output path:
$ summarize -t path/to/transcription.txt -o path/to/output.md
    
# Summarize with a video file and output path:
$ summarize -v path/to/video.mp4 -o path/to/output.md
             
# Summarize with a specific LLM model and API URL:
$ summarize -t path/to/transcription.txt -o path/to/output.md -m custom-model -a http://custom-api-url
             
# Enable debug mode:
$ summarize -t path/to/transcription.txt -o path/to/output.md -d
             
# Keep the extracted audio and transcription files:
$ summarize -v path/to/video.mp4 -o path/to/output.md -k
             
# Provide a custom prompt for summarization:
$ summarize -t path/to/transcription.txt -o path/to/output.md -p "Summarize this video in details"
```

## 🤩 Run UI Chat Mode!
You can launch the UI for summarization in chat mode:

```shell
$ summarize --chat
* Running on local URL:  http://127.0.0.1:3007
2025-02-20 14:24:02 INFO _client _send_single_request HTTP Request: GET http://127.0.0.1:3007/gradio_api/startup-events "HTTP/1.1 200 OK"
2025-02-20 14:24:02 INFO _client _send_single_request HTTP Request: HEAD http://127.0.0.1:3007/ "HTTP/1.1 200 OK"

To create a public link, set `share=True` in `launch()`.
```
The application is launched and it's accessible at `http://localhost:3007`. For custom port, use `--chat-server-port` flag.

# 📦 How to run it in a docker container
In order to run it in a docker container using docker-compose, run the commands bellow:

```shell
$ cd llm-summarizer
$ docker-compose up -d --build

[+] Building 54.8s (12/12) FINISHED                              docker-container:default
[+] Running 4/4
 ✔ Network llm-summarizer_summarizer-network  Created                                0.0s 
 ✔ Volume "llm-summarizer_ollama-data"        Created                                0.0s 
 ✔ Container ollama-server                    Started                                0.1s 
 ✔ Container llm-summarizer-app-1             Started                                0.1s 

$ docker exec -it llm-summarizer-app-1 summarize --help
Usage: summarize  [OPTIONS]
Summarize a transcription or video file by extracting audio, transcribing it, and summarizing the content using an LLM. See usage examples below:
```

**Notes:** 
* ❗️**Perform a video summarization into a docker container could be extremely slow** depending on your hardware, the LLM model and the video's size. It requires huge amount of resources, so be patient or **run it locally in your host instead to get better performance!**
* The `docker-compose` setup maps a volume to the folder `/data` in your host, so you can put the sources files as well as the output file in there.
* The model `deepseek-r1:1.5b` is used as base llm and it's pulled from ollama repo when the `ollama-server` service is built. If you need to use a different
llm model, pull it inside the docker image. Eg:
  ```shell
  $ docker exec -it ollama-server ollama pull llama3.2:latest
  ```
## 🤩 UI Chat Mode in Docker
Launch the chat mode in docker using the command bellow:
```shell
$ docker exec -it llm-summarizer-app-1 summarize --chat
* Running on local URL:  http://0.0.0.0:3007
2025-02-20 17:28:32 INFO _client _send_single_request HTTP Request: GET http://localhost:3007/gradio_api/startup-events "HTTP/1.1 200 OK"
2025-02-20 17:28:32 INFO _client _send_single_request HTTP Request: HEAD http://localhost:3007/ "HTTP/1.1 200 OK"
```
**Notes:**
* ❗️ In `file path` textbox, be sure to fill out the value from `/data` folder. Eg.: `/data/transcription.txt`, `/data/video.mp4`
* For custom server port in chat mode, be sure to update/expose the custom port in `Dockerfile` and/or `docker-compose`.

## 🗑️ Uninstalling 
Bellow are the clean up steps in case you want to revert all isntallations

### ⚡️ Conda
If you installed Anaconda, deactivate and remove the environment created:
```shell
$ cd llm-summarizer
$ conda deactivate  
$ conda env remove -n summarizer -y
Remove all packages in environment /opt/anaconda3/envs/summarizer:

## Package Plan ##
  environment location: /opt/anaconda3/envs/summarizer

The following packages will be REMOVED:

  bzip2-1.0.8-h99b78c6_7
  ca-certificates-2025.1.31-hf0a4a13_0
  libexpat-2.6.4-h286801f_0
  libffi-3.4.2-h3422bc3_5
  liblzma-5.6.4-h39f12f2_0
  libsqlite-3.49.1-h3f77e49_1
  libzlib-1.3.1-h8359307_2
  ncurses-6.5-h5e97a16_3
  openssl-3.4.1-h81ee809_0
  pip-25.0.1-pyh8b19718_0
  python-3.12.8-hc22306f_1_cpython
  readline-8.2-h92ec313_1
  setuptools-75.8.0-pyhff2d567_0
  tk-8.6.13-h5083fa2_1
  tzdata-2025a-h78e105d_0
  wheel-0.45.1-pyhd8ed1ab_1

Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```

Then please check the the link [Uninstalling Anaconda Distribution](https://docs.anaconda.com/anaconda/uninstall)

### ⚡️ Application
Remove the installed `summarize` application. If you used Anaconda and removed the environment, the bellow step is not necessary:
```shell
$ pip uninstall summarizer -y
Found existing installation: summarizer 0.1.dev0
Uninstalling summarizer-0.1.dev0:
  Successfully uninstalled summarizer-0.1.dev0
```

### ⚡️ Ollama
If you are using ollama in your host, just remove all models that you've downloaded:
```shell
$ ollama rm deepseek-r1:1.5b
deleted 'deepseek-r1:1.5b'
```
In order to remove ollama from your host, follow the steps from [Ollama Documentation](https://github.com/ollama/ollama/tree/main/docs) for your specific OS.

### ⚡️ Docker
In case you used docker to execute this app, please run the command bellow:

```shell
$ docker-compose down -v
[+] Running 4/2
 ✔ Container llm-summarizer-app-1             Removed  11.2s 
 ✔ Container ollama-server                    Removed  10.3s 
 ✔ Volume llm-summarizer_ollama-data          Removed   0.0s 
 ✔ Network llm-summarizer_summarizer-network  Removed   0.0s 

$ docker rmi -f docker.io/library/llm-summarizer-app docker.io/ollama/ollama:0.5.7
Untagged: docker.io/library/llm-summarizer-app:latest
Untagged: docker.io/ollama/ollama:0.5.7
Deleted: 19201e530337a4ced5ffb434131ca75cac78df92fd465c9ecc72bd0dd694cb94
Deleted: 0ace9bc2a4e3c8a34a2db68df73c8fccbf38bb34a57ddc00a061bc809de9c026
```

# 🌍 Let's Connect & Collaborate!

I’m always excited to learn, share, and collaborate on AI and LLM-powered projects. If you find this project useful or have ideas to enhance it, let’s connect!

🚀 Connect with me on [LinkedIn](https://www.linkedin.com/in/renatorodriguesrs/) to exchange insights and stay updated on future innovations.
💬 Feel free to either fork this project or open issues, contribute—collaboration makes everything better!

Happy coding! 🤖✨