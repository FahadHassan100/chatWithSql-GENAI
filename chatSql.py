import warnings
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

import os
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor
os.environ['OPENAI_API_KEY'] = "sk-xxxx"

class ChatWithSql:
    """ChatWithSql class is use for chat and query user question with the Sql database"""
    def __init__(self, db_user,db_password,db_host,db_name):
        """This is an Constructor method for the ChatWithSql class"""
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_name = db_name

    
    def message(self, query):
        """Message method will take the query from the user and process the reasult and return the response

        Args:
            query (String): this is the questions of the user
        Returns:
            response(String): This is the response generated my LLM's
        """
        # Initializing llm
        llm = ChatOpenAI(model_name = "gpt-3.5-turbo")
        # Connecting Database
        db = SQLDatabase.from_uri(f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}")
        # Initalizing the toolkit
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)
        # Creating the agent executor
        agen_executor = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)
        response = agen_executor.run(query)
        return response
    

# obj = ChatWithSql("root", "", "localhost","testingdublicatedb")
# obj.message("How many tables do we have")  