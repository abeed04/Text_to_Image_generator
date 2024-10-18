<h1 align="center">Text-to-Image Generator Prototype</h1>
<h2 align="center">Introduction</h2>

- This project is a simple text-to-image generator prototype built using Streamlit for the user interface and the FLUX.1-schnell model from Gradio for the image generation backend.
- Users can input text prompts, and the app generates AI-created images based on the prompt, which can be downloaded.
- Tap below for Hugging Face app interface that generates images for given input prompts.

[![Open in Streamlit](https://cdn-lfs.hf.co/repos/96/a2/96a2c8468c1546e660ac2609e49404b8588fcf5a748761fa72c154b2836b4c83/942cad1ccda905ac5a659dfd2d78b344fccfb84a8a3ac3721e08f488205638a0?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27hf-logo.svg%3B+filename%3D%22hf-logo.svg%22%3B&response-content-type=image%2Fsvg%2Bxml&Expires=1729517380&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcyOTUxNzM4MH19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5oZi5jby9yZXBvcy85Ni9hMi85NmEyYzg0NjhjMTU0NmU2NjBhYzI2MDllNDk0MDRiODU4OGZjZjVhNzQ4NzYxZmE3MmMxNTRiMjgzNmI0YzgzLzk0MmNhZDFjY2RhOTA1YWM1YTY1OWRmZDJkNzhiMzQ0ZmNjZmI4NGE4YTNhYzM3MjFlMDhmNDg4MjA1NjM4YTA%7EcmVzcG9uc2UtY29udGVudC1kaXNwb3NpdGlvbj0qJnJlc3BvbnNlLWNvbnRlbnQtdHlwZT0qIn1dfQ__&Signature=nPvk8koM-VabyqEaPfTcc%7EDu-pm2EeicoPtaCNS2DmMTIi1ikBORlLbwiyOTgTiuYekzQrMWSXR8O4ZOfZq7vMtqyhpRM3C-e6wASjPjS0PVJeo3T7%7EEH1LEDK1hk60IwSuribuSKsp-LPvBd0KNsS8brVMyirUhPUHx6TVZ0Z384ORInqJ2ofppkA7xT9fGj2r0uq2ljEx7ZZQ3tWSrro-t2OGOjrbeWb8ciVzsW6FbrqtN6EYbuuHqlJQbqQx0HxdKMOvMUfDf5eLTdcbigfYxQp%7EszJ2dv1kmK9Bl2KR6O6DHO3e5QlnlB0qBtTqX-i3OV2tEynMG1f-xgaWKpQ__&Key-Pair-Id=K3RPWS32NSSJCE)](https://huggingface.co/spaces/abeed04/Text-to-Image-Generator)

<h2 align="center">Features</h2>
- Allows users to input text prompts.
- Generates an image based on the entered prompt.
- Provides a download button for the generated image.
- Simple progress bar indicating image generation status.

<h2 align="center">Installation </h2>
Prerequisites

- Python 3.7+
- Streamlit
- Gradio Client
- shutil and os are part of the Python standard library.

Install the requirements

   ```
   pip install -r requirements.txt
   ```

 Run the app

   ```
   streamlit run app.py
   ```
<h2 align="center">Usage</h2>

- Change save_dir in app.py file so that images will be saved directly to your directory
- Run the app.py file using the instructions above.
- Input a text prompt in the sidebar.
- Click on the "Generate Image" button to start generating.
- Wait for the progress bar to complete, and your generated image will appear on the screen.
- Click the "Download Image" button to save the image locally.

<h2 align="center">Model Selection</h2>
I selected FLUX.1-schnell, an open-source model accessible via Gradio, due to its robust text-to-image capabilities and ease of integration into web-based applications. It is designed to efficiently convert text prompts into high-quality images, making it ideal for prototyping projects like this.

I opted for a pre-trained model rather than building one from scratch because:
- Simplicity: FLUX.1-schnell offers an accessible API with ready-to-use image generation without needing extensive training.
- Versatility: It handles a wide variety of input prompts and can generate detailed, aesthetically pleasing images.
- Time efficiency: Given the assignment's deadline, using a pre-trained model minimizes setup time while ensuring high-quality results.
