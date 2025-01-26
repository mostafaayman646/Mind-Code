# **Mind Code: Early Diagnosis of Alzheimer’s Using PDEs and Machine Learning**

## **Overview**  
Mind Code is a research project focused on advancing the early diagnosis of **Alzheimer’s disease** by integrating **partial differential equations (PDEs)**, **Physics-Informed Neural Networks (PINNs)**, and **symbolic regression**. This project explores tau protein diffusion in the brain, aiming to predict the reaction term in the reaction-diffusion PDE that governs its behavior.

Through this interdisciplinary approach, we aim to contribute to **healthcare innovation** by providing tools for better understanding Alzheimer’s progression and enhancing diagnostic precision.

---

## **Features**
- 🧠 **Tau Protein Diffusion Modeling**: Simulated tau protein spread in the brain using the reaction-diffusion PDE.  
- 🤖 **Physics-Informed Neural Networks (PINNs)**: Combined physics and data to predict the reaction term in the PDE.  
- 🔬 **Symbolic Regression**: Discovered interpretable mathematical expressions for the reaction term.  
- 📊 **Visualization**: Simulated and visualized tau protein diffusion patterns in a 2D brain-like geometry.  
- 🛠️ **Web Interface**: Dynamic webpage to interactively present diffusion results and project insights.  
- 🧪 **Data Integration**: Used synthetic training data and PET scan data from the **ADNI** database for parameter extraction.  

---

## **Repository Structure**
```
Mind-Code/
├── data/                 # Synthetic and real PET scan data
├── notebooks/            # Jupyter notebooks for data preprocessing and training
├── models/               # PINN and symbolic regression models
├── simulations/          # COMSOL simulation files for tau protein diffusion
├── web_interface/        # Code for the dynamic webpage visualization
├── results/              # Generated images, graphs, and diffusion patterns
├── README.md             # Project description and instructions
└── LICENSE               # License for the repository
```

---

## **How It Works**
### 1. **Preprocessing**
- **PET Scan Denoising**: Applied the **heat equation** to denoise PET scans before classification.
- **Synthetic Data Generation**: Created synthetic data for training using four different reaction equations.

### 2. **Training and Prediction**
- Trained **PINNs** to predict the unknown reaction term in the reaction-diffusion PDE.
- Used **symbolic regression** to derive interpretable reaction equations.

### 3. **Simulation**
- Simulated tau protein diffusion in a 2D brain-like shape using **COMSOL**.
- Applied the predicted reaction term to visualize diffusion patterns.

### 4. **Visualization**
- Developed an interactive webpage to dynamically present results and insights.

---

## **Getting Started**
### Prerequisites
- Python 3.8+
- COMSOL Multiphysics (for simulations)
- Jupyter Notebook

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mind-code.git
   cd mind-code
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter notebooks:
   ```bash
   jupyter notebook
   ```

4. View the dynamic webpage:
   ```bash
   cd web_interface
   python -m http.server
   ```

---

## **Results**
### Key Highlights
- Discovered reaction terms that match synthetic ground truth equations with high accuracy.
- Demonstrated diffusion patterns of tau protein in a 2D brain model.
- Improved PET scan quality using the heat equation for denoising.

### Visualizations
![Tau Diffusion](results/tau_diffusion.png)  
*Figure: Tau protein diffusion patterns in a 2D brain-like shape.*

---

## **Future Work**
- Extend the model to simulate 3D brain geometries.
- Test on additional real-world PET datasets.
- Explore the application of PINNs for other neurodegenerative diseases.

---

## **Contributors**
- **Your Name** ([LinkedIn](https://linkedin.com/in/your-profile)) – Project Lead
- **Team Members (if applicable)**  

---

## **Acknowledgments**
- **ADNI** for providing PET scan data.  
- **COMSOL** for simulation tools.  
- Inspiration from [Paper Name/Authors] (add a link if applicable).  

---

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Contact**
Feel free to reach out for collaboration or questions:  
📧 Email: your.email@example.com  
