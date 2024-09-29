from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as ggi

# Load the API key from the .env file
load_dotenv(".env")
fetcheed_api_key = os.getenv("API_KEY")

# Configure the Google Gemini API
ggi.configure(api_key=fetcheed_api_key)

# Initialize the Gemini model (Gemini Pro in this case)
model = ggi.GenerativeModel("gemini-pro")
chat = model.start_chat()

# Function to generate chatbot response
def LLM_Response(question):
    if st.session_state.language == "English":
        initial_context = ("You are an AI assistant providing legal information specific to "
                           "the state of Florida. Explain legal terms in plain language and provide easy-to-understand advice.")
    elif st.session_state.language == "Español":
        initial_context = (
            "Eres un asistente de IA que proporciona información legal en Florida. Explica los términos legales en un lenguaje simple.")
    else:  # Haitian Creole
        initial_context = (
            "Ou se yon asistan IA k ap bay enfòmasyon legal nan Florid. Eksplike tèm legal yo nan yon fason senp.")

    response = chat.send_message(initial_context + " " + question, stream=True)
    return response

# Sidebar language selection
if "language" not in st.session_state:
    st.session_state.language = "English"

# Define translations for each language
translations = {
    "English": {
        "title": "Empowering Immigrants: Your Legal Rights in Florida",
        "intro": "LegalEase is a cutting-edge platform dedicated to empowering immigrants who call Florida home. Our mission is simple: to provide clear, accessible information about your legal rights and protections as a resident of the United States.",
        "support": "Whether it’s understanding your housing rights, employment protections, or other important legal matters, LegalEase is here to support you every step of the way.",
        "cta_title": "Get Answers, Stay Informed",
        "cta_text": "Have questions? Our AI Legal Assistant is ready to help. Ask a question below and get straightforward, easy-to-understand answers to navigate your legal rights with confidence.",
        "rental_rights": "Florida Rental Rights",
        "employment_rights": "Employment Rights",
        "healthcare_rights": "Healthcare Rights",
        "ask_chatbot": "Ask the AI Legal Assistant",
        "input_placeholder": "Ask your question here...",
        "response_header": "AI Response:",
        "select_language": "Select Language / Seleccionar Idioma / Chwazi Lang",
        "home": "Home",
        "input_prompt": "Got a question? I'm here to help!",  # Ensure this key is present
        "employment_rights_image": "/Users/patrickdavenport/PycharmProjects/LegalEase/Images/FER_English.png",
        "employment_rights_pdf": "/Users/patrickdavenport/PycharmProjects/LegalEase/PDFS/FER_English.pdf",
    },
    "Español": {
        "title": "Empoderando a los Inmigrantes: Sus Derechos Legales en Florida",
        "intro": "LegalEase es una plataforma de vanguardia dedicada a empoderar a los inmigrantes que llaman hogar a Florida. Nuestra misión es simple: proporcionar información clara y accesible sobre sus derechos legales y protecciones como residente de los Estados Unidos.",
        "support": "Ya sea comprender sus derechos de vivienda, protecciones laborales u otros asuntos legales importantes, LegalEase está aquí para apoyarlo en cada paso del camino.",
        "cta_title": "Obtenga Respuestas, Manténgase Informado",
        "cta_text": "¿Tiene preguntas? Nuestro Asistente Legal AI está listo para ayudar. Haga una pregunta a continuación y obtenga respuestas claras y sencillas para navegar por sus derechos legales con confianza.",
        "rental_rights": "Derechos de Alquiler en Florida",
        "employment_rights": "Derechos Laborales",
        "healthcare_rights": "Derechos de Atención Médica",
        "ask_chatbot": "Pregunte al Asistente Legal AI",
        "input_placeholder": "Escribe tu pregunta aquí...",
        "response_header": "Respuesta AI:",
        "select_language": "Select Language / Seleccionar Idioma / Chwazi Lang",
        "home": "Inicio",
        "input_prompt": "¿Tienes una pregunta? Estoy aquí para ayudarte!"  # Ensure this key is present
    },
    "Kreyòl Ayisyen": {
        "title": "Ankouraje Imigran: Dwa Legal ou nan Florid",
        "intro": "LegalEase se yon platfòm inovatè ki dedye pou ede imigran ki konsidere Florid kòm kay yo. Misyon nou senp: bay enfòmasyon klè ak aksesib sou dwa legal ou ak pwoteksyon ou kòm yon rezidan Etazini.",
        "support": "Kèlkeswa si se konprann dwa lojman ou, pwoteksyon travay ou, oswa lòt kesyon legal enpòtan, LegalEase la pou sipòte ou nan chak etap.",
        "cta_title": "Jwenn Repons, Rete Enfòme",
        "cta_text": "Ou gen kesyon? Asistan Legal AI nou an pare pou ede ou. Poze yon kesyon anba a epi jwenn repons klè ak senp pou ede w navige dwa legal ou avèk konfyans.",
        "rental_rights": "Dwa Lwaye Florid",
        "employment_rights": "Dwa Travay",
        "healthcare_rights": "Dwa Swen Sante",
        "ask_chatbot": "Mande Asistan Legal AI a",
        "input_placeholder": "Poze kesyon w la isit...",
        "response_header": "Repons AI:",
        "select_language": "Select Language / Seleccionar Idioma / Chwazi Lang",
        "home": "Akèy",
        "input_prompt": "Ou gen yon kesyon? Mwen la pou ede ou!"  # Ensure this key is present
    }
}


