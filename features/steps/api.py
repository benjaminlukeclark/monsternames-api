from requests import post, get
from behave import *
from asserts import assert_equal


@given("a first name of {first_name}")
def step_imp(context, first_name):
    context.firstName = first_name
    context.data = {"firstName": first_name}


@then("I should be able to POST to {post_endpoint}")
def step_imp(context, post_endpoint):
    req = post(context.base_url + post_endpoint, data=context.data, headers={"x-api-key": context.api_key})
    assert_equal(req.status_code, 200)


@then("GET to {get_endpoint} will contain {fields}")
def step_imp(context, get_endpoint, fields):
    req = get(context.base_url + get_endpoint)
    response = req.json()
    for field in fields.split(","):
        assert_equal(
            field in response,
            True
        )
