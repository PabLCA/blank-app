import streamlit as st
import plotly.graph_objects as go


st.set_page_config(page_title="Salario ", layout="centered")

st.markdown(
    """
    <style>
    body {
        background: radial-gradient(circle at top left, rgba(44, 152, 255, 0.16), transparent 40%),
                    radial-gradient(circle at bottom right, rgba(72, 66, 255, 0.13), transparent 35%),
                    linear-gradient(180deg, #02061d 0%, #091436 100%);
    }

    [data-testid="stApp"] {
        animation: fadeInUp 0.9s ease both;
        min-height: 100vh;
        color: #e8f0ff;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(24px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .hero-card {
        border-radius: 26px;
        padding: 24px;
        margin-bottom: 24px;
        background: linear-gradient(135deg, rgba(14, 93, 194, 0.95), rgba(18, 52, 102, 0.92));
        box-shadow: 0 30px 80px rgba(0, 0, 0, 0.22);
        color: #ffffff;
    }

    .hero-card h1 {
        margin: 0 0 8px 0;
        font-size: 2.4rem;
    }

    .hero-card p {
        margin: 0;
        color: #d8e3ff;
        font-size: 1rem;
    }

    .section-card {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.14);
        border-radius: 22px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
        backdrop-filter: blur(12px);
    }

    .stSelectbox, .stRadio, .stToggle {
        animation: fadeInUp 0.7s ease both;
    }
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <h1>💰 Salario </h1>
        <p>Elige tu perfil .</p>
        <p style="margin-top:12px; font-size:0.95rem; color:#c8d4ff;">

        
    </div>
    """,
    unsafe_allow_html=True,
)


data = {
    'Ingeniería de Sistemas': {'Junior (0-2 años)': 3500000, 'Mid-Senior (2-5 años)': 7000000, 'Senior (5+ años)': 14000000},
    'Ciencia de Datos': {'Junior (0-2 años)': 4000000, 'Mid-Senior (2-5 años)': 7400000, 'Senior (5+ años)': 16500000},
    'Ambas': {'Junior (0-2 años)': 5500000, 'Mid-Senior (2-5 años)': 10250000, 'Senior (5+ años)': 19500000}
}


rol_seleccionado = st.selectbox("1. Selecciona el Rol Profesional:", list(data.keys()))

col1, col2 = st.columns(2)
with col1:
    ingles_remoto = st.toggle("🌐 Trabajo Remoto Internacional")
with col2:
    moneda = st.radio("2. Selecciona la Moneda:", ["COP (Pesos)", "USD (Dólares)"], horizontal=True)

# --- MATEMÁTICA Y CÁLCULOS ---
niveles = list(data[rol_seleccionado].keys())
salarios_base = list(data[rol_seleccionado].values())

multiplicador_remoto = 1.8 if ingles_remoto else 1.0
tasa_cambio = 4000  # 1 USD = 4,000 COP aprox.

salarios_finales = []
for salario in salarios_base:
    total_cop = salario * multiplicador_remoto
    if "USD" in moneda:
        salarios_finales.append(int(total_cop / tasa_cambio))
    else:
        salarios_finales.append(int(total_cop))

# --- GRÁFICA ---
simbolo = "USD" if "USD" in moneda else "COP"

fig = go.Figure(go.Bar(
    x=niveles,
    y=salarios_finales,
    marker_color='#2ca02c' if "USD" in moneda else '#1f77b4',
    text=[f"${val:,.0f} {simbolo}" for val in salarios_finales],
    textposition='auto',
    marker_line_color='rgba(255, 255, 255, 0.18)',
    marker_line_width=1.5,
))

fig.update_layout(
    title=f"Estimación para: {rol_seleccionado}",
    yaxis_title=f"Salario Mensual ({simbolo})",
    template="plotly_dark",
    height=470,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='#f1f7ff',
    transition={'duration': 600, 'easing': 'cubic-in-out'},
)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
