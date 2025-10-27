import streamlit as st
import pandas as pd
import altair as alt
import re
#from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace
import os
from dotenv import load_dotenv
from crew import CrewaiSdad



load_dotenv()

#os.getenv('HUGGINGFACE_API_KEY')
#os.environ['GEMINI_API_KEY']
os.getenv('JINA_API_KEY')

def main():
    #Set page
    st.set_page_config(page_title="AI-Powered Data Insights",page_icon='📊',layout='wide')
    st.title("🤖AI-Powered Descriptive Analytics Dashboard")

    #Upload Dataset
    user_csv = st.file_uploader("Upload file here",type='csv')
    if not user_csv:
        st.info('Please upload a dataset to get started')
        st.stop()

    df = pd.read_csv(user_csv)
    st.dataframe(df,width='stretch')

    # Sample data for the LLM
    sample_data = df.head(50).to_csv(index=False)

    # Run Crew
    if st.button('Run AI Analytics Crew'):
        with st.spinner("The AI Crew is analyzing your data..."):
            results = CrewaiSdad().crew().kickoff(inputs={'sample_data':sample_data})

            # ✅ Extract actual text output
            if hasattr(results, "text"):
                output_text = results.text
            elif hasattr(results, "raw_output"):
                output_text = results.raw_output
            else:
                output_text = str(results)
                
            st.success("✅Crew Completed Analysis!")

            # Extract results
            # analysis_text = results.tasks_output[0]
            # viz_text = results.tasks_output[1]
            # business_text = results.tasks_output[2]

            analysis_text = output_text
            viz_text = output_text
            business_text = output_text

            st.markdown("### 📊Analytical Summary")
            st.markdown(analysis_text)

            # st.markdown("### 💼Business Insights")
            # st.markdown(business_text)

            # ============ 🔍Parse Visualization Recommendations ==========

            st.markdown('### 📈 Auto-Generated Visualizations')
            try:
                # Extract JSON-like text using regex
                json_like = re.search(r'\[.*\]',viz_text,re.S)
                if json_like:
                    import json
                    charts = json.loads(json_like.group(0))
                    for i, chart in enumerate(charts, 1):
                        ctype = chart.get('type','').lower()
                        x = chart.get('x')
                        y = chart.get('y')

                        if x not in df.columns or y not in df.columns:
                            st.warning(f'Skipping chart {i}: columns {x},{y} not found.')
                            continue
                        st.subheader(f"Chat {i}: {ctype.title()} - {x} vs {y}")

                        if ctype == 'bar':
                            c = alt.Chart(df).mark_bar().encode(x=x,y=y)

                        elif ctype  == 'line':
                            c = alt.Chart(df).mark_line().encode(x=x,y=y)

                        elif ctype == 'scatter':
                            c = alt.Chart(df).mark_circle().encode(x=x,y=y)

                        elif ctype == 'boxplot':
                            c = alt.Chart(df).mark_boxplot().encode(x=x,y=y)

                        elif ctype == 'pie':
                            c = alt.Chart(df).mark_arc().encode(theta=y, color=x)

                        else:
                            st.warning(f"Unkown chart type:{ctype}")
                            continue
                        
                        st.altair_chart(c,use_container_width=True)

                    else:
                        st.warning("No chart recommendations were returned by the AI")

            except Exception as e:
                st.error(f"⚠️Error parsing or rendering charts: {e}")



    #Initiate LLM

if __name__=="__main__":
    main()