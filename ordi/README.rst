Ordibooth
=========

Ordibooth is a photobooth originally built for Maker Faire, which drew single line drawings of images.  Unfortunately the original SD card on the raspberry pi became corrupt.  This new version adds generic photoboooth capability as well, ans runs using a flask server.  The server controls the camera using CHDK.  The pi has a Kivy based UI which generates requests to the server to take a photo.  The server makes the photo available to the pi which loads the pic for approval.  The pic can be sent to the Flaschen Taschen and a link is generated to retrieve the photo.

