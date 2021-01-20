# pubsub-cloud-functions
A simple example of how to create your own Google Cloud Functions having a Pub/Sub message as the trigger event.

## Google Cloud Pub/Sub
According to the [documentation](https://cloud.google.com/pubsub/docs), Google Cloud Pub/Sub is an asynchronous messaging service that decouples services that produce events from services that process events. In our case, we use Pub/Sub to receive messages from other squads containing product information, such as registration forms.

## Google Cloud Functions
According to the [documentation](https://cloud.google.com/functions/docs), Google Cloud Functions is a lightweight compute solution for developers to create single-purpose, stand-alone functions that respond to cloud events without the need to manage a server or runtime environment. For us, the functions in two ways: first, the raw date is load into a specific bucket in Google Storage. Secondly, the data in transformed from a unnested json to a parquet, exploding the unnested fields into columns. Then, it is also loaded in Google Storage, now at a different bucket.

## Step by Step
1. **Create a topic**: as far as the Data team was concerned, our first step was to create a topic inside of a project. To this end, all you have to do is login with your account, enter Pub/Sub, click on **CREATE TOPIC** and choose its name.
![passo1](https://user-images.githubusercontent.com/50640320/105192154-97da3400-5b16-11eb-8af8-8267829a8e59.png)


