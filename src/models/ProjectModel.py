from.BaseDataModel import BaseDataModel
from .db_shemes import Project
from .enums.DataBaseEnum import DataBaseEnum

class ProjectModel(BaseDataModel):
    def __init__(self, db_client: object):
        super().__init__(db_client = db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value]
        
    async def init_collection(self):
        all_collections = await self.db_client.list_collection_names()
        if DataBaseEnum.COLLECTION_PROJECT_NAME.value  not in all_collections:
            self.collection = self.db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value]
            indexes = Project.get_indexes()
            for index in indexes:
                await self.collection.create_index(
                    index["key"],
                    name = index["name"],
                    unique=index["unique"]
                )

#We need to call init and init_collection, but init collection is async so we
#can't add it to __init__. The solution is creating async static function to call both methods
    @classmethod
    async def create_instance(cls , db_client: object):
        instance = cls(db_client)
        await instance.init_collection()
        return instance

    async def create_project(self, project:Project):

        result = await self.collection.insert_one(project.dict(by_alias=True , exclude_unset=True)) 
        project._id = result.inserted_id
        return project
    
    async def get_project_or_create_one(self , project_id : str):

        record = await self.collection.find_one({
            "project_id":project_id
        })
        
        if record is None:
            #create new project
            project = Project(project_id=project_id)
            project = await self.create_project(project= project)
            return project
        
        return Project(**record)
    
    #Use get all with pagination, page by page 
    async def get_all_projects(self,page:int=1 , page_size:int=10):

        #count total number of documents 
        total_documents = await self.collection.count_documents({})

        #calculate total number of pages 
        total_pages = total_documents // page_size
        
        if total_documents % page_size >0:
            total_pages+=1
        # creates a cursor to find documents in the collection,
        # skipping the documents of previous pages 
        # and limiting the results to the current page size
        cursor = self.collection.find().skip((page-1)*page_size).limit(page_size)
        projects =[]
        async for document in cursor:
            projects.append(
                Project(**document)
            )
        return projects , total_pages
