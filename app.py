import streamlit as st

# ------------------------
# Fonctions d'interprétation
# ------------------------

def interpret_domain_score(value):
    if value < 30:
        return "🔴 Faible autorité de domaine. Travaille ta notoriété et les mentions de marque."
    elif value < 70:
        return "🟡 Autorité moyenne. Bonne base, mais des efforts sont encore nécessaires pour s'imposer."
    else:
        return "🟢 Forte autorité. Protège cette position par des contenus experts et des backlinks réguliers."

def interpret_traffic(value):
    if value < 1000:
        return "🔴 Trafic organique faible. Il est temps d’investir dans un contenu SEO plus ciblé."
    elif value < 10000:
        return "🟡 Trafic organique modéré. Potentiel en développement. Amplifie ce qui fonctionne."
    else:
        return "🟢 Excellent trafic. Pense à améliorer la conversion et à capitaliser sur tes pages fortes."

def interpret_backlinks(value):
    if value < 100:
        return "🔴 Très peu de backlinks. Ton autorité perçue est faible. Lance une campagne de netlinking."
    elif value < 1000:
        return "🟡 Backlinks raisonnables. Vise maintenant la qualité des domaines référents."
    else:
        return "🟢 Bon profil de backlinks. Continue à varier les sources pour éviter la saturation."

# ------------------------
# Interface Streamlit
# ------------------------

st.set_page_config(page_title="Décodeur SEMrush", layout="centered")
st.title("🔍 Interpréteur simplifié de scores SEMrush")

st.markdown("Entre les 3 principales métriques SEMrush pour obtenir une lecture stratégique directe.")

# Inputs
domain_score = st.slider("🏆 Autorité du domaine (0-100)", 0, 100, 50)
traffic = st.number_input("🌐 Trafic organique mensuel estimé", min_value=0, step=100)
backlinks = st.number_input("🔗 Nombre total de backlinks", min_value=0, step=10)

# Analyse
if st.button("🧠 Interpréter"):
    st.subheader("🧩 Résultats de l'analyse stratégique")

    st.markdown(f"**Autorité de domaine :** {interpret_domain_score(domain_score)}")
    st.markdown(f"**Trafic organique :** {interpret_traffic(traffic)}")
    st.markdown(f"**Backlinks :** {interpret_backlinks(backlinks)}")
