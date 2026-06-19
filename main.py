import streamlit as st
from trip_plan_agent import TripTools
import json

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# ---------- HEADER ----------

st.markdown(
    """
    <h1 style='text-align:center;'>
    🌍 AI Multi-Agent Travel Planner
    </h1>
    <p style='text-align:center;font-size:18px'>
    Plan your dream trip using CrewAI Agents
    </p>
    """,
    unsafe_allow_html=True
)

# ---------- SIDEBAR ----------

with st.sidebar:

    st.header("✈️ Trip Preferences")

    travel_type = st.selectbox(
        "Travel Type",
        [
            "Adventure",
            "Luxury",
            "Family",
            "Backpacking",
            "Romantic",
            "Solo"
        ]
    )

    interests = st.multiselect(
        "Interests",
        [
            "Nature",
            "Food",
            "Culture",
            "Shopping",
            "Nightlife",
            "History",
            "Photography"
        ]
    )

    season = st.selectbox(
        "Season",
        ["Spring", "Summer", "Monsoon", "Autumn", "Winter"]
    )

    duration = st.slider(
        "Trip Duration (Days)",
        1,
        30,
        7
    )

    budget = st.selectbox(
        "Budget",
        [
            "Low",
            "Medium",
            "High",
            "Luxury"
        ]
    )

    generate = st.button(
        "🚀 Generate Travel Plan",
        use_container_width=True
    )

# ---------- MAIN ----------

if generate:

    inputs = {
        "travel_type": travel_type,
        "interests": ", ".join(interests),
        "season": season,
        "duration": duration,
        "budget": budget
    }

    with st.spinner("🤖 Agents are planning your trip..."):

        planner = TripTools(inputs)

        results = planner.run_trip_planner()

    st.success("Trip Generated Successfully!")

    # ---------------- TABS ----------------

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🏙 Cities",
            "📍 Research",
            "🗓 Itinerary",
            "💰 Budget"
        ]
    )

    with tab1:

        st.subheader("Recommended Cities")

        st.markdown(
            results.get(
                "city_selection",
                "No output available."
            )
        )

    with tab2:

        st.subheader("City Research")

        st.markdown(
            results.get(
                "city_research",
                "No output available."
            )
        )

    with tab3:

        st.subheader("Travel Itinerary")

        st.markdown(
            results.get(
                "itinerary_creation",
                "No output available."
            )
        )

    with tab4:

        st.subheader("Budget Plan")

        st.markdown(
            results.get(
                "budget_planning",
                "No output available."
            )
        )

    # ---------- DOWNLOAD ----------

    report = json.dumps(
        results,
        indent=4
    )

    st.download_button(
        label="📥 Download Travel Report",
        data=report,
        file_name="travel_plan.json",
        mime="application/json"
    )