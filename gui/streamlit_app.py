# === IMPORTS ===
import streamlit as st  # Web UI framework
import pandas as pd  # Data processing
import matplotlib.pyplot as plt  # Basic charting
import seaborn as sns  # Modern plotting
import time  # Timer for performance tracking
import base64  # For download functionality
import os, sys  # File path & system utilities
import nltk  # Natural Language Toolkit for stopwords
from nltk.corpus import stopwords  # Stopwords list

# === INITIAL SETUP ===
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

st.set_page_config(page_title="MapReduce Word Count", layout="wide")  # App layout config

# === PAGE STYLING ===
st.markdown("""
    <style>
        .stApp {
            background-color: #2C1A1A;
            color: #FDF6E3;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #E74C3C;
        }
        section[data-testid="stSidebar"] {
            background-color: #3D2C2C;
        }
        .stFileUploader, .stTextArea {
            background-color: #3D2C2C !important;
            color: #FDF6E3;
        }
    </style>
""", unsafe_allow_html=True)

# === PATHS FOR CUSTOM MODULES ===
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.mapper import WordCountMapper
from src.reducer import WordCountReducer

# === SESSION STATE INIT ===
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()
if "times" not in st.session_state:
    st.session_state.times = []

# === NAVIGATION ===
page = st.sidebar.selectbox("📑 Navigate", [
    "📥 Input", "📋 Word Table", "📊 Charts", "📤 Download"
])

# === PAGE: INPUT ===
if page == "📥 Input":
    st.title("📥 Upload or Enter Text")
    st.write("Use this page to upload .txt files or paste your text. The MapReduce process will count the frequency of words.")

    uploaded_files = st.file_uploader("Upload .txt file(s)", type=["txt"], accept_multiple_files=True)
    manual_text = st.text_area("Or paste your text here:", height=150)

    text_lines = []
    if uploaded_files:
        for f in uploaded_files:
            text = f.read().decode("utf-8")
            text_lines.extend(text.splitlines())
    elif manual_text.strip():
        text_lines = manual_text.strip().splitlines()

    if text_lines and st.button("🚀 Run MapReduce"):
        start_time = time.time()

        # MapReduce pipeline
        mapper = WordCountMapper()
        reducer = WordCountReducer()
        mapped = [pair for line in text_lines for pair in mapper.map(line)]
        grouped = reducer.shuffle_and_sort(mapped)
        reduced = reducer.reduce(grouped)

        # Filter out stopwords
        reduced = {w: c for w, c in reduced.items() if w.lower() not in stop_words}

        df = pd.DataFrame(list(reduced.items()), columns=["Word", "Frequency"]).sort_values(by="Frequency", ascending=False)
        st.session_state.df = df

        elapsed_time = round(time.time() - start_time, 4)
        st.session_state.times.append(elapsed_time)
        st.success(f"✅ Processed in {elapsed_time} seconds! Use the sidebar to view results.")

# === PAGE: WORD TABLE ===
elif page == "📋 Word Table":
    st.title("📋 Word Frequency Table")

    if not st.session_state.df.empty:
        search_query = st.text_input("🔍 Search for a word")

        filtered_df = st.session_state.df[
            st.session_state.df["Word"].str.contains(search_query, case=False, na=False)
        ] if search_query else st.session_state.df

        st.markdown("""
            <style>
                .custom-table {
                    background-color: #2C1A1A;
                    border-collapse: collapse;
                    width: 100%;
                    font-family: 'Segoe UI', sans-serif;
                    font-size: 14px;
                    color: #FDF6E3;
                }
                .custom-table th {
                    background-color: #B03A2E;
                    color: #fff;
                    padding: 12px 15px;
                    text-align: center;
                    border: 1px solid #A93226;
                }
                .custom-table td {
                    background-color: #3D2C2C;
                    padding: 10px;
                    text-align: center;
                    border: 1px solid #5D4037;
                }
                .custom-table tr:hover td {
                    background-color: #6E2C00;
                }
            </style>
        """, unsafe_allow_html=True)

        table_html = filtered_df.to_html(classes='custom-table', index=False, escape=False)
        st.markdown(table_html, unsafe_allow_html=True)
    else:
        st.warning("⚠️ No data available. Please go to the Input page and run the MapReduce process first.")

# === PAGE: CHARTS ===
elif page == "📊 Charts":
    st.title("📊 Visual Charts")

    if not st.session_state.df.empty:
        df = st.session_state.df
        top10 = df.head(10)

        # Bar Chart
        fig1, ax1 = plt.subplots(figsize=(10, 5))
        sns.barplot(data=top10, x="Word", y="Frequency", palette="Reds", ax=ax1)
        ax1.set_title("Top 10 Most Frequent Words - Bar Chart")
        st.pyplot(fig1)

        # Pie Chart
        fig2, ax2 = plt.subplots()
        ax2.pie(top10["Frequency"], labels=top10["Word"], autopct="%1.1f%%", startangle=140, colors=sns.color_palette("Reds", n_colors=10))
        ax2.axis("equal")
        st.pyplot(fig2)

        # Horizontal Bar Chart
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        sns.barplot(data=top10, y="Word", x="Frequency", palette="Reds", ax=ax3)
        ax3.set_title("Top 10 Most Frequent Words - Horizontal Bar")
        st.pyplot(fig3)

        # Execution Time Line Chart
        if st.session_state.times:
            st.subheader("⏱️ Execution Time per Run")
            time_df = pd.DataFrame({
                "Run": list(range(1, len(st.session_state.times) + 1)),
                "Execution Time": st.session_state.times
            })
            fig4, ax4 = plt.subplots()
            sns.lineplot(data=time_df, x="Run", y="Execution Time", marker="o", color="#FF5733", ax=ax4)
            ax4.set_title("Execution Time by Run")
            st.pyplot(fig4)
    else:
        st.warning("⚠️ No data available. Please run the MapReduce process first.")

# === PAGE: DOWNLOAD ===
elif page == "📤 Download":
    st.title("📤 Export Results")

    if not st.session_state.df.empty:
        csv_data = st.session_state.df.to_csv(index=False)
        b64 = base64.b64encode(csv_data.encode()).decode()

        download_link = f'''
        <a href="data:file/csv;base64,{b64}" download="word_frequencies.csv"
           style="font-size:18px; color:#FDF6E3; background:#117864;
                  padding:10px 20px; border-radius:5px; text-decoration:none;">
           📄 Click to Download CSV
        </a>'''

        st.markdown("### Your data is ready! 🎉")
        st.markdown("Use the button below to download your results as a CSV file.")
        st.markdown(download_link, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("Sample Preview")
        st.dataframe(st.session_state.df.head(10))
    else:
        st.warning("⚠️ No data available for download. Please run the MapReduce process first.")
