from aiobreaker import CircuitBreaker

DEFAULT_FAIL_MAX = 5
DEFAULT_RESET_TIMEOUT = 60  # seconds

def create_circuit_breaker(fail_max: int = DEFAULT_FAIL_MAX, reset_timeout: int = DEFAULT_RESET_TIMEOUT) -> CircuitBreaker:
    """
    Creates and returns a new CircuitBreaker instance.

    :param fail_max: Maximum number of failures before opening circuit.
    :param reset_timeout: Time to wait before trying again (in seconds).
    :return: CircuitBreaker instance
    """
    breaker = CircuitBreaker(fail_max=fail_max, reset_timeout=reset_timeout)
    return breaker
