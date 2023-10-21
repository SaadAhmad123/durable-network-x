import networkx
from durable_network_x import DurableNetworkX
from durable_network_x.storage_managers import StorageManager

class DurableGraph(DurableNetworkX):
    def __init__(self, storage_manager: StorageManager):
        super().__init__(storage_manager, graph_type = "Graph")
    
    def new(self, instance_id: str) -> 'DurableGraph':
        return super().new(instance_id)
    
    def use(self, instance_id: str) -> 'DurableGraph':
        return super().use(instance_id)
    
    def save(self) -> 'DurableGraph':
        return super().save()
    
    def delete(self) -> 'DurableGraph':
        return super().delete()
    
    @property
    def graph(self) -> networkx.Graph:
        return super().graph