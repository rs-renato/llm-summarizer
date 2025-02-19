import os
os.environ['GRADIO_ANALYTICS_ENABLED'] = 'False'

from app.summarizer import Summarizer
import gradio as gr

def launchInterface():
    interface = create_interface()
    interface.launch(inbrowser=True, server_port=3007, share=False, enable_monitoring=False, show_api=False, show_error=True)

def file_check(file_path):
    if file_path.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):
        return file_path, None
    elif file_path.lower().endswith(('.txt', '.srt', '.vtt')):
        return None, file_path
    else:
        return None, None


def create_interface():
    with gr.Blocks() as demo:

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
                                info='The model needs to be pulled first',
                                choices=['deepseek-r1:1.5b', 'deepseek-r1:32b', 'llama3.2:1b', 'qwen:7b', 'gemma:7b', 'phi3:3.8b'],
                                allow_custom_value=True
                            )
                            context_window = gr.Number(label='Tokens', info='Context window size', value=4096)
                            api_url = gr.Textbox(label='Api', info= 'Local or remote API server to be connected to', value='http://localhost:11434', placeholder='URL of the LLM API server.')
            with gr.Column(scale=1):
                with gr.Tabs():
                    with gr.TabItem('File Path'):
                        source_file = gr.Textbox(autofocus=True, info='Either video or transcription file to be loaded', label='Source File Path', placeholder='Path to the input source file.')
                        video_file = gr.Textbox(visible=False, info='Source video file to be loaded', label='Video File Path', placeholder='Path to the input video file.', value=None)
                        transcription_file = gr.Textbox(visible=False, info='Source transcription file to be loaded', label='Transcription File Path', placeholder='Path to the transcription file.', value=None)
                        source_file.blur(file_check,
                            inputs=source_file,
                            outputs=[video_file, transcription_file]
                        )
     
                            
        gr.ChatInterface(
            fn= Summarizer().summarize_in_chat,
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
    
    return demo