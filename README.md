<div align="center">
<img width="30%" src="https://user-images.githubusercontent.com/72341453/134747028-7e2d90cc-a92f-4f66-815e-54a0d50cca54.PNG">

# StudyBuddy
</div>

--> Check out the live demo here: https://studybudweb.herokuapp.com/

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/davidudo/studybud.git

```

--> Move into the directory where we have the project files : 
```bash
cd studybud

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :
```bash
source env/bin/activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

--> Create a `.env` and add the following environment variables
```
SECRET_KEY
CLOUD_NAME
API_KEY
API_SECRET
```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

### App Preview :

<div width="100%"> 
<p align="center">
  Feed Home
</p>
<img src="https://user-images.githubusercontent.com/72341453/134747262-0a92233d-8010-40f8-84c5-8d94895aac44.PNG">

<p align="center">
  Room Conversation Preview
</p>
<img src="https://user-images.githubusercontent.com/72341453/134747155-3ca5b55f-b064-4741-aeae-abe90bddf41e.PNG">  
</div>