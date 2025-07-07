from diffusers import StableDiffusionPipeline
import torch
import matplotlib.pyplot as plt

def main():
  device = "cuda" if torch.cuda.is_available() else "cpu"

  pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4",
                                                 torch_dtype=torch.float16 if device == "cuda" else torch.float32,
                                                 use_safetensors=True).to(device)
                                              

  prompt = input("Enter image prompt: ")

  image = pipe(prompt).images[0]

  image.show()
  
  image.save("image.png")
  print("Image saved")

main()