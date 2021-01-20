# pubsub-cloud-functions
A simple example of how to create your own Google Cloud Functions having a Pub/Sub message as the trigger event.

## Google Cloud Pub/Sub
According to the [documentation](https://cloud.google.com/pubsub/docs), Google Cloud Pub/Sub is an asynchronous messaging service that decouples services that produce events from services that process events. In our case, we use Pub/Sub to receive messages from other squads containing product information, such as registration forms.

## Google Cloud Functions
According to the [documentation](https://cloud.google.com/functions/docs), Google Cloud Functions is a lightweight compute solution for developers to create single-purpose, stand-alone functions that respond to cloud events without the need to manage a server or runtime environment. For us, the functions in two ways: first, the raw date is load into a specific bucket in Google Storage. Secondly, the data in transformed from a unnested json to a parquet, exploding the unnested fields into columns. Then, it is also loaded in Google Storage, now at a different bucket.

## Step by Step
1. **Create a topic**: as far as the Data team was concerned, our first step was to create a topic inside of a project. To this end, all you have to do is login with your account, enter Pub/Sub, click on **CREATE TOPIC** and choose its name.

![passo1](https://user-images.githubusercontent.com/50640320/105192154-97da3400-5b16-11eb-8af8-8267829a8e59.png)

2. **Create cloud function**: after the topic is created, click on **TRIGGER CLOUD FUNCTION** to write your own function. Once you click, the trigger type will be automatically defined as a *Cloud Pub/Sub trigger*, meaning your code will only run once the message reaches the chosen topic. Reminding that the function is triggered by the message which is on the *subscriber*, not the publisher. Once you create the function, the subscriber is generated automatically and linked to your topic. For other applications, it might be necessary to create it manually.

![passo2](https://user-images.githubusercontent.com/50640320/105194952-da9d0b80-5b18-11eb-8630-63475616813c.png)

3. **Cloud function configuration**: 
* *Function name*: name given to the function. Suggestion: choose the same name used on your topic;

* *Region*: change the default us-central1 to your region in order to avoid unnecessary costs e.g. Brazil: southamerica-east1;

* *VARIABLES, NETWORKING AND ADVANCED SETTINGS*: inside ADVANCED, I suggest replace 60 seconds timeout (default) to 540 (maximum). It better ensures the function will be executed without the risk of timing out before it is finished. 

