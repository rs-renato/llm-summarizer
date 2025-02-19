from llm.ollama_client import OllamaClient

class SummaryGenerator:
    '''Handles summarization of transcriptions using an LLM.'''

    def __init__(self, model: str, api_url: str, custom_prompt: str = None, context_window: int = None ):
        self.custom_prompt = custom_prompt
        self.llm_client = OllamaClient(api_url, model, context_window)

    def generate(self, transcription: str) -> str:
       return self.llm_client.generate(transcription, self.custom_prompt)
    
    def chat(self, message, history):
       yield from self.llm_client.chat(message, history)