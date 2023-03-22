from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='5766c5c2b9d84c7ba5a9378cd31d6c30')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='abc-news,the-verge',
                                          category='holowod',
                                          language='en',
                                          country='in')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='abc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2013-03-01',
                                      to='2023-03-2',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()