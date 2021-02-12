# BASIC GCP ARCHITECTURE FOR A MVP

## Requirements

Bracelet to monitor and alert the user about biometric health (temperature, blood oxygen, etc)

<img src="./img/basic_requirements.png" width=400px>

* Technical requirements:

<img src="./img/tech_requirements.png" height=400px>


## General steps to follow

<img src="./img/steps.png" width=400px>


### Architecture

<img src="./img/architecture.png" width=400px>


### Data generator

Follow the steps in this [github](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/iot/api-client/mqtt_example) to create the data generator

It is also important to add a gateway with the public key and bind the device to it.

Finally, use the following command to start the generator

    ```py
    python cloudiot_mqtt_example.py \
        --registry_id=liip_biometric \
        --cloud_region=europe-west1 \
        --project_id=proven-verve-289913 \
        --device_id=liip_bracelet \
        --algorithm=RS256 \
        --private_key_file=rsa_private.pem \
        --gateway_id=liip_gateway
    ```


### Google architecture implementation

* IoT: https://cloud.google.com/iot/docs/quickstart




