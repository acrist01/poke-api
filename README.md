Set it up locally `localhost:5000` - build the image `docker build --no-cache --tag <image_name> .`
and then `docker-compose up -d`  

 - The fun translations api only allows 5 calls per hour, even though I paid for a subscription. I tried getting in touch with them for some clarification on their api, but with no success so far.  The rest of the time it will just return the description. For production, I would need to have an answer from them. In tranlation service the adding header part is commented out, as the key I received does not seem to be valid anymore. 

 - Run tests locally 
 From the `app` directory
 `docker ps` copy the container id associated with the app_pokedex_docker image and then run `docker exec -it <container_id> bash`
 this should take you inside the box, where you can run `python -m unittest`.  - option without python installation

 Alternatively, you can install python3 locally and then run `pip3 install -r requirements.txt` and then run `python -m unittest`