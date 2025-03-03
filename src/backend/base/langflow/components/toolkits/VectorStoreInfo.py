from langchain.agents.agent_toolkits.vectorstore.toolkit import VectorStoreInfo

from langflow.interface.custom.custom_component import CustomComponent
from langchain_core.vectorstores import VectorStore


class VectorStoreInfoComponent(CustomComponent):
    display_name = "VectorStoreInfo"
    description = "Information about a VectorStore"

    def build_config(self):
        return {
            "vectorstore": {"display_name": "VectorStore"},
            "description": {"display_name": "Description", "multiline": True},
            "name": {"display_name": "Name"},
        }

    def build(
        self,
        vectorstore: VectorStore,
        description: str,
        name: str,
    ) -> VectorStoreInfo:
        return VectorStoreInfo(vectorstore=vectorstore, description=description, name=name)
