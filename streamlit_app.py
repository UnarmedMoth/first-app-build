import streamlit as st
from googletrans import Translator
import asyncio

# Mapping of language names to their ISO 639-1 codes (same as in your code)
language_code_map = {
    "Afrikaans": "af",
    "Akan": "ak",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Assamese": "as",
    "Aymara": "ay",
    "Azerbaijani": "az",
    "Bambara": "bm",
    "Bangla": "bn",
    "Basque": "eu",
    "Belarusian": "be",
    "Bhojpuri": "bh",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Burmese": "my",
    "Catalan": "ca",
    "Cebuano": "ceb",
    "Central Kurdish": "ckb",
    "Chinese (Simplified)": "zh-cn",
    "Chinese (Traditional)": "zh-tw",
    "Corsican": "co",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Divehi": "dv",
    "Dogri": "doi",
    "Dutch": "nl",
    "English": "en",
    "Esperanto": "eo",
    "Estonian": "et",
    "Ewe": "ee",
    "Filipino": "tl",
    "Finnish": "fi",
    "French": "fr",
    "Galician": "gl",
    "Ganda": "lg",
    "Georgian": "ka",
    "German": "de",
    "Goan Konkani": "gom",
    "Greek": "el",
    "Guarani": "gn",
    "Gujarati": "gu",
    "Haitian Creole": "ht",
    "Hausa": "ha",
    "Hawaiian": "haw",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hmong": "hmn",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Igbo": "ig",
    "Iloko": "ilo",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jv",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Khmer": "km",
    "Kinyarwanda": "rw",
    "Korean": "ko",
    "Krio": "kr",
    "Kurdish": "ku",
    "Kyrgyz": "ky",
    "Lao": "lo",
    "Latin": "la",
    "Latvian": "lv",
    "Lingala": "ln",
    "Lithuanian": "lt",
    "Luxembourgish": "lb",
    "Macedonian": "mk",
    "Maithili": "mai",
    "Malagasy": "mg",
    "Malay": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Manipuri (Meitei Mayek)": "mni",
    "Māori": "mi",
    "Marathi": "mr",
    "Mizo": "mzn",
    "Mongolian": "mn",
    "Nepali": "ne",
    "Northern Sotho": "nso",
    "Norwegian": "no",
    "Nyanja": "ny",
    "Odia": "or",
    "Oromo": "om",
    "Pashto": "ps",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Quechua": "qu",
    "Romanian": "ro",
    "Russian": "ru",
    "Samoan": "sm",
    "Sanskrit": "sa",
    "Scottish Gaelic": "gd",
    "Serbian": "sr",
    "Shona": "sn",
    "Sindhi": "sd",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Southern Sotho": "st",
    "Spanish": "es",
    "Sundanese": "su",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tajik": "tg",
    "Tamil": "ta",
    "Tatar": "tt",
    "Telugu": "te",
    "Thai": "th",
    "Tigrinya": "ti",
    "Tsonga": "ts",
    "Turkish": "tr",
    "Turkmen": "tk",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uyghur": "ug",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Western Frisian": "fy",
    "Xhosa": "xh",
    "Yiddish": "yi",
    "Yoruba": "yo",
    "Zulu": "zu"
}

st.title("Language Translation App")

source_text = st.text_area("Enter text to translate:")
target_language_name = st.selectbox("Select target language:", list(language_code_map.keys()))
target_language_code = language_code_map.get(target_language_name)

translate_button = st.button('Translate')

# Define the async translation function
async def translate_text_async(source_text, target_language_code):
    translator = Translator()
    result = await translator.translate(source_text, dest=target_language_code)
    return result.text

# Wrapper function to run async function
def translate_text(source_text, target_language_code):
    return asyncio.run(translate_text_async(source_text, target_language_code))

if translate_button:
    if source_text.strip():  # Check if text is not empty
        translated_text = translate_text(source_text, target_language_code)
        st.write(translated_text)  # Display translated text
    else:
        st.write("Please enter text to translate.")  # Handle empty text case
