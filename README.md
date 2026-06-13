
conda create -p ./venv python=3.10 -y

conda activate ./venv
pip install -r requirements.txt  


STEPS LOGICS: 
1. Field to put my JD 
2. Upload PDF 
3. PDF to image ---> prpcessing --> Google Gemini Pro 
4. Prompts Template [Multiple Prompts ]


streamlit run  app.py 

GO TO GOOGLE AI STUDIO FOR API KEY 
https://aistudio.google.com/api-keys?project=gen-lang-client-0237850925
go to GOOGLE SERPER TOOLS AND GET API KEY 


in env file :

GOOGLE_API_KEY=""

SERPER_API_KEY=''

# https://serper.dev/api-keys


python -m pip install streamlit

python -m pip install -r requirements.txt

pip uninstall streamlit starlette -y
pip install streamlit==1.45.1

Then verify:

pip show streamlit
pip show starlette


Upgrade the Gemini SDK

Inside your virtual environment:

pip uninstall google-generativeai -y
pip install -U google-generativeai

Verify:

pip show google-generativeai
python -m pip install google-generativeai
python -m pip show google-generativeai



python test_models.py

Let's rebuild cleanly once more and force Python 3.11.

1. Exit the current venv
deactivate
2. Delete the environment

From project root:

rm -rf venv
3. Check Python versions installed
which python3
python3 --version

which python3.11
python3.11 --version

If python3.11 says command not found:

brew install python@3.11

Then:

python3.11 --version

Expected:

Python 3.11.x
4. Create venv explicitly with Python 3.11
python3.11 -m venv venv

Activate:

source venv/bin/activate

Verify:

python --version
which python

Expected:

Python 3.11.x
.../ResumeATS_Tracking_LLMG_EMINIpRO/venv/bin/python
5. Install dependencies fresh
python -m pip install --upgrade pip

python -m pip install \
google-generativeai \
streamlit \
python-dotenv \
pillow \
pdf2image \
cryptography
6. Test import only

test_models.py

import google.generativeai as genai

print("Gemini import OK")

Run:

python test_models.py

Expected:

Gemini import OK

If that works, restore the .env loading and model listing afterward.

Also: do not use conda activate ./venv for a Python venv. Use:

source venv/bin/activate

only.


git pull origin main --rebase
git push origin main --force

# To deactivate an active environment, use
#
#     $ conda deactivate


verify environments exist: 

conda env list
python --version


To run : streamlit run app.py 



G_API_   KEY
"AQ*****Ab8RN6KjZNXtfNmzTUPKE9RDIW2VPL-*****P3kpvqNDv8Kk-******dGLZ2Q"

OPENAI  _API_                   KEY
'sk-********proj-yfMUKgvWkSzV0y9y2ewgxHTNnkieiaL3_mZm5uRth0ohH98y3KBbu-Y*****YMElkjCyzeTWO5JZjIoT3BlbkFJKUvzi1_qVDzS-IOPUHSK2nCgdHe0ZGCcdEjVlgfKrHDEBA008eOe7wKayaO849uX8E7-*******TaP1MA'



