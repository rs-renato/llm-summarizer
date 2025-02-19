import logging, os, sys
from openai import OpenAI
from prompt import default_prompts

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'ollama')

class OpenAIClient:
    '''Handles connectons with openai.'''
    
    def __init__(self, llm_server_url: str, model: str, context_window: str):
        self.llm_server_url = llm_server_url
        self.model =  model
        self.context_window=context_window
        self.openai = OpenAI(api_key=OPENAI_API_KEY, base_url=llm_server_url)

    def chat(self, transcription:str, custom_prompt: str):
        logging.info('⏳ Starting transcription summarization')
       
        user_prompt = f'''
            {custom_prompt or default_prompts.user_prompt}
        '''
        
        logging.debug(f'✅ System prompt {default_prompts.system_prompt}')
        logging.debug(f'✅ User prompt: {user_prompt}')
        logging.debug(f'✅ Transcription: \n{transcription}')

        logging.info(f'⏳ Calling LLM API at: {self.llm_server_url}')
        chunks = self.openai.chat.completions.create(
            model=self.model,
            messages=[
                {'role': 'system', 'content': default_prompts.system_prompt},
                {'role': 'user', 'content': user_prompt + '\n\nTranscription:\n' + transcription},
            ],
            max_tokens = self.context_window,
            temperature=0.3,
            stream=True
        )

        logging.info('⏳ Reading response from LLM API')
        response = ''
        for chunk in chunks:
            response += chunk.choices[0].delta.content or ''
            response = response.replace('```','').replace('markdown', '')
            sys.stdout.write('\r' + response)
            sys.stdout.flush()

        logging.debug(f'✅ Full LLM Response: {response}')

        return response