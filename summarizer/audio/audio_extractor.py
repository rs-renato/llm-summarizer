import logging
from moviepy.video.io.VideoFileClip import VideoFileClip

logger = logging.getLogger(__name__)

class AudioExtractor:
    '''Handles audio extraction from video files.'''

    @staticmethod
    def extract_audio(video_path: str, audio_path: str):
        logger.info(f'Starting audio extraction from video: {video_path}')
        VideoFileClip(video_path).audio.write_audiofile(audio_path)
        logger.info(f'✅ Audio extracted successfully: {audio_path}')