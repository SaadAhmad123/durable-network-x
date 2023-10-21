import os, pytest, uuid, networkx
from durable_network_x.storage_managers.local_file_storage_manager import LocalFileStorageManager
from durable_network_x.durable_graph import DurableGraph

current_directory = os.path.dirname(os.path.abspath(__file__))
storage_manager = LocalFileStorageManager(root_dir=os.path.join(current_directory, '.graphs'))
    

def test_throw_error_on_use_when_no_instance_created():
    netx = DurableGraph(storage_manager=storage_manager)

    with pytest.raises(FileNotFoundError):
        random_instance_id = str(uuid.uuid4())
        netx.use(random_instance_id)
        
def test_no_error_on_new_when_no_instance_created():
    netx = DurableGraph(storage_manager=storage_manager)

    random_instance_id = str(uuid.uuid4())
    netx.new(random_instance_id)
    assert isinstance(netx.graph, networkx.Graph)
    netx.delete()
    assert netx.graph is None

def test_use_after_new_instance_created():
    random_instance_id = str(uuid.uuid4())
    netx = DurableGraph(storage_manager=storage_manager)
    
    with pytest.raises(FileNotFoundError):
        netx.use(random_instance_id)
    
    netx.new(random_instance_id)
    netx.save()
    assert not isinstance(netx.graph, networkx.DiGraph)
    assert isinstance(netx.graph, networkx.Graph)

    new_netx = DurableGraph(storage_manager=storage_manager)
    assert new_netx.graph is None
    assert new_netx.exists_in_storage(random_instance_id) == True
    new_netx.use(random_instance_id)
    assert not isinstance(new_netx.graph, networkx.DiGraph)
    assert isinstance(new_netx.graph, networkx.Graph)
    
    new_netx.delete()
    netx.delete()
    assert netx.graph is None
    assert new_netx.graph is None    