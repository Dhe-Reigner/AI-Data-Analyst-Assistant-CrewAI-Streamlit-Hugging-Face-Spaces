# 🤖 AI Data Analyst Assistant

An intelligent **data analytics assistant** powered by **CrewAI**, **LangChain**, and **Streamlit**, capable of analyzing datasets, recommending visualizations, and summarizing business insights — all in one click.

---

## 🧩 Features

* 📊 **Descriptive Analytics:** Automatically summarizes your dataset with trends, correlations, and key metrics.
* 🎨 **Auto-Chart Recommendations:** Suggests chart types and axes based on the dataset structure (bar, line, scatter, boxplot, pie).
* 💼 **Business Insights:** Translates analytics into clear, actionable recommendations.
* 🧠 **AI Crew System:** Multi-agent collaboration using CrewAI (Data Analyst, Visualization Expert, Business Advisor).
* 🌐 **Deployable on Hugging Face Spaces.**

---

## 🚀 Quick Start

### 1️⃣ Clone this Repository

```bash
git clone https://github.com/<your-username>/ai-data-analyst-assistant.git
cd ai-data-analyst-assistant
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Keys

Create a `.env` file in the project root:

```
HUGGINGFACE_API_KEY=your_hf_api_key
JINA_API_KEY=your_jina_api_key
```

### 5️⃣ Run Locally

```bash
streamlit run src/crewaisdad/app.py
```

Then open `http://localhost:8501` in your browser.

---

## 🧠 Project Architecture

```
📦 ai-data-analyst-assistant
├── src/
│   ├── crewaisdad/
│   │   ├── app.py                # Streamlit dashboard
│   │   ├── crew.py               # CrewAI agents + tasks setup
│   │   ├── config.yaml           # YAML definition (roles + tasks)
│   └── utils/
├── requirements.txt
├── .env.example
├── README.md
└── LICENSE
```

---

## 🧑‍💻 Technologies Used

* **Streamlit** – Frontend dashboard
* **CrewAI** – Multi-agent orchestration
* **LangChain / Hugging Face** – LLM integration
* **Altair** – Chart visualization
* **Pandas** – Data manipulation
* **Python-dotenv** – Environment management

---

## 🧱 Example Workflow

1. Upload your dataset (CSV).
2. The AI crew analyzes the data.
3. It returns:

   * Descriptive statistics
   * Recommended charts (JSON format)
   * Business insights in Markdown
4. Streamlit visualizes it automatically.

---

## ☁️ Deployment on Hugging Face Spaces

1. Create a new Space:
   👉 [https://huggingface.co/spaces](https://huggingface.co/spaces) → *New Space* → choose **Streamlit**.

2. Upload your project files or connect your GitHub repo.

3. Add a **`requirements.txt`** file containing:

   ```
   streamlit
   pandas
   altair
   crewai
   langchain
   langchain_huggingface
   python-dotenv
   ```

   (Add others as needed)

4. Add a **`runtime.txt`** if you want to fix Python version:

   ```
   python-3.12
   ```

5. Add your Hugging Face and Jina API keys as **secrets**:

   * Go to the Space → Settings → Secrets → add:

     * `HUGGINGFACE_API_KEY`
     * `JINA_API_KEY`

6. Click **“Deploy”** — your Streamlit app will build and run automatically.

7. Share your Hugging Face Space URL!

---

## 📢 Roadmap / Future Improvements

* [ ] Add predictive analytics module
* [ ] Integrate data cleaning suggestions
* [ ] Enable chat-style conversation with the assistant
* [ ] Export results to PDF or Excel
* [ ] Allow multi-dataset comparison

---

## 📄 License

MIT License — feel free to fork, modify, and build upon this project!

---

## 🌟 Acknowledgements

Inspired by *“Clone Your Mind with AI”* and powered by **CrewAI**, this project showcases how intelligent multi-agent systems can assist with real-world data analysis.
