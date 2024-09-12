Here’s your formatted content in Markdown:


### Tech
- Python - Django with DRF - DONE
- React
- Nginx - must research load balancers, ASGI connector, and static file serve.
  - OAuth2 maybe with Keycloak
  - PostgreSQL 15+
  - Logbook for logs?
  - Elasticsearch or GraphQL?
  - Sass
  - Typescript
  - Leaflet for interactive maps or Maxar
    django compressor
### Infra
- AWS - S3
- AWS - EC2
- Imgix - ?

### Utils
- GA4
- FB Pixel

### DevOps
- Git - DONE
- IntelliJ - DONE
- Github / Actions
- Docker
- Kafka and/or Apache Spark
- Redis (Cluster for later?)
- Kibana?
- Onelogin?
- Terraform

### AI
- Langchain
- Langsmith
- Langgraph
- OpenAI
- Pandas

### Monitoring
- Sentry
- Prometheus
- Airflow
- Kibana
- Grafana

### Payment Systems
- Stripe
- Revolut
- Paypal
- Bank

### Architecture
- Archimate

### Business Tools
- Jira
- Confluence
- Zendesk - for customer live support and internal communication.

---

# Todo
- [Werkzeug Documentation](https://werkzeug.palletsprojects.com/en/2.3.x/)
- [Django ASGI Deployment with Uvicorn](https://docs.djangoproject.com/en/dev/howto/deployment/asgi/uvicorn/)
- [Django ASGI Deployment with Hypercorn](https://docs.djangoproject.com/en/dev/howto/deployment/asgi/hypercorn/)
- Finish configs
- Finish testing setup - pytest
- Finish Docker
- Finish Black and Flake8
- Add Anymail


Here's a list of additional tools, technologies, and services you can include for each section:

### Monitoring
1. **Datadog** - Full-stack monitoring and security.
2. **New Relic** - Application performance monitoring (APM) for cloud environments.
3. **Elastic APM** - Distributed tracing and performance monitoring for applications.
4. **Honeycomb** - Observability for understanding complex systems.
5. **Zabbix** - Open-source monitoring solution for networks and applications.
6. **Nagios** - Infrastructure monitoring for servers and networks.
7. **Splunk** - Log management and monitoring, with machine learning-driven insights.
8. **AppDynamics** - Performance monitoring for apps and business metrics.

### Analytics
1. **Mixpanel** - Product and behavioral analytics.
2. **Hotjar** - Heatmaps and user session recordings for behavior analysis.
3. **Heap** - Automatically captures every event in a product for detailed analytics.
4. **Amplitude** - Product analytics to understand user behavior and engagement.
5. **Segment** - Customer data platform for collecting and routing analytics data.
6. **Looker** - Business intelligence and data exploration.
7. **BigQuery** - Google’s fully-managed, serverless data warehouse for analytics.
8. **Tableau** - Data visualization and business intelligence.

### DevOps
1. **CircleCI** - Continuous integration and delivery (CI/CD).
2. **Jenkins** - Open-source automation server for CI/CD pipelines.
3. **ArgoCD** - GitOps continuous delivery for Kubernetes.
4. **Ansible** - Automation platform for configuration management.
5. **Puppet** - IT automation software for managing configurations.
6. **Chef** - Configuration management tool for automation.
7. **Consul** - Service discovery, monitoring, and configuration.
8. **Vault** - Securely store and access secrets, tokens, API keys, and certificates.
9. **Elastic Stack (ELK)** - Elasticsearch, Logstash, and Kibana for log management.
10. **Fluentd** - Unified logging layer for cloud environments.
11. **Azure DevOps** - Microsoft’s DevOps platform for pipelines, repos, and testing.

### Tech
1. **Kubernetes** - Container orchestration platform for automating application deployment.
2. **FastAPI** - Python framework for building APIs with high performance and speed.
3. **Django Channels** - Real-time communication with Django, enabling WebSockets.
4. **RabbitMQ** - Message broker for communication between services.
5. **Celery** - Task queue for handling asynchronous jobs.
6. **WebSockets** - Real-time bi-directional communication protocol.
7. **GraphQL** - Alternative to REST for APIs, allows clients to request exactly the data they need.
8. **Tornado** - Python framework for handling asynchronous networking.
9. **PostGIS** - Geographic object extensions for PostgreSQL.
10. **RedisGraph** - Graph database built on Redis for high-performance graph querying.
11. **D3.js** - JavaScript library for creating dynamic, interactive data visualizations.
12. **Hadoop** - Framework for processing large datasets in distributed computing environments.


### Current used technologies
- Python 3.12+
- Django 5.1+
- djangorestframework 3.15+
- django-debug-toolbar 5.0+ - for debug test
- django-allauth - Login, 2FA etc.
- redis[hiredis] - caching is important
- psycopg3[pool, binary] - for PostgreSQL
- Click - for command line tools
- lxml - for XML parsing and security
- requests - for HTTP requests
- pytest - for testing
- celery - for asynchronous tasks
- asyncio - for asynchronous tasks


### Features
- Login / Registration for user/ agent
- Notifications
- Notes
- Favorites
- PM
- Saved Searches
- Find an agent with search
- my listings
- blacklist?
- wallet?
- invoices?
- account close/delete?
- push notifications?
