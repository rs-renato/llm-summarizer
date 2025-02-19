import logging,sys
from ollama import Client
from prompt import default_prompts

logger = logging.getLogger(__name__)

class OllamaClient:
    '''Handles connectons with llm's api.'''
    
    def __init__(self, llm_server_url: str, model: str, context_window: int):
        self.llm_server_url = llm_server_url
        self.model =  model
        self.context_window = context_window
        self.ollama_client = Client(host=llm_server_url)

    def generate(self, transcription: str, custom_prompt: str):
        logger.info('⏳ Starting the generation of transcription summarization')
       
        user_prompt = f'''
            {custom_prompt or default_prompts.user_prompt}
        '''
        
        logger.debug(f'✅ System prompt {default_prompts.system_prompt}')
        logger.debug(f'✅ User prompt: {user_prompt}')
        logger.debug(f'✅ Transcription: \n{transcription}')

        logger.info(f'⏳ Calling LLM API at: {self.llm_server_url}')
       
        chunks = self.ollama_client.chat(self.model,
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
            response = response.replace('```','').replace('markdown', '')
            sys.stdout.write('\r' + response)
            sys.stdout.flush()

        logger.debug(f'✅ Full LLM Response: {response}')

        return response
    
    def chat(self, message, history):
        logger.info('⏳ Starting the chat about the transcription summarization')

        if history is None:
            history =[]

        messages = [{"role": "system", "content": default_prompts.system_prompt}]

        for entry in history:
            messages.append({'role': entry['role'], 'content': entry['content']})

        messages.append({'role': 'user', 'content': message})

        logger.debug(f'✅ System prompt {default_prompts.system_prompt}')
        logger.debug(f'✅ User message: {message}')
        logger.debug(f'✅ Chat history: \n{history}')

        logger.info(f'⏳ Calling LLM API at: {self.llm_server_url}')

        stream = self.ollama_client.chat(
            model=self.model,
            messages=messages,
            stream=True,
            options={
                'num_ctx': self.context_window,
                'temperature': 0.1
            }    
        )

        response = ''
        for chunk in stream:
            response += chunk['message']['content']
            response = response.replace('<think>', '').replace('</think>', '\n\n --')
            yield response