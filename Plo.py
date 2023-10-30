import requests
from bs4 import BeautifulSoup
from IPython.display import HTML

# Replace the URL below with the Blogger post URL you provided
blogger_post_url = 'https://indianai2007.blogspot.com/2023/10/test.html?m=1'

# Send a request to the Blogger post URL
response = requests.get(blogger_post_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the post content
    post_content = soup.find('div', {'class': 'post-body'})

    if post_content:
        # Display the post content in the Colab notebook
        display(HTML(str(post_content)))
    else:
        print("Post content not found on the page.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
