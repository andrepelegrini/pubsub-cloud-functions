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

![passo3.1](https://user-images.githubusercontent.com/50640320/105197387-539d6280-5b1b-11eb-91b7-4e13fd41f4bb.png)

![passo3.2](https://user-images.githubusercontent.com/50640320/105197436-6152e800-5b1b-11eb-90bb-b9e50dcdf005.png)

4. **Write script**: firstly, choose each programming language is more suitable to you (Go, Java, Node.js and Python) in *runtime*. If Python is chosen, the block main.py will receive the code and requirements.txt the libraries and dependencies (package>=version). Important to remember that it is necessary to define a function where your transformation code will be written as this function name will be the used at the *Entry Point*, meaning this will be the function to be triggered once the message is received. Once the code is written, click on DEPLOY and your function will be online.

![passo4](https://user-images.githubusercontent.com/50640320/105208981-125f7f80-5b28-11eb-972e-90da654a35af.png)

An example of a code can be found [here](https://github.com/andrepelegrini/pubsub-cloud-functions/blob/master/code-example.py).

## Testing
Once the function is deployed correctly, it is possible to test it without the need to send a message to the topic. First, click on your function and then on TESTING, where it is possible to paste a test message (json format) inside the *triggering event* box. Secondly, click on TEST THE FUNCTION to run the test and receive the feedback at Output below. If the function is working properly, it returns an 'Ok'. Otherwise, the errors will be listed similar to a jupyter notebook. 

ps.: if the TEST THE FUNCTION option is not available once you paste the message, it means your json needs adjustments.

![testing](https://user-images.githubusercontent.com/50640320/105207697-931d7c00-5b26-11eb-80a9-6c1dbf2cf432.png)

**IMPORTANT**: remember that, as a safety measure, all messages reaching the topic are encrypted and this will be message consumed by your cloud function. However, inside the testing environment, the json will not be encrypted, in other words, it will return an error. In this case, it is possible to test your script by removing your decryption line in your code or supply the triggering event with an encrypted message.





