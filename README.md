# 🧠 AI Image Generator using Stable Diffusion

This project is a text-to-image AI generator built using the **Stable Diffusion v1.4** model from Hugging Face's `diffusers` library. It takes a natural language prompt as input and produces a high-quality, realistic image based on the prompt using a diffusion-based generative model.

---

## 🔍 Features

- 📥 Accepts user-defined text prompts  
- 🤖 Loads and uses the `CompVis/stable-diffusion-v1-4` model  
- ⚡ Automatically detects and utilizes GPU (if available)  
- 🖼 Generates and displays AI-generated images  
- 💾 Saves the generated image to disk (`image.png`)

---

## 📦 Technologies Used

- **Python 3.8+**
- **Hugging Face diffusers**
- **PyTorch**
- **PIL (Pillow)**
- **Google Colab / Jupyter Notebook** (for testing or running without local GPU)

---

## 💡 Use Cases

- Creative content generation for artists and writers  
- AI-assisted design for marketing and concept visualization  
- Educational demonstrations of text-to-image AI  
- Rapid prototyping for game and animation assets

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/AI-Image-Generator.git
cd AI-Image-Generator
```

### 2. Install required libraries
```bash
pip install -r requirements.txt
```
Or manually:
```bash
pip install diffusers torch transformers safetensors pillow
```

### 3. Run the project
```bash
python ai_image_generator.py
```
Enter your text prompt when asked. The generated image will be displayed and saved as `image.png`.

---

## 🖼 Sample Output

> (You can add a sample image here for visual reference)  
> ![sample_output](assets/sample_image.png)

---

## 📁 Project Structure

```
AI-Image-Generator/
├── ai_image_generator.py      # Main Python script
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── image.png                  # Sample output (generated)
└── assets/                    # (Optional) Screenshots or samples
```

---

## 🧑‍💻 Author

**Jeff Joe Antony**  
Python Developer Intern – Verveox Technologies  
[LinkedIn](https://www.linkedin.com/) | [GitHub](https://github.com/your-username)

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, modify, and share it.

---

## 🙏 Acknowledgements

- Thanks to **Verveox Technologies** for the internship opportunity and mentorship.
- Based on the amazing work by the [CompVis](https://github.com/CompVis) and [Hugging Face Diffusers](https://github.com/huggingface/diffusers) teams.
