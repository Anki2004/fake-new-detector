# import streamlit as st
# import requests

# Backend_url = "http://localhost:8501/predict"
# st.title("Fake new Detector")

# news_text = st.text_area("Enter the news text here")
# if st.button("check Auhtenticity"):
#     if news_text:
#         response = requests.post(Backend_url, json = {"data": news_text})
#         if response.status_code == 200:
#             result = response.json()

#             st.write(f"Prediction: {result['prediction']}")
#             st.write(f"Probability of being fake news: {result['probability']: .2f}")

#             if result['prediction'] == 'Fake':
#                 st.error('This news can be fake')
#             else:
#                 st.success("This news is likely to be real")

#         else:
#             st.error("Error Occured")
#     else:
#         st.warning("Please enter some text")

# st.markdown("------")
# st.write("This is just a simple model. Always verify from reliable sources")

import streamlit as st
import requests

# Set the backend URL
BACKEND_URL = "http://192.168.1.36:8501/predict"

st.title("Fake News Detector")

# Text input
news_text = st.text_area("Enter the news text here:")

if st.button("Check Authenticity"):
    if news_text:
        try:
            # Make a request to the backend
            response = requests.post(BACKEND_URL, json={"Headline": news_text}, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                
                st.write(f"Prediction: {result['prediction']}")
                st.write(f"Probability of being fake: {result['probability']:.2f}")
                
                # Visual indicator
                if result['prediction'] == 'Fake':
                    st.error("This news is likely to be fake!")
                else:
                    st.success("This news is likely to be real!")
            else:
                st.error(f"Error in prediction. Status code: {response.status_code}")
                st.info("The server responded, but with an unexpected status code.")
        
        except requests.exceptions.ConnectionError:
            st.error("Failed to connect to the backend server.")
            st.info("Please ensure the Flask backend is running on http://192.168.1.36:8501")
        
        except requests.exceptions.Timeout:
            st.error("The request to the backend server timed out.")
            st.info("The server might be overloaded or not responsive.")
        
        except requests.exceptions.RequestException as e:
            st.error(f"An unexpected error occurred: {e}")
            st.info("Please check your network connection and try again.")
        
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
            st.info("Please try again or contact support if the problem persists.")

    else:
        st.warning("Please enter some text to analyze.")

st.markdown("---")
st.write("Note: This is a simple model and may not be 100% accurate. Always verify news from reliable sources.")
st.markdown("---")
st.subheader("How it works")
st.write("""
This Fake News Detector uses a machine learning model to analyze the given text and predict whether it's likely to be real or fake news.

1. You enter the news text (Headline of the news) in the text area above.
2. When you click 'Check Authenticity', the text is sent to our backend server.
3. The server processes the text using a pre-trained model.
4. The model returns a prediction (Fake or Real) and a probability score.
5. The results are displayed on this page.

Please note that this is a simplified model and may not be 100% accurate. Always verify news from reliable sources.
""")

# Add a sidebar with additional information
st.sidebar.title("About")
st.sidebar.info("""
This app is a demonstration of a simple fake news detection system.
It uses natural language processing and machine learning techniques to analyze text content.

Remember: No automated system is perfect. Always cross-check information from multiple reliable sources.
""")

# You can add more elements to the sidebar if needed
st.sidebar.title("Tips for Spotting Fake News")
st.sidebar.markdown("""
- Check the source
- Read beyond the headline
- Check the author
- Check the date
- Check your biases
- Consult fact-checking websites
""")
