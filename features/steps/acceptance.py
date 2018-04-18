import os

import requests
from behave import when, then

@when(u'I request a response for "{colour}" and "{animal}"')
def step_impl(context, colour, animal):
    endpoint = os.getenv("ENDPOINT")
    context.response = requests.get(url=endpoint, params={'colour': colour, 'animal': animal})


@then(u'the response should be "{animal_colour}"')
def step_impl(context, animal_colour):
    assert context.response.text == animal_colour, context.response.text