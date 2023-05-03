import os
import gradio as gr

def inference(filepath):    
    return os.popen(f'tesseract {filepath} -').read().strip()

title = "Tesseract OCR"
description = "Gradio demo for Tesseract. Tesseract is an open source text recognition (OCR) Engine."
article = "<p style='text-align: center'><a href='https://tesseract-ocr.github.io/' target='_blank'>Tesseract documentation</a> | <a href='https://github.com/tesseract-ocr/tesseract' target='_blank'>Github Repo</a></p>"

examples = []

for img in os.listdir("/app/test_images"):
  examples.append(os.path.join("/app/test_images", img))

gr.Interface(
    inference, # Function to run for inference
    [gr.inputs.Image(type="filepath", label="Input")], # Input type (file upload)
    'text', # Output type (text)
    title=title, # Title of the app (informative)
    description=description, # Description of the app (informative)
    article=article, # Longer description of the app (informative)
    examples=examples, # Sample inputs (informative)
    allow_flagging=False, # Allow users to save inputs and outputs for later debugging/review
).launch(server_name="0.0.0.0", server_port=7780)