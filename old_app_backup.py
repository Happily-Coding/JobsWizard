import streamlit as st
from streamlit_tags import st_tags

def add_style_sheet():
  with open('streamlit_customizations.css') as style_sheet:
    return st.markdown(f'<style>{style_sheet}<style>', unsafe_allow_html=True)

def reduced_empty_space_at_top():
  return st.markdown(
    """
        <style>
            .appview-container .main .block-container {{
                padding-top: {padding_top}rem;
                padding-bottom: {padding_bottom}rem;
                }}

        </style>""".format(
        padding_top=3, padding_bottom=1
    ),
    unsafe_allow_html=True,
)

def create_languages(acceptable_multiselect_key, not_acceptable_multiselect_key):
  st.multiselect(key=acceptable_multiselect_key, default=[], label='', format_func=lambda x: f"in {x} ", options=['Argentina', 'United States', 'Others'],placeholder='Should be in countries')
  st.multiselect(key=not_acceptable_multiselect_key, default=[], label='', format_func=lambda x: f"not in {x} ", options=['Argentina', 'United States', 'Others'],placeholder='Should not be in countries')


def create_requirements(importance, mandatory):
    st.text('Experience in fields you hold experience')
    st.slider(key=importance+mandatory+'required_experience_in_fields_you_hold_experience',  label='', min_value=0, max_value=20, value=(0,20), format='%x years')
    st.text('Experience in other fields')
    st.slider(key=importance+mandatory+'required_experience_in_other_fields', label='', min_value=0, max_value=20, value=(0,20), format='%x years')
    st.multiselect(key=importance+mandatory+'required_languages', default=[], label='', options=['None','English', 'Spanish', 'French', 'Portuguese', 'Others'],placeholder='Languages')
    st.multiselect(key=importance+mandatory+'required_education_level', default=[], label='', options=['None','Technician','Bachelor','Master', 'Doctor', 'PhD'],placeholder='Education Level')
    st.multiselect(key=importance+mandatory+'required_education_field', default=[], label='', options=['None','Related', 'Computer Sciences'],placeholder='Education Field')

