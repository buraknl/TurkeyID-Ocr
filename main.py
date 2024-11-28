import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image
import numpy as np

ocr = PaddleOCR(use_angle_cls=True, lang='tr')

st.title("Türk Kimlik Kartı OCR Uygulaması")
st.write("Yüklediğiniz kimlik fotoğrafını okuyarak T.C. Kimlik No, Soyad ve Ad bilgilerini çıkarır.")

uploaded_file = st.file_uploader("Lütfen bir kimlik fotoğrafı yükleyin", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    st.image(image, caption="Yüklenen Kimlik Fotoğrafı", use_column_width=True)

    result = ocr.ocr(img_array, cls=True)

    id_type = "unknown"
    for line in result[0]:
        text = line[1][0].upper()
        if "NUFUS" in text:
            id_type = "old"
            break
        elif "REPUBLIC" in text:
            id_type = "new"
            break

    if id_type == "old":
        try:
            tc_number = result[0][8][1][0]  # T.C. Number
            surname = result[0][10][1][0]  # Surname
            name = result[0][12][1][0]  # Name

            st.subheader("Kimlik Bilgileri (Eski Kimlik):")
            st.write(f"**T.C. Kimlik No:** {tc_number}")
            st.write(f"**Soyad:** {surname}")
            st.write(f"**Ad:** {name}")

        except IndexError:
            st.error("Beklenen veri formatı bulunamadı. Eski kimlik için OCR sonuçları eksik olabilir.")

    elif id_type == "new":
        try:
            tc_number = result[0][3][1][0]
            surname = result[0][5][1][0]
            name = result[0][7][1][0]

            st.subheader("Kimlik Bilgileri (Yeni Kimlik):")
            st.write(f"**T.C. Kimlik No:** {tc_number}")
            st.write(f"**Soyad:** {surname}")
            st.write(f"**Ad:** {name}")

        except IndexError:
            st.error("Beklenen veri formatı bulunamadı. Yeni kimlik için OCR sonuçları eksik olabilir.")

    else:
        st.warning("Kimlik türü belirlenemedi. 'NUFUS' veya 'REPUBLIC' anahtar kelimeleri bulunamadı .")

