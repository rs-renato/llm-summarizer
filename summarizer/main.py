import typer, logging, os
from app.summarizer import Summarizer
from ui.ui_interface import launchInterface

LLM_MODEL = os.getenv('LLM_MODEL', 'deepseek-r1:1.5b')
LLM_SERVER_URL = os.getenv('LLM_SERVER_URL', 'http://localhost:11434')

app = typer.Typer(invoke_without_command=False)

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
    handlers=[
        logging.FileHandler(
            filename='llm-summarizer.log',
            encoding='utf-8',
            mode='w'),
        logging.StreamHandler()
    ]
)

# Configure commands
@app.command(no_args_is_help=True, help='''
    Summarize a transcription or video file by extracting audio, transcribing it, and summarizing the content using an LLM. See usage examples below::\n
             
    1. Summarize with a transcription file and output path:
    python main.py summarize -t path/to/transcription.txt -o path/to/output.md\n\n
    
    2. Summarize with a video file and output path:
    python main.py summarize -v path/to/video.mp4 -o path/to/output.md\n\n
             
    3. Summarize with a specific LLM model and API URL:
    python main.py summarize -t path/to/transcription.txt -o path/to/output.md -m custom-model -a http://custom-api-url\n\n
             
    4. Enable debug mode:
    python main.py summarize -t path/to/transcription.txt -o path/to/output.md -d\n\n
             
    5. Keep the extracted audio and transcription files:
    python main.py summarize -v path/to/video.mp4 -o path/to/output.md -k\n\n
             
    6. Provide a custom prompt for summarization:
    python main.py summarize -t path/to/transcription.txt -o path/to/output.md -p 'Summarize this video in detail'\n\n
             
    Note: You can optionally set the environment variable OPENAI_API_KEY for the OpenAI API key.
''')
def summarize(
    transcription_file: str = typer.Option(None, '-t', '--transcription', help='Path to the transcription file.'),
    video_file: str = typer.Option(None, '-v', '--video', help='Path to the input video file.'),
    output_file: str = typer.Option(None, '-o', '--output', help='Path to save the markdown output file.'),
    llm_model: str = typer.Option(LLM_MODEL, '-m', '--model', help='LLM model name.'),
    api_url: str = typer.Option(LLM_SERVER_URL, '-a', '--api-llm-url', help='URL of the LLM API server.'),
    custom_prompt: str = typer.Option(None, '-p', '--prompt', help='Custom user prompt. At the end of the prompt, the video transcription will be appended.'),
    context_window: int = typer.Option(4096, '-c', '--context-window', help='Custom context window size.'),
    chat_mode: bool = typer.Option(False, '--chat', help='Launch the UI for summarization in chat mode.'),
    keep_files: bool = typer.Option(False, '-k', '--keep-files', help='Keep the audio and transcription extracted from video source.'),
    debug: bool = typer.Option(False, '-d', '--debug', help='Enable debug mode.')
):
    if debug:
        logger.setLevel(logging.DEBUG)
    
    if chat_mode:
        launchInterface()
    else:
        Summarizer().summarize(
            transcription_file,
            video_file,
            output_file,
            llm_model,
            api_url,
            custom_prompt,
            context_window,
            keep_files,
            chat_mode
        )

if __name__ == '__main__':
    app()