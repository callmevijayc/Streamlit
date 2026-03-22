import streamlit as st
st.title("File Upload") ## This line sets the title of the app
st.write("This app demonstrates the file uploader widget in Streamlit.") ## This line writes a message to the app


file = st.file_uploader("Upload a file", type=["txt", "pdf", "jpg", "png","docx"]) ## This line creates a file uploader widget for the user to upload a file
if file is not None: ## This line checks if a file has been uploaded
    st.write("File uploaded successfully!") ## This line writes a success message to the app
    st.write(f"File name: {file.name}") ## This line displays the name of the uploaded file
    st.write(f"File type: {file.type}") ## This line displays the type of the uploaded file
    st.write(f"File size: {file.size} bytes") ## This line displays the size of the uploaded file in bytes  

    if file.name.endswith("jpg") or file.name.endswith("png"): ## This line checks if the uploaded file is an image
        st.image(file) ## This line displays the uploaded image in the app
    if file.name.endswith("pdf") or file.name.endswith("docx"): ## This line checks if the uploaded file is a PDF or Word document
     st.write("Preview not available for this file type.") ## This line writes a message indicating that a preview is not available for this file type
     st.write("You can download the file to view its content.") ## This line writes a message suggesting the user to download the file to view its content
     st.download_button("Download File", file, file.name) ## This line creates a download button for the uploaded file
    if file.name.endswith("txt"):
        content = file.read() ## This line reads the content of the uploaded file
        st.write("File content:") ## This line writes a message to the app
        st.text(content) ## This line displays the content of the uploaded file as text
