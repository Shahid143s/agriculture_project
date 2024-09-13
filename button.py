# HTML and CSS for styled button using st.markdown()
styled_button1_html = """
<div style="text-align: center;">
    <a target="_blank" href="https://crop-recommendation-sys.streamlit.app">
        <button class="button-24" role="button">Open Crop Recommendation System</button>
    </a>
</div>
<style>
.button-24 {
    background: #FF4742;
    border: 1px solid #FF4742;
    border-radius: 6px;
    box-shadow: rgba(0, 0, 0, 0.1) 1px 2px 4px;
    box-sizing: border-box;
    color: #FFFFFF;
    cursor: pointer;
    display: inline-block;
    font-family: Arial, sans-serif;
    font-size: 16px;
    font-weight: bold;
    line-height: 16px;
    min-height: 40px;
    outline: 0;
    padding: 12px 14px;
    text-align: center;
    text-rendering: geometricprecision;
    text-transform: none;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    vertical-align: middle;
}
.button-24:hover,
.button-24:active {
    background-color: initial;
    background-position: 0 0;
    color: #FF4742;
}
.button-24:active {
    opacity: .5;
}
</style>
"""
# HTML and CSS for styled button using st.markdown()
styled_button2_html = """
<div style="text-align: center;">
    <a target="_blank" href="https://huggingface.co/spaces/ShahidML/PlantDiseaseClassifier">
        <button class="button-24" role="button">Open Plant Disease Classifier</button>
    </a>
</div>
<style>
.button-24 {
    background: #FF4742;
    border: 1px solid #FF4742;
    border-radius: 6px;
    box-shadow: rgba(0, 0, 0, 0.1) 1px 2px 4px;
    box-sizing: border-box;
    color: #FFFFFF;
    cursor: pointer;
    display: inline-block;
    font-family: Arial, sans-serif;
    font-size: 16px;
    font-weight: bold;
    line-height: 16px;
    min-height: 40px;
    outline: 0;
    padding: 12px 14px;
    text-align: center;
    text-rendering: geometricprecision;
    text-transform: none;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    vertical-align: middle;
}
.button-24:hover,
.button-24:active {
    background-color: initial;
    background-position: 0 0;
    color: #FF4742;
}
.button-24:active {
    opacity: .5;
}
</style>
"""
styled_container_css = """
<style>
.bordered-container {
    border: 2px solid #FF4742;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
}
</style>
"""

css = """
<style>
.bordered-container {
  border: 2px solid #FF4742;
  text-align: center;
}
</style>
"""
#-----------------
css2 = """
<style>
.bordered-container2 {
  border: 2px solid #FF4742;
  text-align: center;
}

.circle-bordered-container2 {
  border: 2px solid #FF4742;
  border-radius: 50%;
  text-align: center;
  display: inline-block;
  overflow: hidden;
  width: 50px; /* Adjust size to 1/4th of original */
  height: 50px; /* Adjust size to 1/4th of original */
  margin: auto; /* Center the circle container */
}
.circle-bordered-container2 img {
  width: 100%;
  height: auto;
}
</style>
"""
