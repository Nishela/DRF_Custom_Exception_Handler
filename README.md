# DRF_Custom_Exception_Handler

1. Create an environment
2. Install requirements
3. Run server
4. Send a POST request to http://localhost:8000/custom/ with the following body

    ```json
    {
      "custom_field": 0
    }
    ```
    
    expected response:
    
    ```json
    {
      "msg": "ApiException was raised!"
    }
    ```

5. Send a POST request to http://localhost:8000/custom/ with the following body

    ```json
    {
      "custom_field": 1
    }
    ```
    
    expected response:
    
    ```json
    {
      "msg": "ChildApiException was raised!",
      "default_msg": "ChildApiException was raised!"
    }
    ```