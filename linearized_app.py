import streamlit as st
from streamlit_tags import st_tags

def create_page():
    st.session_state.should_contain = []
    st.set_page_config(page_title='Jobs Wizard', page_icon=":male_mage:")
    stylesheet_as_st_markdown()
    st.header('💼 Jobs  Wizard 🧙')
    create_parameters_form()

def stylesheet_as_st_markdown():
  with open('streamlit_customizations.css') as style_sheet:
    style_sheet_text = style_sheet.read()
    return st.markdown(f'<style>{style_sheet_text}<style>', unsafe_allow_html=True)
  
def create_parameters_form():
    parameters_section = st.expander(label='Lets prepare the Search Spell 🔮', expanded=True)
    #Possibly add search params load and save button here.
    form:st.form = parameters_section.form('search form')
    create_job_title(form)
    form.markdown('<br/>', unsafe_allow_html=True)
    create_location(form)
    form.markdown('<br/>', unsafe_allow_html=True)
    create_language(form)
    form.markdown('<br/>', unsafe_allow_html=True)
    create_education(form)
    form.markdown('<br/>', unsafe_allow_html=True)
    create_experience(form)
    form.markdown('<br/>', unsafe_allow_html=True)
    create_skills_tools_and_techniques(form)
    form.markdown('<br/>', unsafe_allow_html=True)
    form.form_submit_button('## 💫 **Search** 💫', on_click=generate_state_text)

def create_job_title(container):
    with container:
      st.markdown('### 👨‍🚀 Job Title')
      st.markdown('***Write a word or phrase and press enter.***')
      st.text('Title Must Contain:')
      st_tags(key='job_title_contains', value=[], label='', suggestions=['analyst', 'business intelligence', 'data'], text='Phrases that should be in job title')
      st.text('Title Must NOT include:')
      st_tags(key='job_title_lacks', value=[], label='', suggestions=['intern', 'sr', 'data entry'], text='Phrases that should not appear in job title ')
def create_location(container):
  with container:
    st.markdown('### 🪐 Location')
    st.checkbox('Treat remote postings requiring specific work permits/residence as hybrid', value=True, key='exclude_fake_remotes')
    #st.markdown('The job can be')
    on_site, hybrid, remote = container.tabs(['🏣 On site','🐉 Hybrid','💻 Remote'])
    with on_site:
      create_location_selectors('on_site_acceptable_countries', 'on_site_not_acceptable_countries')
    with hybrid:
      create_location_selectors('hyrid_acceptable_countries', 'hybrid_not_acceptable_countries')
    with remote:
      create_location_selectors('remote_acceptable_countries', 'remote_not_acceptable_countries')

def create_location_selectors(acceptable_multiselect_key, not_acceptable_multiselect_key):
  st.multiselect(key=acceptable_multiselect_key, default=[], label='',label_visibility='collapsed', format_func=lambda x: f"in {x} ", options=['Argentina', 'United States', 'Others'],placeholder='In countries')
  st.multiselect(key=not_acceptable_multiselect_key, default=[], label='', label_visibility='collapsed', format_func=lambda x: f"not in {x} ", options=['Argentina', 'United States', 'Others'],placeholder='Not in countries')

def create_language(container):
  with container:
    st.markdown('### 🗯️ Language')
    #st.checkbox('Treat postings in a certain language as requiring that language', value=True, key='use_implicit_language_requirements')
    #st.markdown('*Select languages that you know, and can be required by the job lister*')
    st.multiselect(key='known_languages', default=[], label='',label_visibility='collapsed', options=['Spanish', 'English', 'Portuguese'],placeholder='Languages that you know' )#, format_func=lambda x: f"{x} req "
    #How about jobs that prefer? Just boost them up if you have it?

def create_education(container):
  with container:
    st.markdown('### 👩‍🎓 Education')
    st.markdown('You hold degrees equivalent to: ')
    st.multiselect(key='degrees_held', default=[], label='',label_visibility='collapsed', format_func=lambda x: f"{x}  ", options=[' Bachelors, "Related"','Bachelor, Biology', 'Bachelor, Data Science', 'Bachelor, Data Analysis'],placeholder='Your degrees')
    container.markdown('<br/>', unsafe_allow_html=True)
    st.markdown('Jobs can require an education _ levels above yours.')
    st.slider(key='education_acceptable_level_difference',label='',label_visibility='collapsed', min_value=0, max_value=4, value=2, step=1)
    #How about jobs that prefer? Just boost them up if you have it?

def create_experience(container):
  with container:
    st.markdown('### 📑 Experience')
    st.text('You have experience equivalent to:')
    st.multiselect(key='experience_held', default=[], label='',label_visibility='collapsed', format_func=lambda x: f"{x}  ", options=[' "Related", 1y', 'Data Analysis, 1y', 'Data Science, 1y', 'Machine Learning, 1y'],placeholder='Your experience, Years')
    container.markdown('<br/>', unsafe_allow_html=True)
    st.markdown('Jobs can require _ years of experience more than you have per field') # I considered percentage of the experience, while it would be more precise itd be less intuitive so not a good idea.
    st.slider(key='experience_required_acceptable_level_difference',label='',label_visibility='collapsed', min_value=0, max_value=5, value=2, step=1)
    #Add the same parameters for total experience? It doesnt seem that relevant and complicates the form so proably not a good idea.
    #How about jobs that prefer? Just boost them up if you have it?

