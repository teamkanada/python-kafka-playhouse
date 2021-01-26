# A Django API for voting on how something fits

An example API using DRF to send votes for how a product fits to a kafka stream for processing

## Run it

If you want to start up the application just build and up the docker images

`docker-compose build && docker-compose up`

## Update your migration
If you need to make changes apply your changes to the models and then run

`docker-compose exec python-kafka-playhouse python manage.py makemigrations`


## Run the tests

Coming soon