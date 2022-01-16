Poke Api
=========

Description
-----------
I have developed a very basic 'Pokedex' applicaiton in the form of a REST API that return pokemon information. I am using existing public APIs ('https://pokeapi.co/' and 'https://funtranslations.com/') to do the heavy-lifting. 


## API Endpoints
### Get Pokemon Details [GET /pokemon/<name>]

Returns details of the required pokemon

+ Response 200 (application/json)

       {
            'name': 'Pokemon name',
            'description': 'Pokemon description',
            'habitat': 'Pokemon habitat,
            'isLegendary': True/False
        }

+ Response 404 (application/json)

        {
            "message": "Pokemon not found",
            "status": 404
        }

### Get pokemon details with translated description [GET /pokemon/translated/<name>]

Returns details of the required pokemon

+ Response 200 (application/json)

       {
            'name': 'Pokemon name',
            'description': 'Pokemon description translated',
            'habitat': 'Pokemon habitat,
            'isLegendary': True/False
        }

+ Response 404 (application/json)

        {
            "message": "Pokemon not found",
            "status": 404
        }


Installation and testing
------------------------
In order to run this project locally, you need to have docker installed. Find more [here](https://www.docker.com/get-started) <br />
Also, you would need to create an .env file in the `app` directory. Paste in there the environment variables

1. Setup project locally
    - open up your terminal window(or GitBash if running on Windows)
    - move into the app directory: run `cd app`
    - spin up the application locally: run `docker-compose up -d`
    - if you want to shut the application down, run `docker-compoer down`

You should now be able to test the application locally, on `http://localhost:5000`

2. Testing <br />
We only added unit tests, but for a production environment, these would not suffice. We would also add integration and e2e tests.
    - open up your terminal window(or GitBash) if running on Windows
    - move into the app directory: run `cd app` <br />
    At this point, there are two options: <br />
        a) Install python3 locally, choosing the best option for your machine. Find more [here](https://www.python.org/downloads/) <br />
            - install the dependencies locally: run `pip3 install -r requirements.txt` <br />
        OR <br />
        b) get inside your docker container: <br />
            - get container id: run `docker ps` and copy the container id associated with the app_pokedex_docker image <br />
            - get inside the box: run `docker exec -it <container_id> bash` <br />
    Whichever option you chose, you should be able to:
    - Run tests: run `python -m unittest`
    - Check tests coverage : run `coverage report -m`
    
Caveats
-------

1. Fun translations API
    - The fun translations api send back a 401 response, despite me buying a subscription from them. That is why in the tranlation service the adding header part is commented out, as the key I received does not seem to be valid anymore. 
    - The public version of the API only allows 5 calls per hour. That is why the translation service will only return the translated description 5 times/hour. The rest of the time it will just return the description.
    - I tried getting in touch with them for some clarification on their api, but with no success so far. For production, I would need to have an answer from them. 

2. Pokemon service
    - The get description method replaces `\n` and `\f` characters with empty spaces, but because sometimes the `https://pokeapi.co/api/v2/pokemon-species/` endpoint returns these characters inside the words, there are cases where words are split. It was a conscious decision, otherwise we would have had many words with no spaces between them.

