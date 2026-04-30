import streamlit as st
import json
import os
from scores import save_score
from questions import load_questions

st.set_page_config(
    page_title="Quiz Master",
    page_icon="🌞",
    layout="centered"
)

st.title("🌞 Quiz Master")


if "questions" not in st.session_state:
    st.session_state.questions = load_questions()

    
    if not st.session_state.questions:
        st.error("❌ Nu s-au putut încărca întrebările din API.")
        st.stop()

    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.feedback = None
    st.session_state.finished = False


menu = st.sidebar.selectbox("Meniu", ["Start Quiz", "Vezi scoruri"])


if menu == "Start Quiz":

    name = st.text_input("🧚‍♀️ Introdu numele tău")

    if name:

        progress = st.session_state.current / len(st.session_state.questions)
        st.progress(progress)
        st.caption(f"Progres: {st.session_state.current}/{len(st.session_state.questions)}")

        if not st.session_state.finished:

            q = st.session_state.questions[st.session_state.current]

            st.markdown(f"## 🎀 Întrebarea {st.session_state.current + 1}")

            st.markdown(f"""
            <div style="
                padding: 15px;
                border-radius: 12px;
                background-color: #dd4283;
                color: black;
                font-size: 18px;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
            ">
            {q['question']}
            </div>
            """, unsafe_allow_html=True)

            answer = st.radio(
                "Alege răspunsul:",
                q["options"],
                key=f"q_{st.session_state.current}"
            )

           
            if st.button("✔ Confirmă răspunsul"):

                selected_letter = answer.split(".")[0]

                if selected_letter == q["answer"]:
                    st.session_state.score += 1
                    st.session_state.feedback = "corect"
                else:
                    st.session_state.feedback = "gresit"

            
            if st.session_state.feedback:

                if st.session_state.feedback == "corect":

                    st.markdown("""
                    <div style="
                        padding: 12px;
                        border-radius: 10px;
                        background-color: #dd4283;
                        color: black;
                        font-size: 16px;
                    ">
                    🎉 Corect!
                    </div>
                    """, unsafe_allow_html=True)

                else:

                    st.markdown(f"""
                    <div style="
                        padding: 12px;
                        border-radius: 10px;
                        background-color: #dd4283;
                        color: black;
                        font-size: 16px;
                    ">
                    ❌ Greșit! Răspuns corect: <b>{q['answer']}</b>
                    </div>
                    """, unsafe_allow_html=True)

                if st.button("🌷 Următoarea întrebare"):

                    st.session_state.current += 1
                    st.session_state.feedback = None

                    if st.session_state.current >= len(st.session_state.questions):
                        st.session_state.finished = True

                    st.rerun()

        else:
            st.markdown(f"""
            <div style="
                padding: 15px;
                border-radius: 12px;
                background-color: #dd4283;
                color: black;
                font-size: 20px;
                font-weight: bold;
                text-align: center;
            ">
            💅 Gata, {name}!
            </div>
            """, unsafe_allow_html=True)

            st.markdown(
                f"### Scor final: **{st.session_state.score}/{len(st.session_state.questions)}**"
            )

            save_score(name, st.session_state.score)

            if st.button("💋 Restart quiz"):
                st.session_state.clear()
                st.rerun()


elif menu == "Vezi scoruri":

    st.subheader("👑 Leaderboard")

    if os.path.exists("scores.json"):
        with open("scores.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        data.sort(key=lambda x: x["score"], reverse=True)

        for i, entry in enumerate(data[:10], start=1):
            st.write(f"**{i}. {entry['name']}** — {entry['score']} puncte")
    else:
        st.info("Nu există scoruri încă.")