def create_skills_tools_and_techniques(container):
    with container:
      st.markdown('### 📜 Skills, Tools, and Techniques')
      st.markdown('What skills, tools or techniques do you know? Make sure to note soft skills here too.')
      st.multiselect(key='skills_known', default=[], label='',label_visibility='collapsed', format_func=lambda x: f"{x}  ", options=['Power BI', 'Pandas', 'Communication'],placeholder='Skill, Tool or Technique')
      container.markdown('<br/>', unsafe_allow_html=True)
      st.markdown('What proportion of the skills do you need to know in order to consider the job?')
      st.slider(key='skills__required_acceptable_level_difference',label='',label_visibility='collapsed',format="%d%%", min_value=0,  step=5, max_value = 100, value = 30) #min_value=0.0, max_value=10/10, value=50/100, step=5/100)
      #Consider the prefered skills for sorting but not for filtering?
      #create checkbox to ignore soft skills? Or just place them in a separate box and consider them sepparately? It makes the form more complex but its also likely going to result in better average searches.
      #st.markdown('Are you certified in any skills?')
      #Separar skills ceritifacdos?
      #st.multiselect(key='certifications_held', default=[], label='',label_visibility='collapsed', format_func=lambda x: f"{x}  ", options=['Power BI', 'Pandas', 'Communication'],placeholder='Skill, Tool or Technique')

def create_post_date(container):
     with container:
      st.markdown('### 📆 Date Posted')
      st.markdown('**Job was posted between:**')
      st.slider(key='job_was_posted_between', label='', min_value=0, max_value=72, step=1, value=(0,72), format='%d hours ago')
      st.markdown('')
      st.markdown("""
      ***Our job database only contains jobs posted in the last 3 days because:***
      - The chances to land a job if applying later drop significantlly.
      - It allow us to host and share this tool for free.""")

def create_applicant_numbers(container): #It could be included in a new category called post details along wiht applicant numbers and compensation
    with container:
      st.markdown('### 👥 Number of applicants')#Use one of this emojis instead?👨🏻‍💼🧑🏼‍🤝‍🧑🏾
      st.slider(key='max_applicants_already_applied', label='', min_value=0, max_value=72, step=1, value=(0,72), format='%d hours ago')

def create_applicant_numbers(container):
    with container:
      st.markdown('### 🏭 Companies')
      st.multiselect(key='acceptable_companies', default=[], label='',label_visibility='collapsed', format_func=lambda x: f"from {x} ", options=[' Any', 'Accenture', 'OnyxianLTD'],placeholder='Company')
      st.multiselect(key='not_acceptable_companies', default=[], label='',label_visibility='collapsed', format_func=lambda x: f"not from {x} ", options=[' Any', 'Accenture', 'OnyxianLTD'],placeholder='Company')


def create_compensation(container):
   with container:
      st.markdown('# 💰 Salary')

#TODO add capacity to load the posts youve applied or discarded, ATS system ideally,


def generate_state_text():
   pretty_session_sate_list = [f'**{str(state_key).strip()}**:|{str(state_value).strip()}|' for state_key, state_value in st.session_state.items() if ('FormSubmitter' not in str(state_key)) & (state_value not in (None, [])) ]
   #pretty_session_sate_list = [f'**{state_key}**value{str(state_value)}value_type{type(state_value)}' for state_key, state_value in st.session_state.items() ]
   pretty_session_sate_list.sort()
   pretty_session_string = '\n\n'.join(pretty_session_sate_list)
   return st.markdown(pretty_session_string )

    #'👨‍🚀 Job Title', '🪐 Location', '🗯️ Language', '👩‍🎓 Education', '📑 Experience' , '📜 Skills', '📆 Date Posted', '💰 Salary'




def create_experience_old(importance, mandatory):
    st.slider(key=importance+mandatory+'required_experience_in_fields_you_hold_experience',  label='', min_value=0, max_value=20, value=(0,20), format='%x years')
    st.text('Experience in other fields')
    st.slider(key=importance+mandatory+'required_experience_in_other_fields', label='', min_value=0, max_value=20, value=(0,20), format='%x years')
    st.multiselect(key=importance+mandatory+'required_languages', default=[], label='', options=['None','English', 'Spanish', 'French', 'Portuguese', 'Others'],placeholder='Languages')
    st.multiselect(key=importance+mandatory+'required_education_level', default=[], label='', options=['None','Technician','Bachelor','Master', 'Doctor', 'PhD'],placeholder='Education Level')
    st.multiselect(key=importance+mandatory+'required_education_field', default=[], label='', options=['None','Related', 'Computer Sciences'],placeholder='Education Field')

create_page()