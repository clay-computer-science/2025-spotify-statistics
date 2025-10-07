# 2025-spotify-statistics

### INTRO

We will be creating a web application using flask to pull information from the spotify api and display it across several screens.

## Getting started

To get going on this we will need to ensure that you have the ability to run and build python applications.

I have created a first assignment document in the google drive. Please complete the tasks there as well as the setup contained below. 

## You Will Need

To open and run Python applications on your machine, follow these steps:

1. **Install Python**:
   - Download and install Python 3.10 or higher from [python.org](https://www.python.org/).
   - During installation, ensure you check the box to add Python to your system PATH.

2. **Install a Code Editor**:
   - Install Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com/).
   - Add the Python extension for Visual Studio Code.
   - clone the repo from github at https://github.com/clay-computer-science/2025-spotify-statistics

3. **Set Up a Virtual Environment**:
   - Open a terminal in your project directory and run:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows**:
       ```bash
       .\venv\Scripts\activate
       ```
     - **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```

4. **Install Required Packages**:
   - Install the dependencies listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

5. **Run the Application**:
   - Start the Flask development server:
     ```bash
     flask run
     ```
   - Open your browser and navigate to `http://127.0.0.1:5000`.

6. **Troubleshooting**:
   - If you encounter issues, ensure your virtual environment is activated and all dependencies are installed.

### Getting the spotify api information
In order to share the  spotify api information I will need to add you to the application in spotify. I will need your name and email. Please provide it in the Team member info document in the google drive linked below. 

### Creating the `.env` File

Since the `.env` file is not included in the repository, you will need to create it manually. Follow these steps:

1. In the root directory of the project, create a new file named `.env`.
2. Add the following content to the file:
   ```env
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   REDIRECT_URI=http://127.0.0.1:5000/callback
   ```
3. Replace `your_spotify_client_id` and `your_spotify_client_secret` with your Spotify API credentials. This will be located on your spotify dashboard page once I share it with you. There is a link to it here: https://developer.spotify.com/documentation/web-api/concepts/apps

This file is essential for the application to authenticate with the Spotify API.

# Parting notes
If any of this seems wrong its because I havent set this up in a long time and used AI to get me this far because I'm lazy. If you find an issue or would just like to tell me I am an idiot, please do so. 

## Resources

google drive link: https://drive.google.com/drive/folders/1ELmnHIoT-UzxbhZlfrzVeL_FhqVGvJas?usp=drive_link
