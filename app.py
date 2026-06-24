# mpls.hassan
import streamlit as st

from chart import build_chart
from sentiment import analyze_sentiments, get_sentences

# page config
st.set_page_config(page_title="sentimental", layout="centered")

st.markdown(
    """
<style>
  @import url('https://cdn.jsdelivr.net/gh/vincentdoerig/latex-css@1.10.0/fonts/fonts.css');

  html, body, [class*="css"] {
    font-family: 'Latin Modern Roman', 'Computer Modern', Georgia, serif;
  }

  h1 {
    font-family: 'Latin Modern Roman', 'Computer Modern', Georgia, serif !important;
    font-size: 2.4rem !important;
    letter-spacing: 0.05em;
    margin-bottom: 0.1rem !important;
  }

  .subtitle {
    font-family: 'Latin Modern Roman', serif;
    font-size: 0.85rem;
    color: #888;
    letter-spacing: 0.04em;
    margin-bottom: 2rem;
  }

  .section-label {
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    color: #888;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
    font-family: 'Latin Modern Roman', serif;
  }

  /* inputs stay courier for typewriter feel */
  textarea, input[type="text"] {
    font-family: 'Courier Prime', 'Courier New', monospace !important;
    font-size: 0.95rem !important;
    border-radius: 2px !important;
  }

  .sentence-pill {
    display: inline-block;
    border-radius: 2px;
    padding: 0.3rem 0.7rem;
    margin: 0.2rem 0;
    font-size: 0.85rem;
    font-family: 'Courier Prime', 'Courier New', monospace;
    width: 100%;
    border: 1px solid rgba(128,128,128,0.2);
  }

  hr {
    margin: 1.8rem 0 !important;
  }

  .stButton > button {
    font-family: 'Latin Modern Roman', serif !important;
    border-radius: 2px !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.05em;
  }

  #MainMenu, footer, { visibility: hidden; }
  .block-container { padding-top: 2.5rem !important; }
</style>
""",
    unsafe_allow_html=True,
)

# state
if "manual_sentences" not in st.session_state:
    st.session_state.manual_sentences = []

# ui
st.markdown("<h1>sentimental</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>feel the emotions rise and fall</div>",
    unsafe_allow_html=True,
)

# free-text mode
st.markdown("<div class='section-label'>type freely:</div>", unsafe_allow_html=True)
free_text = st.text_area(
    label="free_text",
    placeholder="type or paste anything.",
    height=130,
    label_visibility="collapsed",
    key="free_text_input",
)

free_sentences = get_sentences(free_text) if free_text.strip() else []

st.markdown("<hr>", unsafe_allow_html=True)

# sentence-by-sentence mode
st.markdown(
    "<div class='section-label'> type sentence-by-sentence:</div>",
    unsafe_allow_html=True,
)

col1, col2 = st.columns([5, 1])
with col1:
    manual_input = st.text_input(
        label="manual_input",
        placeholder="type a sentence and hit add →",
        label_visibility="collapsed",
        key="manual_input",
    )
with col2:
    add_clicked = st.button("add", use_container_width=True)

if add_clicked and manual_input.strip():
    st.session_state.manual_sentences.append(manual_input.strip())
    st.rerun()

# render existing manual sentences with remove buttons
for i, s in enumerate(st.session_state.manual_sentences):
    c1, c2 = st.columns([6, 1])
    with c1:
        st.markdown(f"<div class='sentence-pill'>{s}</div>", unsafe_allow_html=True)
    with c2:
        if st.button("✕", key=f"remove_{i}"):
            st.session_state.manual_sentences.pop(i)
            st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)

# chart
all_sentences = free_sentences + st.session_state.manual_sentences

if all_sentences:
    scores_data = analyze_sentiments(all_sentences)
    compound_scores = [s["compound"] for s in scores_data]

    st.plotly_chart(
        build_chart(all_sentences, compound_scores), use_container_width=True
    )
else:
    st.markdown(
        "<div style='font-size:0.85rem; text-align:center; padding: 3rem 0; opacity: 0.3;'>created with <span style='color:#eb5757;'>love</span> by mustafa hassan</div>",
        unsafe_allow_html=True,
    )
