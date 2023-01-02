<div align="center">
<img width="30%" src="https://user-images.githubusercontent.com/72341453/134747028-7e2d90cc-a92f-4f66-815e-54a0d50cca54.PNG">

# StudyBuddy
</div>

--> Check out the live demo here: https://studybud-ugit.onrender.com

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

--> Create a `.env` where `settings.py` is located and add the following environment variables from the `sample_env` file
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

#

### App API

A sample website was created to demonstrate the use of an API route from the Django app. You can check out the website through this [link](). This route gets the details of all rooms created. An example of how the API can be used is shown below.

--> Request
  - GET
  - HTTPS
  - URL: `https://studybud-ugit.onrender.com/api/rooms/`

--> Response
```json
[
  {
    "id": 9,
    "name": "JavaScript (updated)",
    "description": "",
    "updated": "2022-03-07T09:51:21.045513Z",
    "created": "2022-03-07T09:51:21.045740Z",
    "host": 1,
    "topic": 4,
    "participants": []
  },
  {
    "id": 6,
    "name": "React",
    "description": "Join me to discuss about React.",
    "updated": "2022-01-01T20:50:27.944332Z",
    "created": "2022-01-01T20:50:27.944525Z",
    "host": 2,
    "topic": 6,
    "participants": [
      2
    ]
  },
  {
    "id": 5,
    "name": "Ruby On Rails",
    "description": "Understanding the Ruby on Rails framework and building websites with it.",
    "updated": "2022-01-01T20:49:22.369547Z",
    "created": "2022-01-01T20:49:22.369761Z",
    "host": 2,
    "topic": 5,
    "participants": [
      1
    ]
  },
  {
    "id": 4,
    "name": "HTML, CSS & JavaScript",
    "description": "Let's build complicated websites with HTML, CSS and JavaScript.",
    "updated": "2022-01-01T20:48:08.107796Z",
    "created": "2022-01-01T20:48:08.108353Z",
    "host": 2,
    "topic": 4,
    "participants": [
      2
    ]
  },
  {
    "id": 2,
    "name": "Arduino programming",
    "description": "Learn how to build robots and mechatronic devices.",
    "updated": "2022-01-01T20:26:05.390672Z",
    "created": "2022-01-01T20:14:05.464655Z",
    "host": 2,
    "topic": 2,
    "participants": [
      2
    ]
  },
  {
    "id": 1,
    "name": "Let's learn Python",
    "description": "",
    "updated": "2022-01-01T17:23:10.951782Z",
    "created": "2022-01-01T17:23:10.952533Z",
    "host": 1,
    "topic": 1,
    "participants": [
      1,
      2
    ]
  }
]
```