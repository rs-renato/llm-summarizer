import logging
import os
from pathlib import Path
from audio.audio_extractor import AudioExtractor
from transcription.transcription_service import TranscriptionService
from summarization.summary_generator import SummaryGenerator
from utils.file_handler import FileHandler
from validation.argument_validator import ArgumentValidator

logger = logging.getLogger(__name__)
class Summarizer:
    '''Main application class that ties everything together.'''

    def __init__(self):
        self.transcription_service = TranscriptionService()

    def summarize_in_chat(
        self,
        message,
        history,
        transcription_file: str = None,
        video_file: str = None,
        output_file: str = None,
        llm_model: str = None,
        api_url: str = None,
        context_window: int = None,
        keep_files: bool = False,
    ):

        ArgumentValidator.validate_args(transcription_file, video_file)

        chat_message = message
        
        history = [entry for entry in history if entry.get('content') != '']

        if not history:
            _, transcription = self.generate_transcription(transcription_file, video_file, output_file, keep_files)
            chat_message = f'From the given transcription:\n{transcription}\n\n {message}'
        

        # Summarize transcription
        summary_generator = SummaryGenerator(llm_model, api_url, context_window)

        yield from summary_generator.chat(chat_message, history)

    def summarize(
        self,
        transcription_file: str = None,
        video_file: str = None,
        output_file: str = None,
        llm_model: str = None,
        api_url: str = None,
        custom_prompt: str = None,
        context_window: int = None,
        keep_files: bool = False,
    ):
        ArgumentValidator.validate_args(transcription_file, video_file)

        output_path, transcription = self.generate_transcription(transcription_file, video_file, output_file, keep_files)

        # Summarize transcription
        summary_generator = SummaryGenerator(llm_model, api_url, custom_prompt, context_window)

        summary = summary_generator.generate(transcription)

        # Save summary to file
        FileHandler.save_file(summary, output_path)

        logger.info('✅ Video transcription and content summary completed successfully! 🚀')

    def generate_transcription(self, transcription_file, video_file, output_file, keep_files):
        
        logger.info('Starting summarization process..')

        if output_file:
            output_path = Path(output_file).resolve()

        if not transcription_file:
            video_path = Path(video_file).resolve()
            audio_path = video_path.with_name(video_path.stem + '-audio').with_suffix('.mp3')

            # Extract audio from video file
            AudioExtractor.extract_audio(str(video_path), str(audio_path))

            # Transcribe audio from audio file
            transcription = self.transcription_service.transcribe(str(audio_path))
            transcription_path = video_path.with_name(video_path.stem + '-transcription').with_suffix('.txt')

            # Save or delete the generated files
            if keep_files:
                FileHandler.save_file(transcription, transcription_path)
            else:
                logger.info(f'Removing temporary audio file: {audio_path}')
                os.remove(audio_path)

            if not output_file:
                output_path = video_path.with_name(video_path.stem + '-summary').with_suffix('.md')
        else:
            # Reads transcription from file
            transcription = FileHandler.read_file(transcription_file)

            if not output_file:
                transcription_path = Path(transcription_file).resolve()
                output_path = transcription_path.with_name(transcription_path.stem + '-summary').with_suffix('.md')
                
        return output_path,transcription