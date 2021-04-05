import streamlit as st

st.write(
    """ # Hand Tracking in Pictures Using Google's MediaPipe Hands  """
)
output_placeholder = st.empty()

st.sidebar.info("General settings")
max_num_hands = st.sidebar.slider('Max number of hands:', 1, 6, 2, 1)
min_detection_confidence = st.sidebar.slider('Minimum detection confidence:', 0.1, 1.0, 0.5, 0.1)
st.sidebar.info("Input")
uploaded_files = st.sidebar.file_uploader("Upload JPG images of hands:", type=['jpg'], accept_multiple_files=True)
if len(uploaded_files) > 0:
    show_coordinates = st.sidebar.checkbox('Show index finger tips coordinates')
    predict_button = st.sidebar.button('Track Hands')