import streamlit as st
from rdkit import Chem

# Set up page configurations
st.set_page_config(
    page_title="Eribulin Chiral Center Calculator",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f7fbff;
    }
    .title {
        color: #1f77b4;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .footer {
        text-align: center;
        color: #7f8c8d;
        font-size: 14px;
        margin-top: 50px;
    }
    .result-box {
        background-color: #e8f4f8;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1 class='title'>Eribulin Chiral Center Calculator</h1>", unsafe_allow_html=True)
st.write("---")

# Default Eribulin SMILES
eribulin_smiles = "C[C@@H]1C[C@@H]2CC[C@H]3C(=C)C[C@@H](O3)CC[C@]45C[C@@H]6[C@H](O4)[C@H]7[C@@H](O6)[C@@H](O7)CC[C@H]5[C@@H](C)O2"

# Input configuration
smiles_input = st.text_input("Enter a SMILES string below:", value=eribulin_smiles)

# Calculation logic
if st.button("Calculate Chiral Centers", type="primary"):
    if not smiles_input.strip():
        st.warning("Please enter a valid SMILES string.")
    else:
        # Convert SMILES to RDKit Molecule object
        mol = Chem.MolFromSmiles(smiles_input)
        
        if mol is None:
            # Handle invalid SMILES
            st.error("Invalid SMILES string. Ensure the structure is correct.")
        else:
            # Find chiral centers using RDKit
            chiral_centers = Chem.FindMolChiralCenters(mol, includeUnassigned=True)
            num_centers = len(chiral_centers)
            
            # Display results
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.success(f"**Number of Chiral Centers: {num_centers}**")
            
            if num_centers > 0:
                st.write("**List of Chiral Centers (Atom Index, Stereochemistry):**")
                
                # Format chiral centers cleanly
                center_data = [{"Atom Index": index, "Stereochemistry": stereo} for index, stereo in chiral_centers]
                st.table(center_data)
            else:
                st.info("No chiral centers found in this molecule.")
                
            st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Developed for Chemistry Project</div>", unsafe_allow_html=True)
