Set it up locally `localhost:5000` - build the image `docker build --no-cache --tag <image_name> .`
and then `docker-compose up -d`  

 - The fun translations api only allows 5 calls per hour, even though I paid for a subscription. I tried getting in touch with them for some clarification on their api, but with no success so far.  The rest of the time it will just return the description. For production, I would need to have an answer from them. In tranlation service the adding header part is commented out, as the key I received does not seem to be valid anymore. 