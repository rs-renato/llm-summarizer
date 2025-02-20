import os
os.environ['GRADIO_ANALYTICS_ENABLED'] = 'False'
LLM_SERVER_URL = os.getenv('LLM_SERVER_URL', 'http://localhost:11434')
LLM_MODEL = os.getenv('LLM_MODEL', 'deepseek-r1:1.5b')

from app.summarizer import Summarizer
import gradio as gr

class GradioInterface:
    def __init__(self):
        self.interface = self.create_interface()

    def create_interface(self):
        with gr.Blocks(title='Summarizer') as gr_interface:

            gr.Markdown('''
                            # Leveraging LLM to summarize content.
                            ### Made with ❤️ by [Renato Rodrigues](https://www.linkedin.com/in/renatorodriguesrs)
                        ''')

            with gr.Row():
                with gr.Column(scale=1):
                    with gr.Tabs():
                        with gr.TabItem('LLM Config'):
                            with gr.Row():        
                                llm_model = gr.Dropdown(
                                    label='Model',
                                    value=LLM_MODEL,
                                    info='The model needs to be pulled first',
                                    choices=['deepseek-r1:1.5b', 'deepseek-r1:32b', 'llama3.2:1b', 'qwen:7b', 'gemma:7b', 'phi3:3.8b'],
                                    allow_custom_value=True
                                )
                                context_window = gr.Number(label='Tokens', info='Context window size', value=4096)
                                api_url = gr.Textbox(label='Api', info= 'Local or remote API server to be connected to', value=LLM_SERVER_URL, placeholder='URL of the LLM API server.')
                with gr.Column(scale=1):
                    with gr.Tabs():
                        with gr.TabItem('File Path'):
                            source_file = gr.Textbox(autofocus=True, info='Either video or transcription file to be loaded', label='Source File Path', placeholder='Path to the input source file.')
                            video_file = gr.Textbox(visible=False, info='Source video file to be loaded', label='Video File Path', placeholder='Path to the input video file.', value=None)
                            transcription_file = gr.Textbox(visible=False, info='Source transcription file to be loaded', label='Transcription File Path', placeholder='Path to the transcription file.', value=None)
                            source_file.blur(self.file_check,
                                inputs=source_file,
                                outputs=[video_file, transcription_file]
                            )
        
                                
            gr.ChatInterface(
                fn= self.fn_chat,
                type='messages',
                flagging_mode='never',
                save_history=True,
                analytics_enabled=False,
                additional_inputs=[
                    transcription_file,
                    video_file,
                    gr.Textbox(visible=False, value=None),
                    llm_model,
                    api_url,
                    context_window,
                    gr.Checkbox(visible=False, value=False), 
                ]
            )
        
        return gr_interface
    
    def fn_chat(self, *args, **kwargs):
        try:
            history = [entry for entry in args[1] if entry.get('content') != '']
            if not history:
                gr.Info(message='The file will be processed and summarized..')
            
            yield from Summarizer().summarize_in_chat(*args, **kwargs)
        except BaseException as e:
            raise gr.Error(str(e))

    def launch(self, inbrowser:bool = True, server_port:int=3007):
        server_host = '0.0.0.0' if os.getenv('DOCKER_ENV') else '127.0.0.1'
        self.interface.launch(inbrowser=inbrowser, server_name=server_host, server_port=server_port, share=False, enable_monitoring=False, show_api=False, show_error=True)

    def file_check(self,file_path):        
        if file_path.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):
            return file_path, None
        elif file_path.lower().endswith(('.txt', '.srt', '.vtt')):
            return None, file_path
        else:
            return None, None
        