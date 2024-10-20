import os
import shutil
import streamlit as st
from gradio_client import Client
import time

save_dir = r"C:\Users\abeed\OneDrive\Pictures"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

client = Client("black-forest-labs/FLUX.1-schnell")

# Streamlit layout with sidebar for input
st.sidebar.title("Image Generation Prompt")
prompt = st.sidebar.text_area("Enter your prompt:", "")

generate_image = st.sidebar.button("Generate Image")

if generate_image:
    if prompt:
            # Initialize the progress bar
            progress_bar = st.progress(0)
            st.info("Generating your image, please wait...")

            # Update progress
            for percent_complete in range(0, 100, 20):  
                time.sleep(0.5) 
                progress_bar.progress(percent_complete)

            # Generate the image using the prompt
            result = client.predict(
                prompt=prompt,
                seed=0,
                randomize_seed=True,
                width=1024,
                height=1024,
                num_inference_steps=4,
                api_name="/infer"
            )
            
            # Complete progress bar
            progress_bar.progress(100)

            image_path = result[0]  # This is the path to the generated image

            # Define the destination path where you want to save
            save_path = os.path.join(save_dir, "generated_image.png")

            # Move the image from the temporary location to the desired directory
            shutil.move(image_path, save_path)

            # Display the image in Streamlit
            st.image(save_path, caption="Generated Image", use_column_width=True)

            # Provide download link
            with open(save_path, "rb") as file:
                st.download_button(
                    label="Download Image",
                    data=file,
                    file_name="generated_image.png",
                    mime="image/png"
                )

            st.success("Image generated ")
    else:
        st.error("Please enter a prompt to generate the image.")
