class InsufficientRights(Exception):
    """The requesting client does not have sufficient rights for a service"""


class InvalidEntityID(Exception):
    """The given entity ID is not a valid UUID"""


class InvalidPrivateKey(Exception):
    """The given private key is not a valid PEM string"""


class InvalidIssuer(Exception):
    """The issuer is not valid"""
    

class InvalidIssuerFormat(Exception):
    """The issuer format is not a valid UUID"""
    
    
class InvalidIssuerVersion(Exception):
    """The issuer UUID is the wrong version type"""
    

class InvalidAlgorithm(Exception):
    """Input algorithm is not supported"""


class InvalidPolicyFormat(Exception):
    """Invalid policy format. A JSON object is expected which is in the proper format containing minimum_requirements
    and factors."""


class DuplicateGeoFenceName(Exception):
    """The input Geo-Fence name is already taken"""


class InvalidGeoFenceName(Exception):
    """The input Geo-Fence name was not found"""


class DuplicateTimeFenceName(Exception):
    """The input Time-Fence name is already taken"""


class InvalidTimeFenceName(Exception):
    """The input Time-Fence name was not found"""


class InvalidTimeFenceStartTime(Exception):
    """The input start time should be a datetime.time object"""


class InvalidTimeFenceEndTime(Exception):
    """The input end time should be a datetime.time object"""


class MismatchedTimeFenceTimezones(Exception):
    """Start time and end time timezones must match"""


class LaunchKeyAPIException(Exception):
    error_code = None

    """API Error (400+) was returned"""
    def __init__(self, message=None, status_code=None, reason=None, *args, **kwargs):
        super(LaunchKeyAPIException, self).__init__(message, *args, **kwargs)
        self.message = message
        self.status_code = status_code
        self.reason = reason
        if self.error_code is None:
            self.error_code = message['error_code'] if message and 'error_code' in message else None


class InvalidParameters(LaunchKeyAPIException):
    """API Error ARG-001 - Parameter validation error"""
    error_code = "ARG-001"


class InvalidRoute(LaunchKeyAPIException):
    """API Error ARG-002 - The requested route does not exist in the requested path + method"""
    error_code = "ARG-002"


class ServiceNameTaken(LaunchKeyAPIException):
    """API Error SVC-001 - The requested Service name is already in use. Service names are unique."""
    error_code = "SVC-001"


class InvalidPolicyInput(LaunchKeyAPIException):
    """API Error SVC-002 - The input auth policy is not valid"""
    error_code = "SVC-002"


class PolicyFailure(LaunchKeyAPIException):
    """API Error SVC-003 - Auth creation failed due to user not passing policy"""
    error_code = "SVC-003"


class ServiceNotFound(LaunchKeyAPIException):
    """API Error SVC-004 - The requested Service does not exist. Likely invalid UUID or the service has been removed."""
    error_code = "SVC-004"


class InvalidPublicKey(LaunchKeyAPIException):
    """API Error KEY-001 - The public key you supplied is not valid."""
    error_code = "KEY-001"


class PublicKeyAlreadyInUse(LaunchKeyAPIException):
    """API Error KEY-002 - The public key you supplied already exists for the requested entity.
    It cannot be added again."""
    error_code = "KEY-002"


class PublicKeyDoesNotExist(LaunchKeyAPIException):
    """API Error KEY-003 - The key_id you supplied could not be found."""
    error_code = "KEY-003"


class LastRemainingKey(LaunchKeyAPIException):
    """API Error KEY-004 - The last remaining public key cannot be removed."""
    error_code = "KEY-004"


class DirectoryNameInUse(LaunchKeyAPIException):
    """API Error ORG-003 - The input Directory name is already in use."""
    error_code = "ORG-003"


class LastRemainingSDKKey(LaunchKeyAPIException):
    """API Error ORG-005 - The last remaining Authenticator SDK Key cannot be removed."""
    error_code = "ORG-005"


class InvalidSDKKey(LaunchKeyAPIException):
    """API Error ORG-006 - The Authenticator SDK Key you supplied does not belong to the referenced Directory"""
    error_code = "ORG-006"


class InvalidDirectoryIdentifier(LaunchKeyAPIException):
    """API Error DIR-001 - The input directory identifier was invalid"""
    error_code = "DIR-001"


class Unauthorized(LaunchKeyAPIException):
    """Generic API 401 Error - Authentication was denied. Likely an invalid key."""
    error_code = "HTTP-401"


class Forbidden(LaunchKeyAPIException):
    """Generic API 403 Error"""
    error_code = "HTTP-403"


class EntityNotFound(LaunchKeyAPIException):
    """Generic API 404 Error - Entity was not found"""
    error_code = "HTTP-404"


class RequestTimedOut(LaunchKeyAPIException):
    """Generic API 408 Error - Request timed out"""
    error_code = "HTTP-408"


class RateLimited(LaunchKeyAPIException):
    """Generic API 429 Error - Rate Limited"""
    error_code = "HTTP-429"


class UnexpectedAPIResponse(LaunchKeyAPIException):
    """The API returned a response that cannot be handled"""


class UnexpectedDeviceResponse(LaunchKeyAPIException):
    """The device returned a response that cannot be handled"""


class InvalidDeviceStatus(LaunchKeyAPIException):
    """The device status code is not recognized"""


class JWTValidationFailure(LaunchKeyAPIException):
    """JWT Response from the API was determined to be invalid"""


class UnexpectedKeyID(LaunchKeyAPIException):
    """The given key id was not unrecognized"""


class NoIssuerKey(LaunchKeyAPIException):
    """Issuer key was not loaded"""


class InvalidJWTResponse(LaunchKeyAPIException):
    """JWT Response is not in a valid format"""
