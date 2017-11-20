from behave import *
from hamcrest import assert_that, equal_to
from votelig import votelig
from helper import *

# Background: default_test
@given('default minimum voter age is {default_min_voter_age}')
def g_default_min(context, default_min_voter_age):

    default_min_voter_age = h_convert_if_number(default_min_voter_age)
    h_is_age_integer(default_min_voter_age, "default_min_voter_age")

    context.votelig = votelig.Votelig()
    assert_that(context.votelig.min_voter_age, equal_to(
                int(default_min_voter_age)
                )
                )


# Background: nondefault_test
@given('we change minimum voter age to {new_min_voter_age}')
def g_change_min(context, new_min_voter_age):

    new_min_voter_age = h_convert_if_number(new_min_voter_age)
    h_is_age_integer(new_min_voter_age, "new_min_voter_age")

    context.votelig = votelig.Votelig(new_min_voter_age)
    assert_that(context.votelig.min_voter_age,
                equal_to(int(new_min_voter_age))
                )


# Scenarios: default_test and nondefault_test -------------------#

@given('valid age {voter_age}')
def g_valid_age(context, voter_age):
    voter_age = h_convert_if_number(voter_age)
    h_is_age_integer(voter_age, "voter_age")
    context.voter_age = voter_age

def h_is_age_integer(age, field):
    '''
    Use when test case is supposed to send valid integer input for age. Catches incorrect test at the source.
    :param age: Value of the age field
    :param field: Field name to display in error message when age value is not integer
    :return: None
    '''
    if not isinstance((age), int):
        msg= "Test case passed argument {0} with invalid value {1} which could not be converted into integer".format(
                                                                                                                field,
                                                                                                                age)
        raise Exception(msg)

@then('voter is found eligible')
def t_voter_eligible(context):
    assert_that( context.eligible , equal_to(True))
    assert_that(context.error , equal_to(None) )


@then('voter is found ineligible')
def t_voter_ineligible(context):
    assert_that( context.eligible , equal_to(False))
    assert_that( context.error , equal_to(None) )


# Scenarios: default_test, nondefault_test, and Invalid_Input_test ------------#

@when('we check eligibility')
def w_check_eligibility(context):
    context.error = None
    try:
        context.eligible = context.votelig.is_eligible(context.voter_age)
    except Exception as e:
        context.eligible = None
        context.error = e




# Scenarios: Invalid_Input_test ----------------------------------------------#

@given('voter age input having {invalid_type} {value}')
def g_invalid_voter_age(context, invalid_type, value):
    context.field = "Voter age"
    value = h_convert_if_number(value)
    context.value, context.voter_age = value, value


@given('minimum voter age input having {invalid_type} {value}')
def g_invalid_min(context, invalid_type, value):
    context.field = "Minimum voter age"
    context.value = h_convert_if_number(value)


@when('we change minimum voter age to this invalid value')
def w_change_min_invalid(context):
    try:
        context.votelig = votelig.Votelig(context.value)
    except Exception as e:
        context.error = e


@then('error is returned')
def t_error_returned(context):
    expected_error_msg = "Invalid input {0}. {1} must be positive integer".format(context.value,
                                                                                  context.field)
    assert_that(
        str(context.error),
        equal_to(expected_error_msg)
    )

