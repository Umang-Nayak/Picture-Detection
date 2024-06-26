# Picture Detection

<video width="600" controls>
  <source src="demo/sample_video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Overview

Picture Detection is a project that allows users to upload images and receive descriptions in both text and voice. This functionality can be used in various applications such as accessibility tools, content description, and more.

## Features

- Upload an image to get a detailed description.
- Receive the description in both text and voice formats.
- User-friendly interface for easy interaction.


## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Umang-Nayak/Picture-Detection.git
    cd Picture-Detection
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    python app.py
    ```

## Usage

1. Open the application in your browser.
2. Upload an image using the upload button.
3. Wait for the description to be generated.
4. View the description in text format and listen to it via the voice output.

## Technologies Used

- Python
- Streamlit For UI
- Description Generator Via Google Model (gemini-1.0-pro-vision-latest)
- Text-to-Speech API (Google Text-to-Speech)

