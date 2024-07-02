**Refer YouTube Video**: https://www.youtube.com/watch?v=QqqWlBhe_Ro

**tools/GraphQueryTool/GraphQueryFunction.py**<br>
This cloud function executes OpenCypher query passed to it as parameter against Neo4J database instance.

**tools/GraphQueryTool/GraphQueryTool/OpenAPISchema.yml**<br>
OpenAPI Schema that defines (the interfaces of) the above function (GraphQueryFunction.py).<br>
**_Important_**: In this schema - you must modify the function name URL, PATHS and operationId as per your implementation.

**FlightAgent**

Goal:<br>
Help customers find flight connections from one airport to another

Instructions:<br>
- Instructions:
- Your job is to generate OpenCypher queries, with no explanation or prefix.
- Use this Knowledge Graph only as sample data to understand nodes and their relationships. It is not exhaustive. Do not interpret it directly:
- CREATE (:Airport {name: 'JFK', city: 'New York'});
- CREATE (:Airport {name: 'LAX', city: 'Los Angeles'});
- MATCH (a1:Airport {name: 'JFK'}), (a2:Airport {name: 'LAX'})
- CREATE (a1)-[:FLIGHT_TO {flight_number: 'AA100', duration: 6, airline: 'American Airlines'}]->(a2);
- If user asks a question: Generate OpenCypher query in plain text with no explanation or prefix.
- Escape any special characters in the query that might be interpreted as YAML syntax.
- Invoke the ${TOOL:GraphQueryTool} with the escaped query as 'query' parameter.
- Interpret the results and provide an answer from it.

**GraphQueryTool**<br>
Description: 
Execute the Open Cypher query against Graph database
The tool should received Query parameter is plain text, and should not be treated as YAML.
