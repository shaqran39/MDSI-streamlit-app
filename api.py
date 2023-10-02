import requests

def get_url(url: str):
    """
    Function that will call a provide GET API endpoint url and return its status code and either its content or error message as a string

    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called

    Returns
    -------
    int
        API call response status code
    str
        Text from API call response
    """

    response = requests.get(url)

    if response.status_code == 200:
            # Return the status code and the content as a string
            return response
    else:
            # Return the status code and an error message as a string
            return response.status_code, f"Unable to call the API, error code {response.status_code}"
