import time

def measure_execution_time(func):
    """
    A decorator to measure the execution time of a function.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The wrapped function.

    """
    def wrapper(*args, **kwargs):
        """
        The wrapper function that replaces the original function.

        Args:
            *args: Positional arguments to be passed to the original function.
            **kwargs: Keyword arguments to be passed to the original function.

        Returns:
            The result of the original function.
        """
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time  # Calculate execution time
        print(f"Execution time of '{func.__name__}': {execution_time} seconds")
        return result  # Return the result of the original function
    return wrapper



@measure_execution_time
def example_function():
    """An example function to demonstrate the usage of the decorator."""
    time.sleep(2)
    print("Function executed")

example_function()
