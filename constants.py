RESPONSE_CODE_OK=0
RESPONSE_CODE_ERROR_GENERIC=99
RESPONSE_CODE_ERROR_PARAMS_REQUIRED=11
RESPONSE_CODE_ERROR_BAD_REQUEST=400 # Podríamos definir otro codigo, por ahora usamos el mismo código de HTTP
RESPONSE_CODE_ERROR_NOT_CONTENT=204 # Podríamos definir otro codigo, por ahora usamos el mismo código de HTTP
RESPONSE_CODE_ERROR_PRODUCT_ALREADY_EXISTS=12
RESPONSE_CODE_ERROR_PRODUCT_NOT_EXISTS=13
RESPONSE_CODE_ERROR_USER_NOT_EXISTS=14

RESPONSE_MESSAGE_OK='Transacción realizada con éxito'
RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED='No se ingresaron todos los parámetros requeridos'
RESPONSE_MESSAGE_ERROR_BAD_REQUEST='Request mal formado'
RESPONSE_MESSAGE_ERROR_NOT_FOUND='No se encontró información con los filtros de búsqueda ingresados'
RESPONSE_MESSAGE_ERROR_PRODUCT_ALREADY_EXISTS='Ya existe un producto con ese nombre'
RESPONSE_MESSAGE_ERROR_PRODUCT_NOT_EXISTS='No existe el producto'
RESPONSE_MESSAGE_ERROR_GENERIC='Ocurrió un error inesperado'
RESPONSE_MESSAGE_ERROR_USER_NOT_EXISTS='No existe el usuario'