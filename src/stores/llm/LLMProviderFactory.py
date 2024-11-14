from .LLMEnums import LLMEnums
from.providers import CoHereProvider,OpenAIProvider
class LLMProviderFactory:
    def __init__(self, config: dict) :
        self.config = config
    
    def create(self , provider:str):
        if provider == LLMEnums.OPENAI.value:
            return OpenAIProvider (
                api_key= self.config.OPENAI_API_KEY,
                api_url= self.config.OPENAI_API_URL,
                default_genetation_max_output_tokens= self.config.GENERATION_DEFAULT_MAX_TOKENS,
                default_input_max_characters=self.config.INPUT_DEFAULT_MAX_CHARACTERS,
                default_generation_temperature=self.config.GENERATION_DEFAULT_TEMPERATURRE
            )
        if provider == LLMEnums.COHERE.value:
            return CoHereProvider(
                api_key= self.config.COHERE_API_KEY,
                default_genetation_max_output_tokens= self.config.GENERATION_DEFAULT_MAX_TOKENS,
                default_input_max_characters=self.config.INPUT_DEFAULT_MAX_CHARACTERS,
                default_generation_temperature=self.config.GENERATION_DEFAULT_TEMPERATURRE)
        

        return None