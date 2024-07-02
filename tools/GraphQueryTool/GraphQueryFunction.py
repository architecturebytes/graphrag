from neo4j import GraphDatabase
import json

# NOTE: Remember that requirements.txt in Cloud Function should have 'neo4j' entry added to it.

# Initialize the Neo4j driver
def get_driver():
    # NOTE: It's a good idea to Get these from Secret Manager
    # NOTE: Make sure that uri, user and password are updated correctly.
    uri = "neo4j+s://xxxxxx.databases.neo4j.io"
    user = "neo4j"
    password = "------"
    return GraphDatabase.driver(uri, auth=(user, password))

# The main function that will be triggered by HTTP request
def execute_query(request):

    if 'query' in request.args:
        query = request.args['query']
    else:
        return json.dumps({'error': 'No query provided'}), 400

    driver = get_driver()

    try:
        with driver.session() as session:
            result = session.run(query)
            data = [record.data() for record in result]
            return json.dumps(data), 200
    except Exception as e:
        return json.dumps({'error': str(e)}), 500
    finally:
        driver.close()
