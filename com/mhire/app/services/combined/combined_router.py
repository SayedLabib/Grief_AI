import logging
import time

from fastapi import APIRouter, Request

from com.mhire.app.services.combined.combined_service import CombinedService
from com.mhire.app.services.combined.combined_schema import CombinedRequest, CombinedResponse
from com.mhire.app.common.network_responses import NetworkResponse, HTTPCode, ErrorCode, Message

logger = logging.getLogger(__name__)

router = APIRouter()
combined_service = CombinedService()
response = NetworkResponse()

@router.post("/api/v1/sentiment-analyze")
async def combined_analysis(request: CombinedRequest, http_request: Request):
    """
    Generate a combined response including sentiment analysis, tool recommendations,
    and a personalized daily schedule based on the user's grief context.
    """
    start_time = time.time()
    
    try:
        combined_result = await combined_service.generate_combined_response(request)
        return response.success_response(
            http_code=HTTPCode.SUCCESS,
            message=Message.SuccessMessage.RESPONSE_GENERATED,
            data=combined_result,
            resource=http_request.url.path,
            duration=time.time() - start_time
        )
    
    except Exception as e:
        logger.error(f"Error in combined analysis: {str(e)}", exc_info=True)
        return response.json_response(
            http_code=HTTPCode.UNPROCESSABLE_ENTITY,
            error_code=ErrorCode.UnprocessableEntity.CONTEXT_PROCESSING_ERROR,
            error_message=f"{Message.ErrorMessage.UnprocessableEntity.CONTEXT_PROCESSING_ERROR}",
            resource=http_request.url.path,
            duration=time.time() - start_time
        )