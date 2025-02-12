# Leveraging LLM to summarize video content

Over the past few weeks, I faced a challenge that many of us can relate to: how to efficiently consume hours of Knowledge Transfer (KT) videos without spending days watching them. With about 20 hours of KT videos to review, I knew there had to be a better way than sitting through every minute of footage. That’s when I decided to leverage the power of Large Language Models (LLMs) to create a solution.

I built a PoC python-based application that automatically extracts audio from videos, transcribes the content, and generates detailed summaries using an LLM. The result? Instead of spending 20 hours watching videos, I was able to read the summaries in just 40 minutes. That’s a 97% reduction in time spent! Now, my team can quickly grasp the main topics from the summaries and only dive into the original video when more details are needed.

# Why This Matters

In today’s fast-paced work environment, time is one of our most valuable resources. This tool not only saves time but also ensures that key insights are captured in a structured, easy-to-read format. It’s perfect for anyone dealing with long videos, whether it’s KT sessions, meeting recordings, or lectures.

**Check the full article on Linkedin:** [Leveraging LLM to summarize video content](https://www.linkedin.com/pulse/leveraging-llm-summarize-video-content-renato-rodrigues-q5mpf/)

# How to run it in your own host
First, let's install the dependencies for this project

## Ollama installation
Download and install [ollama](https://github.com/ollama/ollama) to integrate locally with the LLM tool. You can use the LLM as you want, however, it's nice to start with a lighther model such as  
`llama3.2:1b, qwen:1.8b, deepseek-r1:1.5b` or other that you want. If you have a big machine, go ahead and work with larger models. Be free to use Ollama in a docker container. If so, use the flag `-a http://custom-api-url` in the cli command.

```shell
$ ollama pull deepseek-r1:1.5b
```

## Conda installation
Download and install [conda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) to isolate your host environment from what's being installated as dependencies, then run the commands bellow to create an environment. If you preffer, you can work with `Miniconda, Pvenv, Poetry, Virtualenv, Docker` or whatever you want to isolate your environment.

```shell
$ cd llm-summarizer
$ conda create -n summarizer
$ conda activate summarizer
```

## Install the application dependencies
Clone this repo and run the command bellow:

```shell
$ pip install -e . --use-pep517
```

## Run it!
Bellow are some examples of how to run it, you can also check `summarize --help` in order to see all available options

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

# How to run it in docker container
In order to run it in a docker container using docker-compose, run the commands bellow:

```shell
$ cd llm-summarizer
$ docker-compose up -d --build

 ✔ Network llm-summarizer_summarizer-network  Created  0.0s 
 ✔ Volume "llm-summarizer_ollama-data"        Created  0.0s 
 ✔ Container ollama-server                    Started  0.1s 
 ✔ Container llm-summarizer-app-1             Started  0.1s 

$ docker exec -it llm-summarizer-app-1 summarize --help
```

*Notes:* 
* The `docker-compose` setup maps a volume to the folder `./data` in your host, so you can put the sources files as well as the output file in there.
* The model `deepseek-r1:1.5b` is used as base llm and it's pulled from ollama repo when the `ollama-server` service is built.