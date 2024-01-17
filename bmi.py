import streamlit as st
from PIL import Image

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

# Streamlit App
def main():
    st.title("BMI Calculator")

    # User input for height and weight
    height = st.slider("Height (cm)", 0, 220, 170, 1)
    weight = st.slider("Weight (kg)", 0, 200, 70, 1)

    # Calculate BMI and interpret result
    bmi_result = calculate_bmi(height, weight)
    interpretation, advice = interpret_bmi(bmi_result)

    # Display BMI result
    st.subheader("BMI Result:")
    st.info(f"Your BMI: {bmi_result}")
    st.success(f"Interpretation: {interpretation}")
    st.text(advice)

    # Show image with styling
    image_path = "man.png"
    img = Image.open(image_path)
    aspect_ratio = img.width / img.height
    new_width = int(height * aspect_ratio)
    resized_img = img.resize((new_width, height))

    # Additional styling for the resized image
    st.image(resized_img, caption="Resized Image", use_column_width=True, output_format="PNG", channels="RGBA")

if __name__ == "__main__":
    main()
