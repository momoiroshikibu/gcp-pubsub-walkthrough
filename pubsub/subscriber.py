import os
import google.cloud
from google.cloud import pubsub_v1

project_id = os.environ.get('GOOGLE_CLOUD_PROJECT')
topic_name = os.environ.get('PUBSUB_TOPIC')

topic_name = f"projects/{project_id}/topics/{topic_name}"
subscription_name = f"projects/{project_id}/subscriptions/sample_subscriber"

subscriber = pubsub_v1.SubscriberClient()
try:
    subscriber.create_subscription(
        name=subscription_name,
        topic=topic_name
    )
except google.api_core.exceptions.AlreadyExists as e:
    print(e)

def callback(message):
    print(message.data)
    message.ack()

future = subscriber.subscribe(subscription_name, callback)
try:
    future.result()
except Exception as ex:
    subscription.close()
    raise