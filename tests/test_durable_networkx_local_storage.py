import os, pytest, uuid, networkx
from durable_network_x.storage_managers.local_file_storage_manager import LocalFileStorageManager
from durable_network_x import DurableNetworkX

current_directory = os.path.dirname(os.path.abspath(__file__))
storage_manager = LocalFileStorageManager(root_dir=os.path.join(current_directory, '.graphs'))
    

def test_throw_error_on_use_when_no_instance_created():
    netx = DurableNetworkX(
        storage_manager=storage_manager,
        graph_type="Graph"
    )

    with pytest.raises(FileNotFoundError):
        random_instance_id = str(uuid.uuid4())
        netx.use(random_instance_id)
        
def test_no_error_on_new_when_no_instance_created():
    netx = DurableNetworkX(
        storage_manager=storage_manager,
        graph_type="Graph"
    )

    random_instance_id = str(uuid.uuid4())
    netx.new(random_instance_id)
    assert isinstance(netx.graph, networkx.Graph)
    netx.delete()

def test_use_after_new_instance_created():
    random_instance_id = str(uuid.uuid4())
    netx = DurableNetworkX(
        storage_manager=storage_manager,
        graph_type="DiGraph"
    )
    
    with pytest.raises(FileNotFoundError):
        netx.use(random_instance_id)
    
    netx.new(random_instance_id)
    netx.save()
    assert isinstance(netx.graph, networkx.DiGraph)

    new_netx = DurableNetworkX(
        storage_manager=storage_manager,
        graph_type="DiGraph"
    )
    assert new_netx.graph is None
    new_netx.use(random_instance_id)
    assert isinstance(netx.graph, networkx.DiGraph)
    
    new_netx.delete()
    netx.delete()
    
    