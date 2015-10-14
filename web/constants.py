
# End points' methods
METHOD_GET_LIST = {'get': 'list'}
METHOD_GET_RETRIEVE = {'get': 'retrieve'}
METHOD_PUT_UPDATE = {'put': 'update'}
METHOD_POST_CREATE = {'post': 'create'}

# Configuration's validation messages
INVALID_URL = 'URL is not valid. Please give a valid URL again.'
DOES_NOT_EXIST = 'Email does not exist.'

def merge(first_dict, second_dict):
    """merges two dictionaries into a third one"""
    merged_dict = second_dict.copy()
    merged_dict.update(first_dict)
    return merged_dict