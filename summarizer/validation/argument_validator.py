import logging
import typer
from pathlib import Path

logger = logging.getLogger(__name__)

class ArgumentValidator:
    """Validates input arguments."""

    @staticmethod
    def validate_args(transcription_file, video_file):
        if video_file and transcription_file:
            logger.debug(f'-t {transcription_file} and -v {video_file} were provided.')
            typer.echo("[ERROR] ❌ --transcription and --video must not be provided together.")
            raise typer.Exit(code=1)

        if not video_file and not transcription_file:
            logger.debug(f'nor -t {transcription_file} or -v {video_file} were provided.')
            typer.echo("[ERROR] ❌ Either transcription or video must be provided.")
            raise typer.Exit(code=1)

        if video_file and not Path(video_file).is_file():
            logger.debug(f'The video file {video_file} does not exists.')
            typer.echo(f"[ERROR] ❌ Video file '{video_file}' does not exists.")
            raise typer.Exit(code=1)

        if transcription_file and not Path(transcription_file).is_file():
            logger.debug(f'The transcription file {transcription_file} does not exists.')
            typer.echo(f"[ERROR] ❌ Transcription file '{transcription_file}' does not exist.")
            raise typer.Exit(code=1)