import logging,sys
from ollama import chat
from prompt import default_prompts

logger = logging.getLogger(__name__)

class OllamaClient:
    """Handles connectons with llm's api."""
    
    def __init__(self, llm_server_url: str, model: str, context_window: int):
        self.llm_server_url = llm_server_url
        self.model =  model
        self.context_window = context_window

    def chat(self, transcription: str, custom_prompt: str):
        logger.info('⏳ Starting transcription summarization')
       
        user_prompt = f'''
            {custom_prompt or default_prompts.user_prompt}
        '''
        
        logger.debug(f'✅ System prompt {default_prompts.system_prompt}')
        logger.debug(f'✅ User prompt: {user_prompt}')
        logger.debug(f'✅ Transcription: \n{transcription}')

        logger.info(f'⏳ Calling LLM API at: {self.llm_server_url}')
       
        chunks = chat(self.model,
                    options={
                        'num_ctx': self.context_window,
                        'temperature': 0.3
                    },  
                    messages=[
                        {'role': 'system', 'content': default_prompts.system_prompt},
                        {'role': 'user', 'content': user_prompt},
                        {'role': 'user', 'content': transcription},
                ], stream=True)

        logger.info('⏳ Reading response from LLM API')
        response = ''
        for chunk in chunks:
            response += chunk['message']['content'] or ''
            response = response.replace("```","").replace("markdown", "")
            sys.stdout.write("\r" + response)
            sys.stdout.flush()

        logger.debug(f'✅ Full LLM Response: {response}')

        return response