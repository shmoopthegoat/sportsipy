from ratelimit import limits, sleep_and_retry

CALLS = 1
RATE_LIMIT = 60

@sleep_and_retry
@limits(calls = CALLS, period = RATE_LIMIT)
def check_limit():
    print('sleeping for 60 seconds')
    return