from datetime import date
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search, Integer, Completion, analyzer, tokenizer, Object, Q
from elasticsearch_dsl.query import MultiMatch, Match
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models
import csv
from django.contrib.auth.models import User
import datetime
import operator, functools

# This connections call should connect this to the elastic search cluster we have running on AWS via Elastic Cloud
# I ran bulk_indexing() through a shell on it once and it seemed to have uploaded most if not all of our data
# I don't think running bulk_indexing again would be needed since that data should reside in the cloud now, but I don't know
connections.create_connection(hosts=["https://dd90577b842c4f9396ca1846612e98df.us-east-1.aws.found.io:9243"],
                              http_auth=('elastic', 'Mq2jdfPLSRG1m8qxp4vd0qNa'))


# This is the code to use if you are chosing to run elastic search on your local machine instead of in the cloud
# connections.create_connection()

# my_analyzer = analyzer('my_analyzer', tokenizer=tokenizer('trigram', 'edge_gram', min_gram=1, max_gram=20), filter=['lowercase'])

class PolicyIndex(DocType):
    title = Text()
    school = Text()
    department = Text()
    administrator = Text()
    author = Text()
    state = Text()
    city = Text()
    latitude = Text()
    longitude = Text()
    link = Text()
    published_date = Date()
    tags = Text()
    abstract = Text()
    text = Text()


# if bulk_indexing() doesn't work due to space, try running
# curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": null}'

def bulk_indexing():
    es = Elasticsearch()
    PolicyIndex.init(index='policy-index')

    # unsure if this is needed, doesn't seem to be, can't remember why I had it in here
    # bulk(client=es, actions=(b.indexing() for b in models.Policy.objects.all().iterator()))

    # code to go into the csv file of data and add it to elasticsearch
    f = open('policy.csv', encoding="ISO-8859-1")
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        # handling of improperly formatted date entries
        # this assumes that dates are being entered into the database as MM/DD/YY (as the first couple thousand were)
        # and it formats them correctly in order to use Date() in elasticsearch. Since only two digits being
        # entered for year, assumes numbers <19 correspond to 21st century and rest to 20th.
        # Assigns 'None' when no date entered.
        date = row[11]
        date = date.split("/")
        try:
            if int(date[2]) <= 19:
                date[2] = "20" + date[2]
            else:
                date[2] = "19" + date[2]
            date = date[2] + "-" + date[0] + "-" + date[1]
        except:
            date = None

        # catch weird characters
        try:
            if datetime.datetime.strptime(date, '%Y-%m-%d'):
                row[11] = date
        except:
            row[11] = None

        # handling of weird characters appearing in lat and long entries
        try:
            row[8] = float(row[8][:2])
            row[9] = float(row[9][:2])
        except:
            row[8] = ""
            row[9] = ""
        blog = models.Policy.objects.get_or_create(title=row[1], school=row[2], department=row[3], administrator=row[4],
                                                   author=row[5], state=row[6], city=row[7], latitude=row[8],
                                                   longitude=row[9], link=row[10], published_date=row[11], tags=row[12],
                                                   abstract=row[13], text=row[14])[0]
        pass


# currently gets 100 results--will need to figure out a way to get best number of potentially useful results
def search(query, filter=None):
    s = Search(index='policy-index').query("multi_match", query=query,
                                           fields=["title", "school", "department", "administrator", "author", "state",
                                                   "city", "latitude", "longitude", "link", "tags", "abstract", "text"],
                                           fuzziness="AUTO").extra(from_=0, size=100)
    if filter is not None and len(filter) > 0:
        years = []
        schools = []
        for f in filter:
            try:
                f = int(f)
                years.append(Q('range', published_date={'gte': date(f, 1, 1), 'lt': date(f, 12, 31)}))
            except ValueError:
                schools.append(Q('match_phrase', school=f))
        if len(years) > 0 and len(schools) == 0:
            s = s.query("bool", filter=functools.reduce(operator.or_, years))
        if len(schools) > 0 and len(years) == 0:
            s = s.query("bool", filter=functools.reduce(operator.or_, schools))
        if len(schools) > 0 and len(years) > 0:
            combined = functools.reduce(operator.or_, years) & functools.reduce(operator.or_, schools)
            s = s.query("bool", filter=combined)
    response = s.execute()
    return response

# Functions similarly to search(), except results are found using prefix, only searching over title field, and object
# is used differently than the search() object is in the function calling search_suggest()

def search_suggest(query):
    query = query + "*"
    s = Search(index='policy-index').query("match_phrase_prefix", title=query)
    response = s.execute()
    return response
