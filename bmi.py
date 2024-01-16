import streamlit as st
from PIL import Image
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🧍‍♂️",
    layout="wide",
)

# Function to calculate BMI
def calculate_bmi(height, weight):
    m = height / 100
    bmi = round(weight / m ** 2, 1)
    return bmi

# Function to interpret BMI result
def interpret_bmi(bmi):
    if bmi <= 18.5:
        return "Underweight!", "Your body weight is lower than normal."
    elif 18.5 < bmi <= 25:
        return "Normal.", "Congratulations! Your body weight is normal."
    elif 25 < bmi <= 30:
        return "Overweight!", "Your body weight is slightly above normal."
    else:
        return "Obese!", "Your health is at risk. You should visit a doctor."

# Function to resize image dynamically
def resize_image(img, height):
    img_np = np.array(img)
    resized_img = Image.fromarray(img_np)
    aspect_ratio = img.width / img.height
    new_width = int(height * aspect_ratio)
    resized_img = resized_img.resize((new_width, height))
    return resized_img

# Streamlit App
def main():
    st.title("BMI Calculator")

    # Sidebar with image
    st.sidebar.image("icon.png", width=100)

    # Load original image
    man_img = Image.open("man.png")

    # User input for height and weight
    height = st.sidebar.slider("Height (cm)", 0, 220, 170, 1)
    weight = st.sidebar.slider("Weight (kg)", 0, 200, 70, 1)

    # Resize image dynamically based on height
    resized_man_img = resize_image(man_img, height)

    # Display resized image
    st.sidebar.image(resized_man_img, caption="Resized Image", use_column_width=True)

    # Calculate BMI and interpret result
    bmi_result = calculate_bmi(height, weight)
    interpretation, advice = interpret_bmi(bmi_result)

    # Display BMI result
    st.subheader("BMI Result:")
    st.info(f"Your BMI: {bmi_result}")
    st.success(f"Interpretation: {interpretation}")
    st.text(advice)

if __name__ == "__main__":
    main()
