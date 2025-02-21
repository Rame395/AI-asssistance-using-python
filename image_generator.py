from openai import OpenAI
import user_config

client=OpenAI(api_key=user_config.openai_key)

response = client.images.generate(
    model="dall-e-2",
    prompt="small boy watching cartoon",
    n=2,
    size="1024x1024",
    quality="standard",
)

print(response.data[0].url)


# import openai
# import user_config
# openai.api_key = user_config.openai_key


# response = openai.Image.create(
#     model="dell-e-2",
#     prompt="small boy watching cartoon",
#     n=1,
#     size="1024x1024"
# )
# print(response['data'][0]['url'])
