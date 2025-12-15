import requests
import json
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

class NewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("News App")
        self.root.geometry("600x500")
        self.root.configure(bg="black")

        # News API URL (Replace 'YOUR_ACTUAL_API_KEY' with an actual API key)
       # Replace with your actual API key
        self.url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY"


        self.data = self.fetch_news()
        self.current_index = 0

        # UI Components
        self.title_label = Label(root, text="", font=("Verdana", 16, "bold"), bg="black", fg="white", wraplength=550)
        self.title_label.pack(pady=20)

        self.news_image_label = Label(root, bg="black")
        self.news_image_label.pack()

        self.desc_label = Label(root, text="", font=("Verdana", 12), bg="black", fg="white", wraplength=550)
        self.desc_label.pack(pady=10)

        # Buttons
        self.btn_prev = Button(root, text="Previous", command=self.prev_news, font=("Verdana", 12), bg="gray", fg="white")
        self.btn_prev.pack(side=LEFT, padx=20, pady=20)

        self.btn_next = Button(root, text="Next", command=self.next_news, font=("Verdana", 12), bg="gray", fg="white")
        self.btn_next.pack(side=RIGHT, padx=20, pady=20)

        self.btn_details = Button(root, text="Read More", command=self.open_article, font=("Verdana", 12), bg="blue", fg="white")
        self.btn_details.pack(pady=10)

        # Show first news article
        self.show_news()

    def fetch_news(self):
        """Fetch news data from the API"""
        try:
            response = requests.get(self.url)
            news_data = response.json()

            # Print the response to check the structure (for debugging)
            print(json.dumps(news_data, indent=4))  # Pretty-print the response

            # Check for 'articles' key in the response
            if 'articles' in news_data:
                return news_data['articles']
            else:
                print("Error: 'articles' not found in the response")
                return []

        except Exception as e:
            print("Error fetching news:", e)
            return []

    def show_news(self):
        """Display news title, image, and description"""
        if not self.data:
            self.title_label.config(text="No news available.")
            return

        article = self.data[self.current_index]
        self.title_label.config(text=article["title"])

        # Load Image
        image_url = article.get("urlToImage", "")
        if image_url:
            image_response = requests.get(image_url)
            img_data = Image.open(BytesIO(image_response.content))
            img_data = img_data.resize((500, 250))
            img = ImageTk.PhotoImage(img_data)
            self.news_image_label.config(image=img)
            self.news_image_label.image = img
        else:
            self.news_image_label.config(image="")

        # Description
        self.desc_label.config(text=article.get("description", "No description available."))

    def next_news(self):
        """Show next news article"""
        if self.current_index < len(self.data) - 1:
            self.current_index += 1
            self.show_news()

    def prev_news(self):
        """Show previous news article"""
        if self.current_index > 0:
            self.current_index -= 1
            self.show_news()

    def open_article(self):
        """Open the full news article in the web browser"""
        import webbrowser
        if self.data:  # Ensure there is news data available
            article_url = self.data[self.current_index].get("url", "")
            if article_url:
                webbrowser.open(article_url)
            else:
                print("No URL available for this article.")
        else:
            print("No article data available to open.")

# Run the App
root = Tk()
app = NewsApp(root)
root.mainloop()
