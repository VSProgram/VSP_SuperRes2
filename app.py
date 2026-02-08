import gradio as gr
from func_model import sr_func

def function_selection(image_data):
    image = image_data['composite']
    new_image = sr_func(image)
    return new_image


app = gr.Interface(
    fn=function_selection,
    inputs=[
        gr.ImageEditor(
            label='Загрузите фотографию и выделите область (если это необходимо)',
            type='pil'
        ),
    ],
    outputs=gr.Image(
                    type='pil',
                     label = 'Результат'
        ),
)

app.launch(server_name='0.0.0.0', server_port=7860)

