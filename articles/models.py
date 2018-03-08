from django.db import models

from articles import CrawlData


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=False, null=False, db_column='post_title')
    content = models.TextField(blank=False, null=False, db_column='post_content')

    class Meta:
        db_table = 'wp_posts'

    # translate Chinese to English after clean the data, then save it to database.
    def tran_ch_to_en(self):
        self.title = translate(clean_data(self.title))
        self.content = translate(clean_data(self.content))
        self.save()

    # translate English to Chinese, then save it to database.
    def tran_en_to_ch(self):
        self.title = translate(self.title)
        self.content = translate(self.content)
        self.save()


# use the regular expression to remove html label included the data.
def clean_data(data):
    import re
    result = re.compile(r'<[^>]+>', re.S)
    cleaned_data = result.sub('', data)
    return cleaned_data


# use requests package to crawl data from the website.
def translate(query):
    crawl_data = CrawlData.crawl_data(query)
    return crawl_data
