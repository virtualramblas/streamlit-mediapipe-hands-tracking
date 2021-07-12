# streamlit-mediapipe-hands-tracking
A [Streamlit](https://streamlit.io/) app for Google [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands).  
  
![App Demo Image](https://github.com/virtualramblas/streamlit-mediapipe-hands-tracking/blob/main/images/demo-image.PNG)  
  
MediaPipe is a suite of cross-platform, customizable ML solutions for live and streaming media. One of the provided solutions is an high-fidelity hand and finger tracking.  
This Streamlit web app allows hands tracking in static images. Mediapipe supports also video and live hands-tracking, but these features aren't yet covered by this demo app. Mediapipe hands tracking can be configured through this app UI through the following params:  
* Max number of hands to track: Mediapipe can track up to 4 hands in a single image or frame. Default for this app is set to 2.  
* Minimum detection confidence. Default is set to 50%. 
* Show/Hide Mediapipe classification results (index, score and label in JSON format). Default is set to False.  
  
### Setup for running the app
Anaconda and Python 3.7+ are required.

* Clone this repo.
* From the root directory of the project, create a conda virtual environment: *conda env create -f environment.yml*
* Activate the newly created virtual environment: *conda activate streamlit-mediapipe-hands*
* Run the app: *streamlit run app.py*  
* Open a web browser and go to http://localhost:8501
