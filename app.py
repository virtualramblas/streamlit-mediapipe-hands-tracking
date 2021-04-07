import cv2
import mediapipe as mp
import numpy as np
import streamlit as st
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def track_hands_in_images(file_list, max_num_hands, min_detection_confidence):
    annotated_images = []
    multi_handednesses = []
    
    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=max_num_hands,
        min_detection_confidence=min_detection_confidence) as hands:
        for uploaded_file in file_list:
            image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
            image = cv2.flip(image, 1)
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            if not results.multi_hand_landmarks:
                continue
            multi_handednesses.append(results.multi_handedness)
            annotated_image = image.copy()
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            annotated_images.append(annotated_image)
            
    return annotated_images, multi_handednesses

st.write(
    """ # Hand Tracking in Pictures Using Google's MediaPipe Hands  """
)

st.sidebar.info("General settings")
max_num_hands = st.sidebar.slider('Max number of hands:', 1, 4, 2, 1)
min_detection_confidence = st.sidebar.slider('Minimum detection confidence:', 0.1, 1.0, 0.5, 0.1)
st.sidebar.info("Input")
uploaded_files = st.sidebar.file_uploader("Upload JPG images of hands:", type=['jpg'], accept_multiple_files=True)
if len(uploaded_files) > 0:
    show_results = st.sidebar.checkbox('Show classification results')
    track_button = st.sidebar.button('Track Hands')
    if track_button:
        annotated_images, multi_handednesses = track_hands_in_images(uploaded_files, max_num_hands, min_detection_confidence)
        if len(annotated_images) > 0:
            for idx, annotated_image in enumerate(annotated_images):
                annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
                st.image(cv2.flip(annotated_image, 1))
                if show_results:
                    st.write(str(multi_handednesses[idx]))