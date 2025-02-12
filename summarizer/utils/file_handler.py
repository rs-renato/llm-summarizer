import logging

logger = logging.getLogger(__name__)

class FileHandler:
    """Handles file operations like saving and reading files."""

    @staticmethod
    def save_file(file: str, output_path: str):
        logger.info(f'⏳ Saving file to: {output_path}')
        with open(output_path, 'w') as f:
            f.write(file)
        logger.info(f'✅ File saved successfully to: {output_path}')

    @staticmethod
    def read_file(file_path: str) -> str:
        logger.info(f'⏳ Reading file: {file_path}')
        with open(file_path, 'r') as f:
            content = f.read()
        logger.info(f'✅ File read successfully: {file_path}')
        return content