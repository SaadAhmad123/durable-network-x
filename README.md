# Durable NetworkX

### Introduction

Durable NetworkX is an extension to the popular Python package NetworkX, providing persistence capabilities for graph objects. By seamlessly integrating with NetworkX, Durable NetworkX offers users the ability to not only perform complex graph operations but also to store and manage graph data across sessions, ensuring data durability and easy retrieval.

### Why use Durable NetworkX?

1. **Integrated Experience with NetworkX**: If you are already familiar with NetworkX, integrating Durable NetworkX is straightforward. You can perform all the graph operations that NetworkX provides while also enjoying the added persistence capabilities of Durable NetworkX.

2. **Data Durability**: With Durable NetworkX, you no longer need to worry about losing your graph data after your Python session ends. Your graph data will persist, allowing you to load it in subsequent sessions, making it ideal for long-term projects and research.

3. **Versatile Storage Options**: Durable NetworkX offers multiple storage manager implementations, including `LocalFileStorageManager` for storing on the local filesystem and `S3StorageManager` for storing on Amazon S3. This flexibility ensures that you can choose the storage solution that best fits your project needs.

4. **Easy Management of Graph Instances**: With the ability to create new instances, use existing ones, and delete instances, managing your graph datasets becomes hassle-free. This is especially beneficial for projects that deal with multiple graph datasets.

5. **Storage Efficiency**: Durable NetworkX uses the GraphML format for storage, ensuring that your graph data is stored in a structured and efficient manner, which is also widely supported for interoperability with other graph processing tools.

6. **Scalable**: Leveraging cloud storage solutions like Amazon S3 means that as your data grows, you can easily scale your storage without worrying about infrastructure.

7. **Enhanced Data Security**: By using storage solutions like Amazon S3, you can benefit from the built-in security measures provided by these platforms, ensuring your graph data remains protected.

### How to Use Durable NetworkX?

1. **Installation**: 
You can add in your project
```
pip install durable-network-x
```
Or, if you are using poetry
```
poetry add durable-network-x
```

2. **Initialization**:
    ```python
    from durable_network_x.storage_managers.local_file_storage_manager import LocalFileStorageManager
    from durable_network_x import DurableNetworkX
    storage_manager = LocalFileStorageManager(root_dir="/path/to/store/data")
    durable_graph = DurableNetworkX(storage_manager=storage_manager)
    ```

3. **Creating a New Graph Instance**:
    ```python
    durable_graph.new(instance_id="my_graph")
    ```

4. **Working with the Graph**: All the operations you can perform on a NetworkX graph, you can perform on the `graph` property of the Durable NetworkX instance.
    ```python
    g = durable_graph.graph
    g.add_node(1)
    ```

5. **Saving Changes**: After performing operations, save the graph.
    ```python
    durable_graph.save()
    ```

6. **Loading an Existing Graph**:
    ```python
    durable_graph.use(instance_id="my_graph")
    ```

7. **Deleting a Graph Instance**:
    ```python
    durable_graph.delete()
    ```

### Using Amazon S3 as a Storage

To use Amazon S3, simply use the `S3StorageManager`.

```python
from durable_network_x.storage_managers.local_file_storage_manager import S3StorageManager

# Initialize a storage manager with the desired S3 bucket and credentials
storage_manager = S3StorageManager(bucket_name="my-s3-bucket", aws_access_key_id="YOUR_AWS_KEY", aws_secret_access_key="YOUR_AWS_SECRET")

# The rest of the operations remain the same
```

### Extending with Custom Storage Managers

Users can also define their own storage managers by inheriting from the `StorageManager` class and implementing the required methods (`read`, `write`, `delete`, and `exists`).

```
from durable_network_x.storage_managers import StorageManager
```

## Contributing

If you would like to contribute to `durable-network-x`, please fork the repository, make your changes, and submit a pull request. I appreciate all contributions and feedback!

## License

[MIT](LICENSE.md) 


Enjoy using `durable-network-x` and have fun building durable graph applications!