from streamlit_extras.stylable_container import stylable_container
def example():
    with stylable_container(
        key="green_button",
        css_styles="""
            button {
                background-color: green;
                color: white;
                border-radius: 20px;
            }
            """,
    ):
        st.button("Green button")

    st.button("Normal button")

    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: calc(1em - 1px)
            }
            """,
    ):
        st.markdown("This is a container with a border.")

    


def create_fields(importance:str): #Maybe add responsabilities?
  st.markdown(
  """
  <style>
    div.st-ae>div>div.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am.st-an.st-ao.st-ap.st-aq.st-ar{
      flex-wrap: wrap;
    }
    div.st-ae>div.st-af{
      background-color: green;
    }
    /*Para el ultimo hice right click copy css selector, pero creo que con route hubiera funcionado aunque da alto choclo */
    /*Ojo que seleccione solo el caso salary!*/
    /*html body div#root div div.withScreencast div div.stApp.stAppEmbeddingId-s7y0ccgl4s7l.st-emotion-cache-1r4qj8v.erw9t6i1 div.appview-container.st-emotion-cache-1wrcr25.ea3mdgi4 section.main.st-emotion-cache-uf99v8.ea3mdgi3 div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi2 div.st-emotion-cache-0.e1f1d6gn0 div.st-emotion-cache-1wmy9hl.e1f1d6gn1 div.st-emotion-cache-1n76uvr.e1f1d6gn2 div.st-emotion-cache-0.eqpbllx5 details.st-emotion-cache-1h9usn1.eqpbllx4 div.st-emotion-cache-1clstc5.eqpbllx1 div.st-emotion-cache-0.e1f1d6gn0 div.st-emotion-cache-1wmy9hl.e1f1d6gn1 div.st-emotion-cache-1w1t4c.e1f1d6gn2 div.st-emotion-cache-r421ms.e10yg2by1 div.st-emotion-cache-0.e1f1d6gn0 div.st-emotion-cache-1wmy9hl.e1f1d6gn1 div.st-emotion-cache-1b6fvrv.e1f1d6gn2 div.stTabs.st-emotion-cache-0.esjhkag0 div.st-ae div#tabs-bui3094-tabpanel-0.st-ai.st-bi.st-cb.st-b3.st-b4.st-b1 div.st-emotion-cache-0.e1f1d6gn0 div.st-emotion-cache-1wmy9hl.e1f1d6gn1 div.st-emotion-cache-1b6fvrv.e1f1d6gn2 div.stTabs.st-emotion-cache-0.esjhkag0 div.st-ae div div.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am.st-an.st-ao.st-ap.st-aq.st-ar div.st-c2.st-c3.st-c4.st-c5.st-c6.st-c7.st-gb.st-c9.st-f5.st-f6.st-f7*/
    div.st-ae>div>div.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am.st-an.st-ao.st-ap.st-aq.st-ar>div.st-gb{
      background-color: blue;
    };
  <style>
  """, unsafe_allow_html=True)
  #/html/body/div/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[2]/details/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div/div[3]/div/div[1]/div/div
  job_title, location, language, education, experience, skills, date_posted, salary = st.tabs(['👨‍🚀 Job Title', '🪐 Location', '🗯️ Language', '👩‍🎓 Education', '📑 Experience' , '📜 Skills', '📆 Date Posted', '💰 Salary'])

  with job_title:
    #Maybe add an example
    st.markdown('***Write a word or phrase and press enter.***')
    st.text('Should contain:') #Todo change the style of the tags to prevent unnecesary space or if not possible remove text use label and change label format
    st_tags(key=importance+'job_title_desire', value=[], label='', suggestions=['analyst', 'business intelligence', 'data'], text='Phrases that should be in job title')
    st.text('Should not include:')
    st_tags(key=importance+'job_title_avoid', value=[], label='', suggestions=['intern', 'sr', 'data entry'], text='Phrases that should not appear in job title ')

  with location:
    st.checkbox('Treat remote postings requiring specific work permits as hybrid', value=True, key=importance+'exclude_fake_remotes')
    on_site, hybrid, remote = location.tabs(['🏣 On site','🐉 Hybrid','💻 Remote'])

    with on_site:
      create_languages(importance+'on_site_acceptable_countries', importance+'on_site_not_acceptable_countries')
      
    with hybrid:
      create_languages(importance+'hyrid_acceptable_countries', importance+'hybrid_not_acceptable_countries')

    with remote:
      create_languages(importance+'remote_acceptable_countries', importance+'remote_not_acceptable_countries')

  with language:
    st.multiselect(key=importance+'exp1', default=[], label='', options=['Test'],placeholder='Fields Where You hold Experience')
    musts, preferences = st.tabs(['Musts', 'Preferences'])
    with musts:
      st.header('Requirements listed as mandatory')
      create_requirements(importance,'mandatory.')
    with preferences:
      st.header('Requirements listed as optional/prefered')
      create_requirements(importance,'not_mandatory.')

  with date_posted:
    st.markdown('**Job was posted between:**')
    st.slider(key=importance+'job_was_posted_between', label='', min_value=0, max_value=72, step=1, value=(0,72), format='%d hours ago')
    st.markdown('')
    st.markdown("""
    ***Our job database only contains jobs posted in the last 3 days because:***
    - The chances to land a job if applying later drop significantlly.
    - It allow us to host and share this tool for free.""")
  
  #Incluir benefits en salary


reduced_empty_space_at_top()
st.header('Jobs 🧙 Wizard')
st.markdown(
  """
  <style>
    div.st-ae>div>div.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am.st-an.st-ao.st-ap.st-aq.st-ar{
      flex-wrap: wrap;
    }
    div.st-ae>div.st-af{
      background-color: green;
    }
    /*Para el ultimo hice right click copy css selector, pero creo que con route hubiera funcionado aunque da alto choclo */
    /*Ojo que seleccione solo el caso salary!*/
    /*html body div#root div div.withScreencast div div.stApp.stAppEmbeddingId-s7y0ccgl4s7l.st-emotion-cache-1r4qj8v.erw9t6i1 div.appview-container.st-emotion-cache-1wrcr25.ea3mdgi4 section.main.st-emotion-cache-uf99v8.ea3mdgi3 div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi2 div.st-emotion-cache-0.e1f1d6gn0 div.st-emotion-cache-1wmy9hl.e1f1d6gn1 div.st-emotion-cache-1n76uvr.e1f1d6gn2 div.st-emotion-cache-0.eqpbllx5 details.st-emotion-cache-1h9usn1.eqpbllx4 div.st-emotion-cache-1clstc5.eqpbllx1 div.st-emotion-cache-0.e1f1d6gn0 div.st-emotion-cache-1wmy9hl.e1f1d6gn1 div.st-emotion-cache-1w1t4c.e1f1d6gn2 div.st-emotion-cache-r421ms.e10yg2by1 div.st-emotion-cache-0.e1f1d6gn0 div.st-emotion-cache-1wmy9hl.e1f1d6gn1 div.st-emotion-cache-1b6fvrv.e1f1d6gn2 div.stTabs.st-emotion-cache-0.esjhkag0 div.st-ae div#tabs-bui3094-tabpanel-0.st-ai.st-bi.st-cb.st-b3.st-b4.st-b1 div.st-emotion-cache-0.e1f1d6gn0 div.st-emotion-cache-1wmy9hl.e1f1d6gn1 div.st-emotion-cache-1b6fvrv.e1f1d6gn2 div.stTabs.st-emotion-cache-0.esjhkag0 div.st-ae div div.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am.st-an.st-ao.st-ap.st-aq.st-ar div.st-c2.st-c3.st-c4.st-c5.st-c6.st-c7.st-gb.st-c9.st-f5.st-f6.st-f7*/
    div.st-ae>div>div.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am.st-an.st-ao.st-ap.st-aq.st-ar>div.st-gb{
      background-color: blue;
    };
  <style>
""", unsafe_allow_html=True) #El segundo agarra solo date posted pero no sirve de nada.
parameters_section = st.expander(label='Search Parameters',expanded=True)

form:st.form = parameters_section.form('search form')
musts, wants = form.tabs(['✅ I Require', '❤️ I Want'], )

with musts:
  st.markdown("**If this conditions aren't met, discard the job**")
  create_fields('musts.')

with wants:
  st.markdown('**What would you like in the job?**')
  create_fields('wants.')

form.form_submit_button('Search!')
example()