# Display language selection in sidebar
language = st.sidebar.selectbox(
    "Please select your preferred language:",
    ["English", "Español", "Kreyòl Ayisyen"],
    index=["English", "Español", "Kreyòl Ayisyen"].index(st.session_state.language),
)

# Update session state when language is selected
if language != st.session_state.language:
    st.session_state.language = language

# Access the selected language translations
translation = translations[st.session_state.language]

# Apply custom styling for the logo, header, and text
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap');  /* Modern font from Google Fonts */

    .top-left-logo {
        position: absolute;
        top: 20px;
        left: 20px;
        width: 100px;  /* Adjust size here */
    }

    .header-text {
        font-family: 'Roboto', sans-serif;
        color: #B5CDA3;  /* Muted sage */
        text-align: left;
        font-size: 24px;
        font-weight: bold;
        margin-top: 10px;  /* Reduced margin to avoid overlap */
        margin-bottom: 40px;
        line-height: 1.4;
    }
    
    .title {
        font-family: 'Roboto', sans-serif;
        color: #F7E7A6;  /* Soft yellow color */
        font-size: 38px;  /* Larger font size */
        font-weight: bold;
        margin-top: 20px;  /* Space above the title */
    }

    .cta {
        font-family: 'Roboto', sans-serif;
        color: #F7CAC9;  /* Muted peach */
        text-align: left;
        font-size: 18px;
        font-weight: normal;
        margin-top: 20px;
        line-height: 1.4;
    }
    </style>
""", unsafe_allow_html=True)

# Display the logo in the top-left corner
st.image("Images/LegalEaseStreamlitLogo.png", use_column_width=False)

# Display the header text below the logo, with margin to avoid overlap (ONLY ONCE HERE)
st.markdown(f"""
    <div class='header-text'>
        {translation['title']}<br><br>
        {translation['intro']}<br><br>
        {translation['support']}
    </div>
""", unsafe_allow_html=True)

# Sidebar navigation for pages
st.sidebar.title("Navigate")
page = st.sidebar.radio(
    "Go to:",
    (translation["home"], translation["rental_rights"], translation["employment_rights"],
     translation["healthcare_rights"])
)

# Define page content based on user selection
if page == translation["home"]:
    # Display the call to action (with translations)
    st.markdown(f"""
        <div class='cta'>
            <strong>{translation['cta_title']}</strong><br>
            {translation['cta_text']}
        </div>
    """, unsafe_allow_html=True)

    # Place the chatbot on the landing page
    st.title(translation["ask_chatbot"])
    user_quest = st.text_input(translation["input_prompt"])

    if st.button("Ask"):
        if user_quest:
            result = LLM_Response(user_quest)
            st.subheader(translation["response_header"])
            for word in result:
                st.write(word.text)

    # Add a disclaimer
    st.write(
        "**Disclaimer:** This chatbot provides general legal information based on Florida laws. It is not a substitute for legal advice from a licensed attorney.")

elif page == translation["rental_rights"]:
    #st.title(translation["rental_rights"])

    image_filenames = {
        "English": "LegalEase/Images/FRR_English.png",
        "Español": "LegalEase/Images/FRR_Spanish.png",
        "Kreyòl Ayisyen": "LegalEase/Images/FRR_Kreyol.png"
    }

    # Get the correct image path based on the selected language
    image_path = image_filenames.get(st.session_state.language, image_filenames["English"])

    # Display the rental rights image
    st.image(image_path, use_column_width=True)

elif page == translation["employment_rights"]:
    #st.title(translation["employment_rights"])

    # Get the correct image and PDF path based on the selected language
    employment_image_path = translation.get("employment_rights_image")
    employment_pdf_path = translation.get("employment_rights_pdf")

    # Check if the image file exists before displaying it
    if os.path.exists(employment_image_path):
        st.image(employment_image_path, use_column_width=True)
    else:
        st.write("Employment rights image not found.")

    # Provide a download button for the PDF
    if os.path.exists(employment_pdf_path):
        with open(employment_pdf_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        st.download_button(
            label="Download Employment Rights PDF",
            data=pdf_bytes,
            file_name=employment_pdf_path.split("/")[-1],  # Use the filename from the path
            mime="application/pdf",
        )
    else:
        st.write("Employment rights PDF not found.")

elif page == translation["healthcare_rights"]:
    st.title(translation["healthcare_rights"])
