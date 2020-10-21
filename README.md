# CARD SYSTEM DEMO FOR A HOLOCAUST THEMED MUSEUM

## Summary

This site simulates a card system in use on the Museum of Tolerance in Los Angeles (http://www.museumoftolerance.com) , for the exhibit on the Holocaust. Every visitor is given a card with the name and photo of a Jew child and as the visitor advances on the exhibit, putting the card on terminals with card readers, he/she is updated on the successive changes of the child history. At the end of the tour, the ultimate fate of the child is revealed.

This site allows to try how the system works, and its code on GitHub (free of rights) can help different Holocaust Museums worldwide to implement it (if authorized by the Museum of Tolerance). 

This system was shown on the movie "Freedom writers" (2007). 

### See further information on the home page of the web app.
 

## Technical information
### Django 3.1 / Python 3.8 / Bootstrap 4.5 / Cloudinary
(focus on the back-end; front-end not polished)

    - User-uploaded images (media) handled by Cloudinary. Static images handled by Whitenoise.

    - Secret keys based on environment variables for safe deployment.

    - Demo site implemented on Heroku with PostgreSQL DB and Cloudinary.

