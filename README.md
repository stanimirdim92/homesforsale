Here’s your formatted content in Markdown:


### Tech
- [x] Python - Django with DRF
- Nginx - must research load balancers, ASGI connector, and static file serve.
- OAuth2 maybe with Keycloak
- [x] PostgreSQL 16+
- Logbook for logs
- Elasticsearch
- GraphQL
- Sass
- Typescript
- React
- Leaflet for interactive maps or Maxar
- Kubernetes - Container orchestration platform for automating application deployment.
- Django Channels - Real-time communication with Django, enabling WebSockets.
- Celery - Task queue for handling asynchronous jobs.
- PostGIS - Geographic object extensions for PostgreSQL.




### Infrastructure
- AWS - RDS
- AWS - S3
- AWS - EC2
- Imgix - ?

### DevOps
- [x] Git
- [x] IntelliJ
- Github / Actions
- Docker
- Kafka and/or Apache Spark
- Hadoop - Framework for processing large datasets in distributed computing environments.
- [x] Redis still needs configuration
  - (Cluster for later?).
- Kibana?
- Onelogin?
- Terraform
- CircleCI - Continuous integration and delivery (CI/CD).
- Jenkins - Open-source automation server for CI/CD pipelines.
- ArgoCD - GitOps continuous delivery for Kubernetes.
- Ansible - Automation platform for configuration management.
- Puppet - IT automation software for managing configurations.
- Chef - Configuration management tool for automation.
- Consul - Service discovery, monitoring, and configuration.
- Vault - Securely store and access secrets, tokens, API keys, and certificates.
- Elastic Stack (ELK) - Elasticsearch, Logstash, and Kibana for log management.
- Fluentd - Unified logging layer for cloud environments.
- Azure DevOps - Microsoft’s DevOps platform for pipelines, repos, and testing.

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
- Datadog - Full-stack monitoring and security.
- New Relic - Application performance monitoring (APM) for cloud environments.
- Elastic APM - Distributed tracing and performance monitoring for applications.
- Honeycomb - Observability for understanding complex systems.
- Zabbix - Open-source monitoring solution for networks and applications.
- Nagios - Infrastructure monitoring for servers and networks.
- Splunk - Log management and monitoring, with machine learning-driven insights.
- AppDynamics - Performance monitoring for apps and business metrics.


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

### Analytics
- Mixpanel - Product and behavioral analytics.
- Hotjar - Heatmaps and user session recordings for behavior analysis.
- Heap - Automatically captures every event in a product for detailed analytics.
- Amplitude - Product analytics to understand user behavior and engagement.
- Segment - Customer data platform for collecting and routing analytics data.
- Looker - Business intelligence and data exploration.
- BigQuery - Google’s fully-managed, serverless data warehouse for analytics.
- Tableau - Data visualization and business intelligence.
- GA4
- FB Pixel


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
- setup mypy
- black
- flake
- isort




### Current used technologies
- Python 3.12+
- Django 5.1+
- djangorestframework 3.15+
- django-debug-toolbar 5.0+ - for debug test
- django-allauth - Login, 2FA etc.
- redis[hiredis] - caching is important
- psycopg3[pool, binary] - for PostgreSQL v16
- Click - for command line tools - no commands yet, but planned
- lxml - for XML parsing and security
- requests - for HTTP requests # change to httpx
- pytest - for testing - no test yet
- celery - for asynchronous tasks - not installed yet
- asyncio - for asynchronous tasks
- django-oauth-toolkit - for OAuth
- rosseta for languages
- django-storages for S3  - not installed yet
- 
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
