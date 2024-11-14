from enum import Enum

class LLMEnums(Enum):
    OPENAI = "OPENAI"
    COHERE = "COHERE"

class OpenAIEnums(Enum):
    SYSTEM = "system"
    UESR = "user"
    ASSISTANT = "asssistant"

class CoHereEnums(Enum):
    SYSTEM = "SYSTEM"
    UESR = "USER"
    ASSISTANT = "CHATBOT"
    DOCUMENT = "search_document"
    QUERY = "search_query"

class DocumentTypeEnum(Enum):
    DOCUMENT = "document"
    QUERY = "query"
