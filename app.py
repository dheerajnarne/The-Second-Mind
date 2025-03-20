import sys
import os
from huggingface_hub import login

import sys
import os

# Add the 'agents' folder to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'agents'))

from agents.supervisor_agent import SupervisorAgent
import streamlit as st

# Initialize the supervisor agent
supervisor = SupervisorAgent()

# Streamlit app
st.title("Research Idea Generation and Evolution")

# Input query
query = st.text_input("Enter your research query:")

# Button to start the loop
if st.button("Generate and Evolve Idea"):
    if query:
        # Initialize loop variables
        current_query = query
        for i in range(3):  # Loop 3 times for demonstration
            st.write(f"### Iteration {i+1}")
            
            # Fetch web data
            web_data = supervisor.fetch_web_data(current_query)
            st.write("**Web Data:**")
            for item in web_data:
                st.write(f"- **{item['title']}**: {item['summary']}")
            
            # Generate idea
            idea = supervisor.generation_agent.generate_idea(current_query, web_data)
            st.write("**Generated Idea:**")
            st.write(idea)
            
            # Reflect on the idea
            reflection = supervisor.reflection_agent.reflect(idea, web_data)
            st.write("**Reflection:**")
            st.write(reflection)
            
            # Rank the idea
            ranking_feedback = supervisor.ranking_agent.rank(idea, web_data)
            st.write("**Ranking Feedback:**")
            st.write(ranking_feedback)
            
            # Evolve the idea
            evolved_idea = supervisor.evolution_agent.evolve(idea, ranking_feedback, web_data)
            st.write("**Evolved Idea:**")
            st.write(evolved_idea)
            
            # Link to past interactions
            proximity_feedback = supervisor.proximity_agent.link_to_past(current_query, evolved_idea)
            st.write("**Proximity Feedback:**")
            st.write(proximity_feedback)
            
            # Meta-review the process
            meta_review = supervisor.meta_review_agent.review_process("\n".join(supervisor.process_log))
            st.write("**Meta-review:**")
            st.write(meta_review)
            
            # Update current query for next iteration
            current_query = evolved_idea
            
            # Add to memory
            supervisor.memory_agent.add_to_memory(current_query, evolved_idea)
            
            st.write("---")
    else:
        st.write("Please enter a query to start the process.")