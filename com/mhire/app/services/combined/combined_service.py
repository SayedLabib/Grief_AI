import logging
import time
from typing import Dict, Any

from com.mhire.app.services.sentiment_toolkit.sentiment_toolkit import SentimentToolkit
from com.mhire.app.services.schedule_builder.schedule_builder import ScheduleBuilder
from com.mhire.app.common.exceptions_utility import rethrow_as_http_exception
from com.mhire.app.services.combined.combined_schema import CombinedRequest, CombinedResponse
from com.mhire.app.common.json_handler import LLMJsonHandler

logger = logging.getLogger(__name__)

class CombinedService:
    """
    A service that combines functionality from SentimentToolkit and ScheduleBuilder
    to provide a comprehensive response including sentiment analysis, tool recommendations,
    and a personalized daily schedule.
    """

    def __init__(self):
        """Initialize the CombinedService with required components."""
        try:
            self.sentiment_toolkit = SentimentToolkit()
            self.schedule_builder = ScheduleBuilder()
            self.json_handler = LLMJsonHandler()
            
            if not self.sentiment_toolkit or not self.schedule_builder:
                raise ValueError("Failed to initialize: Missing required components")
                
        except Exception as e:
            logger.error(f"Failed to initialize CombinedService: {str(e)}")
            rethrow_as_http_exception(e)

    async def generate_combined_response(self, request: CombinedRequest) -> Dict[str, Any]:
        """
        Generate a combined response including sentiment analysis, tool recommendations,
        and a personalized daily schedule.
        
        Args:
            request: CombinedRequest model containing user's grief context
            
        Returns:
            Dict containing mood analysis, tool recommendations, and daily schedule
            
        Raises:
            HTTPException: For any errors in processing or invalid responses
        """
        try:
            start_time = time.time()
            
            # Step 1: Get sentiment analysis and tool recommendations
            sentiment_result = await self.sentiment_toolkit.analyze_grief(request)
            
            # Step 2: Generate daily schedule
            schedule_result = await self.schedule_builder.generate_daily_schedule(request)
            
            # Step 3: Combine results
            combined_result = {
                "mood": sentiment_result["mood"],
                "titles": sentiment_result["titles"],
                "schedule": schedule_result.model_dump()
            }
            
            # Validate with model and return as dictionary
            validated_model = self.json_handler.validate_model(combined_result, CombinedResponse)
            return validated_model.model_dump()
            
        except Exception as e:
            logger.error(f"Error in generate_combined_response: {str(e)}", exc_info=True)
            rethrow_as_http_exception(e)