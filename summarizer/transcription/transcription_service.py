import logging
from datetime import timedelta
from faster_whisper import BatchedInferencePipeline, WhisperModel

logger = logging.getLogger(__name__)

class TranscriptionService:
    '''Handles transcription of audio files using WhisperModel.'''

    def __init__(self, model_size: str = 'medium', language: str = 'en', compute_type: str = 'float32', batch_size: int = 8):
        self.model_size = model_size
        self.language = language
        self.compute_type = compute_type
        self.batch_size = batch_size

    def transcribe(self, audio_path: str) -> str:
        logger.info(f'⏳ Starting transcription for audio: {audio_path}')
        model = WhisperModel(self.model_size, cpu_threads=16, device='cpu', compute_type=self.compute_type)
        logger.debug(f'✅ Initialized WhisperModel with size: {self.model_size}, compute_type: {self.compute_type}')
        batched_model = BatchedInferencePipeline(model=model)
        logger.debug('✅ BatchedInferencePipeline initialized')
        segments, _ = batched_model.transcribe(audio_path, vad_filter=True, language=self.language, log_progress=True, batch_size=self.batch_size)
        transcription = '\n'.join(
            f'[{timedelta(seconds=int(segment.start))}-{timedelta(seconds=int(segment.end))}] {segment.text}'
            for segment in segments
        )
        logger.info('✅ Transcription completed successfully.')
        return transcription