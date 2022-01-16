Poke Api
=========

Installation and testing
------------------------

1. Setup project locally
    - open up your terminal window(or GitBash) if running on Windows
    - move into the app directory: run `cd app`
    - build the image locally: run `docker build --no-cache --tag <image_name> .`
    - spin up the application locally: run `docker-compose up -d`

You should now be able to test the application locally, on `http://localhost:5000`

2. Testing
    - open up your terminal window(or GitBash) if running on Windows
    - move into the app directory: run `cd app`
    At this point, there are two options:
        a) Install python3 locally, choosing the best option for your machine. Find more [here](https://www.python.org/downloads/)
            * install the dependencies locally: run `pip3 install -r requirements.txt`
        OR 
        b) get inside your docker container:
            * get container id: run `docker ps` and copy the container id associated with the app_pokedex_docker image
            * get inside the box: run `docker exec -it <container_id> bash`
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
    - The get description method replaces `\n` and `\f` characters with empty spaces, but because sometimes the `https://pokeapi.co/api/v2/pokemon-species/` endpoint returns there characters inside the words, there are cases where words are split. It was a conscious decision, otherwise we would have had many words with no spaces between them.

