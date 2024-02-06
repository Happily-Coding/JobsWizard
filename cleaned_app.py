import streamlit as st
from streamlit_tags import st_tags

def create_page():
    st.session_state.should_contain = []
    st.set_page_config(page_title='Jobs Wizard', page_icon=":male_mage:")
    stylesheet_as_st_markdown()
    st.header('Jobs  Wizard 🧙')
    create_parameters_form()
    create_filters()
    generate_state_text()

def generate_state_text():
   pretty_session_sate_list = [f'**{str(state_key).strip()}**:|{str(state_value).strip()}|' for state_key, state_value in st.session_state.items() if ('FormSubmitter' not in str(state_key)) & (state_value not in (None, [])) ]
   #pretty_session_sate_list = [f'**{state_key}**value{str(state_value)}value_type{type(state_value)}' for state_key, state_value in st.session_state.items() ]
   pretty_session_sate_list.sort()
   pretty_session_string = '\n\n'.join(pretty_session_sate_list)
   return st.markdown(pretty_session_string )

def create_parameters_form():
    parameters_section = st.expander(label='Search Parameters', expanded=True)

    form:st.form = parameters_section.form('search form')
    musts, wants = form.tabs(['✅ I Require', '❤️ I Want'])

    with musts:
        st.markdown("**If this conditions aren't met, discard the job**")
        create_fields('mandatory_')

    with wants:
        st.markdown('**What would you like in the job?**')
        create_fields('ideal_')

    form.form_submit_button('Search!', on_click=generate_state_text)

def stylesheet_as_st_markdown():
  with open('streamlit_customizations.css') as style_sheet:
    style_sheet_text = style_sheet.read()
    #return st.write(f'Style sheet:{style_sheet}')
    return st.markdown(f'<style>{style_sheet_text}<style>', unsafe_allow_html=True)

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


def create_fields(prefix:str): #Maybe add responsabilities?
  #/html/body/div/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[2]/details/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div/div[3]/div/div[1]/div/div
  job_title, location, language, education, experience, skills, date_posted, salary = st.tabs(['👨‍🚀 Job Title', '🪐 Location', '🗯️ Language', '👩‍🎓 Education', '📑 Experience' , '📜 Skills', '📆 Date Posted', '💰 Salary'])

  with job_title:
    #Maybe add an example
    st.markdown('***Write a word or phrase and press enter.***')
    st.text('Should contain:') #Todo change the style of the tags to prevent unnecesary space or if not possible remove text use label and change label format
    st_tags(key=prefix+'job_title_contains', value=[], label='', suggestions=['analyst', 'business intelligence', 'data'], text='Phrases that should be in job title')
    st.text('Should not include:')
    st_tags(key=prefix+'job_title_lacks', value=[], label='', suggestions=['intern', 'sr', 'data entry'], text='Phrases that should not appear in job title ')

  with location:
    st.checkbox('Treat remote postings requiring specific work permits as hybrid', value=True, key=prefix+'exclude_fake_remotes')
    on_site, hybrid, remote = location.tabs(['🏣 On site','🐉 Hybrid','💻 Remote'])

    with on_site:
      create_languages(prefix+'on_site_acceptable_countries', prefix+'on_site_not_acceptable_countries')
      
    with hybrid:
      create_languages(prefix+'hyrid_acceptable_countries', prefix+'hybrid_not_acceptable_countries')

    with remote:
      create_languages(prefix+'remote_acceptable_countries', prefix+'remote_not_acceptable_countries')

  with language:
    st.multiselect(key=prefix+'exp1', default=[], label='', options=['Test'],placeholder='Fields Where You hold Experience')
    musts, preferences = st.tabs(['Musts', 'Preferences'])
    with musts:
      st.header('Requirements listed as mandatory')
      create_requirements(prefix,'required_')
    with preferences:
      st.header('Requirements listed as optional/prefered')
      create_requirements(prefix,'prefered_')

  with date_posted:
    st.markdown('**Job was posted between:**')
    st.slider(key=prefix+'job_was_posted_between', label='', min_value=0, max_value=72, step=1, value=(0,72), format='%d hours ago')
    st.markdown('')
    st.markdown("""
    ***Our job database only contains jobs posted in the last 3 days because:***
    - The chances to land a job if applying later drop significantlly.
    - It allow us to host and share this tool for free.""")
  
  #Incluir benefits en salary

def create_filters():
   container = st.container()
   container.header('Filters')
   #container.text(st.session_state.should_contain)
   return container

create_page()