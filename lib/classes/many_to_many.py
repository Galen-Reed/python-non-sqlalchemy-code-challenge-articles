class Article:

    all=[]

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Title must be of type str.")
        if len(title) >= 5 and len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be between 5 and 50 characters.")
        self.author = author
        self.magazine = magazine

        Article.all.append(self)
        

    @property
    def title(self):
        return self._title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Author must be of type str.")
        if len(name) == 0:
            raise ValueError("Author must be longer than 0 characters.")
        self._name = name

    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if not self.magazines():
            return None
        topics = set()
        for magazine in self.magazines():
            topics.add(magazine.category)
        return list(topics)
    
class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")

        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in Article.all if article.magazine == self})

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        author_article_counts = {}
        for article in Article.all:
            if article.magazine == self:
                author_article_counts[article.author] = author_article_counts.get(article.author, 0) + 1

        authors = [author for author, count in author_article_counts.items() if count > 2]
        return authors if authors else None