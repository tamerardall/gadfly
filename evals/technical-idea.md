# Proposal: Nimbus, a vector database written from scratch in Go

Our team stores about two million document embeddings and queries them from a support chatbot. We currently run a managed vector database, and the monthly bill keeps growing. I propose we write our own vector database in Go and move off the managed service within one quarter.

The design is simple. Nimbus keeps every vector in memory on a single server and answers nearest-neighbour queries with a brute-force cosine scan. A small HTTP API accepts inserts and queries. Persistence is a nightly snapshot to local disk. Because the scan is plain Go with no external dependencies, there is nothing to learn and nothing to break.

For access control, the API sits on the internal network, so we will not add authentication in the first version. The chatbot passes the user's question straight into the query endpoint, and documents from every customer live in one shared index.

Two million vectors is small, and I expect queries to stay fast even if the data grows tenfold. We will measure latency after launch and optimise if needed. A custom system also lets us tune exactly for our use case, which the managed service never could.

I estimate four weeks of work for one engineer. After that the only cost is the server, so the saving is the whole managed bill. I would like approval to start next sprint.
