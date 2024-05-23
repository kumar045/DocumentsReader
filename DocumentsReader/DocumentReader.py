import os
import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer
from helper import convert_file_to_images

def Load():
  # Initialize the model and tokenizer
  model = AutoModel.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5-int4', trust_remote_code=True)
  tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5-int4', trust_remote_code=True)
  model.eval()
  return model, tokenizer

def DocumentReader(FileName):

  convert_file_to_images(FileName)
  # Initialize the model and tokenizer
  model, tokenizer = Load()

  # Question to ask for each image
  question = 'Give data in json?'
  msgs = [{'role': 'user', 'content': question}]
  
  output_folder = 'output_folder'
  # Process each image in the folder
  for filename in os.listdir(output_folder):
      if filename.endswith('.png'):
          image_path = os.path.join(output_folder, filename)
          image = Image.open(image_path).convert('RGB')
          
          response = model.chat(
              image=image,
              msgs=msgs,
              tokenizer=tokenizer,
              sampling=True,
              temperature=0.7
          )
          
          return f"Response for {filename}:" , response
          
          
