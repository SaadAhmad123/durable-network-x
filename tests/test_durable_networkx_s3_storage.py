import os, pytest, uuid, networkx, time
from durable_network_x.storage_managers.s3_storage_manager import S3StorageManager
from tests.create_s3_bucket import S3Bucket
from durable_network_x import DurableNetworkX
from dotenv import load_dotenv
load_dotenv()

AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")

def test_durable_networkx_s3_storage():
    with S3Bucket('test-networkx') as bucket:
        storage_manager = S3StorageManager(
            bucket_name=bucket.bucket_name,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
        
        netx = DurableNetworkX(storage_manager)
        random_instance_id = str(uuid.uuid4())

        with pytest.raises(FileNotFoundError):
            netx.use(random_instance_id)

        netx.new(random_instance_id)
        assert isinstance(netx.graph, networkx.Graph)

        new_netx = DurableNetworkX(storage_manager)
        
        with pytest.raises(FileExistsError):
            new_netx.new(random_instance_id)

        assert new_netx.graph is None

        new_netx.use(random_instance_id)
        assert new_netx.graph is not None
        assert isinstance(new_netx.graph, networkx.Graph)
        
        new_netx.delete()
        assert netx.exists_in_storage(random_instance_id) == False
        netx.delete()
        
        assert new_netx.graph is None
        assert netx.graph is None
        