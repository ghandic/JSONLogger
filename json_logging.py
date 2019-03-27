import socket
import subprocess


def JSONExtras(extras):
    """This is a utility function to add extra logging information
    
    Description:
        - If version is not set then it will try to get it from the git commit hash

    Args:
        extras: A dictionary of predefined extra logging attributes
   
    Returns:
        A dict of the combined defaults and defined logging attributes

    Raises:
        LoggingAttributeNotGiven: An error if compulsory logging attributes are not given                                                                 
    """
    
    COMPULSARY = set(['type'])
        
    missing_keys = COMPULSARY -  set(extras.keys())
    if missing_keys:
        raise LoggingAttributeNotGivenException(f"extras is missing logging attributes {missing_keys}")

    defaults = {'type': '', 
                'returncode': '', 
                'traceid': '', 
                'version': extras['version'] if extras.get('version') is not None else get_git_revision_hash(), 
                'uname': socket.gethostbyname(socket.gethostname())
               }
    
    return {**defaults, **extras}


def get_git_revision_hash():
    """This is a utility function returns the git commit hash of the current module
   
    Returns:
        A string of the commit hash                                                                 
    """
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    except FileNotFoundError:
        raise GitNotFoundException("Could not find git installed")
    except subprocess.CalledProcessError:
        raise NotGitProjectException("Current folder is not a git repo")
    


class LoggingAttributeNotGivenException(Exception):
    pass


class GitNotFoundException(Exception):
    pass


class NotGitProjectException(Exception):
    pass
